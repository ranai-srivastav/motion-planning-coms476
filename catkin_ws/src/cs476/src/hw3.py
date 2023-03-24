import json, sys, os, argparse
import matplotlib.pyplot as plt
from discrete_search import fsearch, ALG_BFS
from hw1 import Grid2DStates, GridStateTransition, Grid2DActions, draw_path
from hw2_chain_plotter import get_link_positions
from math import radians
import numpy

from shapely import Polygon, Point, intersects


LINK_ANGLES = [i - 180 for i in range(360)]
obstacle_list = []


def compute_Cobs(O, W, L, D):
    """Compute C-Space obstacles for a 2-link robot
    @type O:   a list of obstacles, where for each i, O[i] is a list [(x_0, y_0), ..., (x_m, y_m)]
               of coordinates of the vertices of the i^th obstacle
    @type W:   float, representing the width of each link
    @type L:   float, representing the length of each link
    @type D:   float, the distance between the two points of attachment on each link
    @return: a list of configurations (theta_1, theta_2) of the robot that leads to a collision
        between the robot and an obstacle in O.
    """
    """
        To return a list of all possible points that result in a collision
            I need two loops to go through each angle [t1, t2] and trnslate that to world coord (x1, y1)
            I should "move" the arm to that certain (x1, y1) position => get the polygon
            
            For each link:
                For each obstacle
                    Given two polygons, do they intersect?
    """
    # obstacle_list = []
    link_list = []
    
    C_obs = set()
    
    for obstacle in O:
        point_list = []
        for obs_vertex in obstacle:
            pt = Point(obs_vertex)
            point_list.append(pt)
        obstacle_list.append(Polygon(point_list))
    
    
    for t1 in LINK_ANGLES:
        for t2 in LINK_ANGLES:
            link_list = []
            has_collision = False
            
            config = (radians(t1), radians(t2))
            _, vert_list = get_link_positions(config, W, L, D)
            
            for link in vert_list:
                point_list = []
                for vertices in link:
                    pt = Point(vertices)
                    point_list.append(pt)
                link_list.append(Polygon(point_list))
                
            for obstacle in obstacle_list:
                if has_collision:
                    break
                
                for link in link_list:
                    if(intersects(obstacle, link)):
                        C_obs.add((t1, t2))
                        has_collision = True
    
    # Using a set to ensure checking conditions is O(1)
    C_obs = list(C_obs)
    C_obs = sorted(C_obs)
    # print(len(C_obs))
                        
    return C_obs
                        

def compute_Cfree(Cobs):
    """Compute the free space for a 2-link robot
    @type Cobs: a list of configurations (theta_1, theta_2) of the robot that leads to a collision
                between the robot and an obstacle in O.
    @return an instance of Grid2DStates that represents the free space
    """
    
    Cfree = Grid2DStates(-180, 180, -180, 180, Cobs)
    
    return Cfree
    


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Run forward search")
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
    XG = [tuple(x) for x in data["XG"]]
    U = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    return (O, W, L, D, xI, XG, U)


def finer_discretization_hw_3_ec(search_result):
    for i in range(len(search_result["path"])-1):
        p1 = numpy.array(search_result["path"][i])
        p2 = numpy.array(search_result["path"][i+1])
        
        dir = p2 - p1
        dir = 0.1 * dir

        for i in range(1, 10):
            temp = p1 + dir * i
            for obs in obstacle_list:
                if obs.contains(Point(temp)):
                    print(temp)

if __name__ == "__main__":
    args = parse_args()
    (O, W, L, D, xI, XG, U) = parse_desc(args.desc)
    Cobs = compute_Cobs(O, W, L, D)

    X = compute_Cfree(Cobs)
    f = GridStateTransition()
    U = Grid2DActions(X, f)

    search_result = fsearch(X, U, f, xI, XG, ALG_BFS)
    
    finer_discretization_hw_3_ec(search_result)
    
    result = {"Cobs": Cobs, "path": search_result["path"]}

    with open(args.out, "w") as outfile:
        json.dump(result, outfile)

    fig, ax = plt.subplots()
    X.draw(ax, grid_on=False, tick_step=[30, 30])
    draw_path(ax, search_result["path"])
    plt.show()