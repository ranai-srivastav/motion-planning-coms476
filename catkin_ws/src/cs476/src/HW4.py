import argparse
import matplotlib.pyplot as plt
from obstacle import Obstacles, CircularObstacle
from world import World
from graph import Graph
from planning import *


def run_rrt():
    rrt_exploration = RRT(world, obs, 100)
    rrt_exploration.rrt_exploration()
    print_world(obs.get_obstacles(), world, rrt_exploration.rrt_graph)

    rrt_obs = RRT(world, obs, 100)
    rrt_obs.rrt_exploration_with_collisions()
    print_world(obs.get_obstacles(), world, rrt_obs.rrt_graph)

    rrt_path = RRT(world, obs, 500)
    rrt_path.rrt_path_gen()
    # print_world(obs.get_obstacles(), world, rrt_path.rrt_graph, print_path=False)
    print_world(obs.get_obstacles(), world, rrt_path.rrt_graph, print_path=True)


def run_prm():
    pass


def print_world(obstacles: list, world: World, graph: Graph, print_path: bool = False):
    x1, y1 = obstacles[0].exterior.xy
    x2, y2 = obstacles[1].exterior.xy

    plt.figure(figsize=(18, 3))
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.ylim((world.get_y_min(), world.get_y_max()))
    plt.xlim((world.get_x_min(), world.get_x_max()))

    x = []
    y = []

    for edge in graph.get_all_graph_edges():
        if edge.point1 == world.get_init_state():
            plt.plot(edge.point1.x, edge.point1.y, 'bo')
            plt.plot(edge.point2.x, edge.point2.y, 'ko')
        elif edge.point1 == world.get_goal_state():
            plt.plot(edge.point1.x, edge.point1.y, 'bx')
            plt.plot(edge.point2.x, edge.point2.y, 'ko')
        elif edge.point2 == world.get_init_state():
            plt.plot(edge.point1.x, edge.point1.y, 'ko')
            plt.plot(edge.point2.x, edge.point2.y, 'bo')
        elif edge.point2 == world.get_goal_state():
            plt.plot(edge.point1.x, edge.point1.y, 'ko')
            plt.plot(edge.point2.x, edge.point2.y, 'bx')
        else:
            plt.plot(edge.point1.x, edge.point1.y, 'ko')
            plt.plot(edge.point2.x, edge.point2.y, 'ko')
        plt.plot([edge.point1.x, edge.point2.x], [edge.point1.y, edge.point2.y], 'k-')

    plt.plot(world.get_init_state().x, world.get_init_state().y, 'bo')
    plt.plot(world.get_goal_state().x, world.get_goal_state().y, 'bx')

    if print_path:
        goal_state = None
        for point in graph.vert_list:
            if point == world.get_goal_state():
                goal_state = point
                break

        if goal_state is None or goal_state.parent is None:
            print("COULD NOT FIND VALID PATH IN THE SET NUMBER OF ITERATIONS")
            return
        else:
            curr_state = goal_state

            while curr_state.parent is not None:
                parent = curr_state.parent
                plt.plot([parent.x, curr_state.x], [parent.y, curr_state.y], 'bs-')

                curr_state = parent

    plt.show()


if __name__ == '__main__':

    #################################
    # Define default values here
    #################################
    default_step_size = 0.05
    xG = Point(2., -0.5)
    xI = Point(-2., -0.5)

    dt = -1 # Define dt using the cmd args --dt=[value]

    parser = argparse.ArgumentParser()

    parser.add_argument("--rrt", action="store_true")
    parser.add_argument("--prm", action="store_true")
    parser.add_argument("--dt", type=float)

    args = parser.parse_args()

    # print(args.dt)

    if args.dt is not None:
        dt = args.dt
    else:
        dt = 0.01

    world = World(-3., 3., -1., 1., dt=dt, step_size=default_step_size, xG=xG, xI=xI)
    cir_obs = CircularObstacle()
    bot, top = cir_obs(dt, world)
    obs = Obstacles()
    obs.add_to_obstacle_list(bot)
    obs.add_to_obstacle_list(top)

    run_rrt()
    if args.rrt:
        print("Running RRT")
    elif args.prm:
        print("Running PRM")
        run_prm()
    else:
        print("usage: python3 HW4.py [--rrt/--prm] [--dt]")
        print("You will have to select either PRM or RRT")
        print("If you included both, RRT will run")
