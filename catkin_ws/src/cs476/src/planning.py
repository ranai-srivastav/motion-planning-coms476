from graph import Graph
from geometry import Edge, Point
from world import World
from obstacle import Obstacles
from random import randint, uniform


class DistanceComputator:

    @staticmethod
    def EuclideanDistanceComputator(vertex1, vertex2):
        return Edge.get_two_point_euclidean_distance(vertex1, vertex2)


class CollisionChecker:
    def is_in_collision():
        False


class RRT:
    def __init__(self, world: World, obs: Obstacles, max_iter: int = 1000):
        self.world = world
        self.obs = obs
        self.max_iter = max_iter

        self.rrt_graph = Graph(0.1)

    def gen_random_point(self) -> Point:
        """ returns a random Point object in the CSpace
        """
        choose_goal = randint(0, 100) <= 10

        if choose_goal:
            return self.world.get_goal_state()
        else:
            x = round(uniform(self.world.get_x_min(), self.world.get_x_max()), 2)
            y = round(uniform(self.world.get_y_min(), self.world.get_y_max()), 2)
            return Point(x, y)

    def rrt_exploration(self):

        self.rrt_graph.add_vertex(self.world.get_init_state())
        self.rrt_graph.add_edge(Edge(self.world.get_init_state(), self.gen_random_point()))

        for i in range(self.max_iter):
            new_point = self.gen_random_point()
            # TODO make this addRandomPointToGraph() method
            closest_edge = self.rrt_graph.get_closest_edge(new_point)
            print(closest_edge)
            # TODO get the point on the edge, not the randomly gen point
            edge1, edge2, closest_point_on_edge = closest_edge.split_edge(new_point)
            self.rrt_graph.rm_edge(closest_edge)
            # TODO if one of them is null, no need to remove
            if edge1 is not None:
                self.rrt_graph.add_edge(edge1)
            if edge2 is not None:
                self.rrt_graph.add_edge(edge2)
            self.rrt_graph.add_edge(Edge(closest_point_on_edge, new_point))
