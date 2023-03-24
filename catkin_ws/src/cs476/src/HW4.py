import argparse
import matplotlib.pyplot as plt
from src.cs476.src.obstacle import Obstacles, CircularObstacle 
from src.cs476.src.world import World

def run_rrt():
    pass

def run_prm():
    pass

def print_world(obstacles: list):
    x1, y1 = obstacles[0].exterior.xy
    x2, y2 = obstacles[1].exterior.xy
    print()
    fig = plt.figure(figsize=(60, 10))
    plt.plot(x1, y1)
    plt.plot(x2, y2)
    plt.xlim((world.get_x_min(), world.get_x_max()))
    plt.ylim((world.get_y_min(), world.get_y_max()))
    
    plt.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--rrt", action="store_true")
    parser.add_argument("--prm", action="store_true")
    
    args = parser.parse_args()
    
    world = World(-3., 3., -1., 1.)
    cir_obs = CircularObstacle()
    bot, top = cir_obs(0.02, world)
    obs = Obstacles()
    obs.add_to_obstacle_list(bot)
    obs.add_to_obstacle_list(top)
    
    print_world(obs.get_obstacles())
    
    if args.rrt:
        print("Running PRM")
        run_rrt()
    elif args.prm:
        print("Running RRT")
        run_prm()
    else:
        print("usage: python3 HW4.py [--rrt/--prm]")
        print("You will have to select either PRM or RRT")
        print("If you included both, RRT will run")