import argparse
import matplotlib.pyplot as plt
from src.cs476.src.obstacle import Obstacles, CircularObstacle 
from src.cs476.src.world import World
from graph import Graph
from planning import *

def run_rrt():
    
    rrt = RRT(world, obs)
    rrt.rrt_exploration()
    print_world(obs.get_obstacles(), world, rrt.rrt_graph)
    

def run_prm():
    pass

def print_world(obstacles: list, world: World, graph:Graph):
    x1, y1 = obstacles[0].exterior.xy
    x2, y2 = obstacles[1].exterior.xy

    plt.figure(figsize=(60, 10))
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.xlim((world.get_x_min(), world.get_x_max()))
    plt.ylim((world.get_y_min(), world.get_y_max()))
    
    x = []
    y = []
    for edge in Graph.get_all_graph_edges():
        if edge.point1 == world.get_goal_state() or edge.point1 == world.get_init_state() or \
           edge.point2 == world.get_goal_state() or edge.point2 == world.get_init_state():
               continue
        
        plt.plot([edge.point1.x, edge.point2.x], [edge.point1.y, edge.point2.y], 'k-')

    plt.plot(world.get_goal_state().x, world.get_goal_state().y, 'bx')
    plt.plot(world.get_init_state().x, world.get_init_state().y, 'bo')
    
    plt.show()
    
    

if __name__ == '__main__':
    
    dt = -1
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--rrt", action="store_true")
    parser.add_argument("--prm", action="store_true")
    parser.add_argument("--dt", type=float)

    args = parser.parse_args()
    
    print(args.dt)
    
    xG = Point(2., -0.5)
    xI = Point(-2., -0.5)
    
    world = World(-3., 3., -1., 1., xG = xG, xI = xI)
    cir_obs = CircularObstacle()
    bot, top = cir_obs(0.02, world)
    obs = Obstacles()
    obs.add_to_obstacle_list(bot)
    obs.add_to_obstacle_list(top)
    
    run_rrt()
    
    if args.rrt:
        print("Running PRM")
        run_rrt()
    elif args.prm:
        print("Running RRT")
        run_prm()
    else:
        print("usage: python3 HW4.py [--rrt/--prm] [--dt]")
        print("You will have to select either PRM or RRT")
        print("If you included both, RRT will run")