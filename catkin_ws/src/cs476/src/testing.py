from planning import *
from world import World
import HW4
from obstacle import *
from world import World


if __name__ == "__main__":

    world = World(-3, 3, -1, 1, 0.1, 0.05, xI = Point(-3, 0.75), xG = Point(2, -0.5))

    cir_obs = CircularObstacle()
    bot, top = cir_obs(0.4, world)
    obs = Obstacles()
    obs.add_to_obstacle_list(bot)
    obs.add_to_obstacle_list(top)

    # # rrt = RRT(world, obs, 0)
    # rrt_graph = Graph(0.1)
    # rrt_graph.add_edge(Edge(world.get_init_state(), world.get_goal_state()))
    # rrt_graph.add_edge(Edge(Point(-1, -0.25), Point(2, -0.25)))

    # new_point = Point(0, -1)
    # # TODO make this addRandomPointToGraph() method
    # closest_edge = rrt_graph.get_closest_edge(new_point)
    # edge1, edge2, closest_point_on_edge = closest_edge.split_edge(new_point)
    # rrt_graph.rm_edge(closest_edge)
    # # TODO if one of them is null, no need to remove
    # if edge1 is not None:
    #     rrt_graph.add_edge(edge1)
    # if edge2 is not None:
    #     rrt_graph.add_edge(edge2)
    # rrt_graph.add_edge(Edge(closest_point_on_edge, new_point))
    #
    # HW4.print_world(obs.get_obstacles(), world, rrt_graph)
    # coll = CollisionChecker(obs.get_obstacles(), world)
    # e = Edge(Point(-2, -0.5), Point(2, -0.5))
    #
    rrt_graph = Graph(0.01)
    # rrt_graph.add_edge(e)
    # print(coll.edge_in_collision(e))
    # print(coll.closest_pt_on_line_outside_obs(e))

    # print(coll.point_in_obs(p))

    set_of_points = [Point(-1, 0.75), Point(-2, -0.75), Point(0, -1), Point(0.5, 0), Point(3, 0), world.get_goal_state()]

    collision_detector = CollisionChecker(obs.get_obstacles(), world)
    rrt_graph.add_vertex(world.get_init_state())
    new_point = set_of_points[0]
    new_point.set_parent(world.get_init_state())

    ai_edge = Edge(world.get_init_state(), new_point)
    new_point = collision_detector.closest_pt_on_line_outside_obs(ai_edge)
    new_point.set_parent(world.get_init_state())

    ai_edge = Edge(world.get_init_state(), new_point)
    rrt_graph.add_edge(ai_edge)
    HW4.print_world(obs.get_obstacles(), world, rrt_graph)

    for i in set_of_points[1:]:
        new_point = i
        closest_edge = rrt_graph.get_closest_edge(new_point)
        edge1, edge2, closest_point_on_edge = closest_edge.split_edge(new_point)
        new_point.set_parent(closest_point_on_edge)
        ai_edge = Edge(closest_point_on_edge, new_point)

        if collision_detector.edge_in_collision(ai_edge):
            new_point = collision_detector.closest_pt_on_line_outside_obs(ai_edge)
            new_point.set_parent(closest_point_on_edge)
            ai_edge = Edge(closest_point_on_edge, new_point)

        rrt_graph.rm_edge(closest_edge)

        if edge1 is not None:
            rrt_graph.add_edge(edge1)
        if edge2 is not None:
            rrt_graph.add_edge(edge2)

        rrt_graph.add_edge(ai_edge)

        if ai_edge.point2 == world.get_goal_state():
            break
        if ai_edge.point1 == world.get_goal_state():
            print("ARE YOUR EDGES REVERSED")
            break
        HW4.print_world(obs.get_obstacles(), world, rrt_graph)
    HW4.print_world(obs.get_obstacles(), world, rrt_graph, print_path=True)

