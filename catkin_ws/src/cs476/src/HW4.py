import argparse
import matplotlib.pyplot as plt
from obstacle import Obstacles, CircularObstacle
from world import World
from graph import Graph
from planning import *


def run_rrt():
    # rrt_exploration = RRT(world, obs, 100)
    # rrt_exploration.rrt_exploration()
    # print_world(obs.get_obstacles(), world, rrt_exploration.rrt_graph)

    rrt_obs = RRT(world, obs, 100)
    rrt_obs.rrt_exploration_with_collisions()
    print_world(obs.get_obstacles(), world, rrt_obs.rrt_graph)


def run_prm():
    pass


def print_world(obstacles: list, world: World, graph: Graph):
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

    plt.show()


if __name__ == '__main__':

    dt = -1

    parser = argparse.ArgumentParser()

    parser.add_argument("--rrt", action="store_true")
    parser.add_argument("--prm", action="store_true")
    parser.add_argument("--dt", type=float)

    args = parser.parse_args()

    # print(args.dt)

    xG = Point(2., -0.5)
    xI = Point(-2., -0.5)

    if args.dt is not None:
        dt = args.dt
    else:
        dt = 0.1

    world = World(-3., 3., -1., 1., dt, xG=xG, xI=xI)
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
