from planning import *
from world import World


if __name__ == "__main__":
    
    world = World(-3, 3, -1, 1, Point(0.5, 1), Point(-1, 2))
    rrt = RRT(world, None, 1000)
    
    e1 = Edge(Point(0, 0), Point(5, 5))
    p1 = Point(0, 4)
    
    split = e1.get_nearest_point(p1)
    print(split)
    # s1, s2 = Edge.split_edge(e1, p1)
    # print(s1.point1)
    # print(s1.point2)
    # print(s2.point1)
    # print(s2.point2)