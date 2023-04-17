import argparse
import json
import os
import sys
import matplotlib.pyplot as plt
import numpy
from draw_cspace import draw
from planning import EuclideanDistanceComputator, StraightEdgeCreator, LinkCollisionChecker
from obstacle import LinkObstacle
from planning import rrt


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Run search")
    parser.add_argument(
        "desc",
        metavar="problem_description_path",
        type=str,
        help="path to the problem description file containing the obstacle region in the world as well as the size and shape of the robot, including the width and length of each link, and the distance between two points of attachment",
    )
    parser.add_argument(
        "--out",
        metavar="output_path",
        type=str,
        required=False,
        default="",
        dest="out",
        help="path to the output file",
    )

    args = parser.parse_args(sys.argv[1:])
    if not args.out:
        args.out = os.path.splitext(os.path.basename(args.desc))[0] + "_out" + ".json"

    print("Problem description: ", args.desc)
    print("Output:              ", args.out)

    return args


def parse_desc(desc):
    """Parse problem description json file to get the problem description"""
    with open(desc) as desc:
        data = json.load(desc)

    O = data["O"]
    W = data["W"]
    L = data["L"]
    D = data["D"]
    xI = tuple(data["xI"])
    xG = tuple(data["xG"])
    return O, W, L, D, xI, xG


def visualize_obstacles(ax):
    for theta1 in numpy.linspace(-numpy.pi, numpy.pi, 250):
        for theta2 in numpy.linspace(-numpy.pi, numpy.pi, 250):
            if collision_checker.is_in_collision([theta1, theta2]):
                ax.plot(theta1, theta2, "g.")


def print_json(rrt_graph, xI, xG, filename):
    """ writes to a json_file
    @author ranais@iastate.edu
    @param rrt_graph: the graph that rrt() function returns
    @param xI: The initial state
    @param xG: The final state
    @return:
    """
    vertices = []
    for i, vertex in enumerate(rrt_graph.vertices):
        d = {}
        d["id"] = i
        x = rrt_graph.vertices[i][0]
        y = rrt_graph.vertices[i][1]
        d["config"] = [x, y]
        vertices.append(d)

    edge_list = []
    for i, edges in enumerate(rrt_graph.edges.keys()):
        edge_list.append([edges[0], edges[1]])

    path = []
    goal = -1
    for key, value in rrt_graph.vertices.items():
        if value[0] == xG[0] and value[1] == xG[1]:
            goal = key

    while goal > 0:
        path.insert(0, goal)
        goal = rrt_graph.parents[goal][0] if isinstance(rrt_graph.parents[goal], list) else rrt_graph.parents[goal]

    answer = {}
    answer["vertices"] = vertices
    answer["edges"] = edge_list
    answer["path"] = path

    json_object = json.dumps(answer, indent=4)

    with open(filename, "w+") as op_file:
        op_file.write(json_object)


if __name__ == "__main__":

    # ##################################### SCRIPT PARAMETERS #########################
    prob_goal = 0.1
    # ##################################### SCRIPT PARAMTERS  #########################

    args = parse_args()
    O, W, L, D, xI, xG = parse_desc(args.desc)
    cspace = [(-numpy.pi, numpy.pi), (-numpy.pi, numpy.pi)]

    obstacles = []
    for obs_vert in O:
        obstacles.append(LinkObstacle(obs_vert, W, L, D).shapely_poly)

    edge_creator = StraightEdgeCreator(0.1)
    collision_checker = LinkCollisionChecker(W, L, D, obstacles)
    distance_computator = EuclideanDistanceComputator()

    # num_blank = 0
    # for i in range(1000):

    rrt_graph, root, goal = rrt(cspace, xI, xG, edge_creator, distance_computator, collision_checker, pG=prob_goal)

    fig, ax = plt.subplots()
    if goal is not None:
        path = rrt_graph.get_path(root, goal)
    else:
        path = []
        # num_blank += 1
    draw(ax, cspace, O, xI, xG, rrt_graph, path, "RRT for a 2 link robot")

    # visualize_obstacles(ax)
    plt.show()

    # print(f"{num_blank}/1000")
    print_json(rrt_graph, xI, xG, args.out)
