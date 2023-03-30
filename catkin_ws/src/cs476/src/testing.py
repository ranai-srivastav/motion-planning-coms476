from planning import *
from world import World
import HW4
from obstacle import *
from world import World


if __name__ == "__main__":

    world = World(-3, 3, -1, 1, Point(-2, -0.5), Point(2, -0.5))

    cir_obs = CircularObstacle()
    bot, top = cir_obs(1, world)
    obs = Obstacles()
    obs.add_to_obstacle_list(bot)
    obs.add_to_obstacle_list(top)

    # rrt = RRT(world, obs, 0)
    rrt_graph = Graph(0.1)
    rrt_graph.add_edge(Edge(world.get_init_state(), world.get_goal_state()))
    rrt_graph.add_edge(Edge(Point(-1, -0.25), Point(2, -0.25)))

    new_point = Point(0, -1)
    # TODO make this addRandomPointToGraph() method
    closest_edge = rrt_graph.get_closest_edge(new_point)
    edge1, edge2, closest_point_on_edge = closest_edge.split_edge(new_point)
    rrt_graph.rm_edge(closest_edge)
    # TODO if one of them is null, no need to remove
    if edge1 is not None:
        rrt_graph.add_edge(edge1)
    if edge2 is not None:
        rrt_graph.add_edge(edge2)
    rrt_graph.add_edge(Edge(closest_point_on_edge, new_point))

    HW4.print_world(obs.get_obstacles(), world, rrt_graph)

