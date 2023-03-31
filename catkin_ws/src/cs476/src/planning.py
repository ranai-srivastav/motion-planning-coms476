import shapely
from shapely import LineString
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
    def __init__(self, obs: list, world: World):
        self.obstacle_list = obs
        self.world = world
        self.circ_obs_radius = (world.get_width() - world.dt) / 2.0

    def edge_in_collision(self, edge: Edge) -> bool:
        line = LineString([[edge.point1.x, edge.point1.y], [edge.point2.x, edge.point2.y]])

        for obs in self.obstacle_list:
            if obs.intersects(line):
                return True
        return False

    def point_in_obs(self, point: Point) -> bool:
        for obs in self.obstacle_list:
            if obs.contains(shapely.Point(point.x, point.y)):
                return True

        if Edge.get_two_point_euclidean_distance(point, Point(0, 1)) <= self.circ_obs_radius:
            return True
        if Edge.get_two_point_euclidean_distance(point, Point(0, -1)) <= self.circ_obs_radius:
            return True
        return False

    def closest_pt_on_line_outside_obs(self, edge: Edge):
        """

        @param edge:
        @return:
        """
        discretizations = edge.get_discritized_edge(self.world.get_step_size())

        prev_point = discretizations[0]
        for point_on_line in discretizations[1:]:
            if self.point_in_obs(point_on_line):
                return prev_point
            prev_point = point_on_line

        return discretizations[-1]

class RandomPointGenerator:
    def __init__(self, world: World):
        self.world = world

    def __call__(self):
        choose_goal = randint(0, 100) <= 10

        if choose_goal:
            return self.world.get_goal_state()
        else:
            x = round(uniform(self.world.get_x_min(), self.world.get_x_max()), 2)
            y = round(uniform(self.world.get_y_min(), self.world.get_y_max()), 2)
            return Point(x, y)


class RRT:
    def __init__(self, world: World, obs: Obstacles, max_iter: int = 1000):
        self.world = world
        self.obs = obs
        self.max_iter = max_iter
        self.get_random_point = RandomPointGenerator(world)

        self.rrt_graph = Graph(world.get_step_size())

    def rrt_exploration(self):

        self.rrt_graph.add_vertex(self.world.get_init_state())
        self.rrt_graph.add_edge(Edge(self.world.get_init_state(), self.get_random_point()))

        for i in range(self.max_iter):
            new_point = self.get_random_point()
            # TODO make this addRandomPointToGraph() method
            closest_edge = self.rrt_graph.get_closest_edge(new_point)
            edge1, edge2, closest_point_on_edge = closest_edge.split_edge(new_point)
            self.rrt_graph.rm_edge(closest_edge)
            # TODO if one of them is null, no need to remove
            if edge1 is not None:
                self.rrt_graph.add_edge(edge1)
            if edge2 is not None:
                self.rrt_graph.add_edge(edge2)
            self.rrt_graph.add_edge(Edge(closest_point_on_edge, new_point))

    def rrt_exploration_with_collisions(self):

        collision_detector = CollisionChecker(self.obs.get_obstacles(), self.world)

        self.rrt_graph.add_vertex(self.world.get_init_state())
        new_point = self.get_random_point()
        ai_edge = Edge(self.world.get_init_state(), new_point)
        new_point = collision_detector.closest_pt_on_line_outside_obs(ai_edge)
        ai_edge = Edge(self.world.get_init_state(), new_point)
        self.rrt_graph.add_edge(ai_edge)

        for i in range(self.max_iter):
            new_point = self.get_random_point()
            closest_edge = self.rrt_graph.get_closest_edge(new_point)
            edge1, edge2, closest_point_on_edge = closest_edge.split_edge(new_point)
            ai_edge = Edge(closest_point_on_edge, new_point)

            if collision_detector.edge_in_collision(ai_edge):
                new_point = collision_detector.closest_pt_on_line_outside_obs(ai_edge)
                ai_edge = Edge(closest_point_on_edge, new_point)

            self.rrt_graph.rm_edge(closest_edge)

            if edge1 is not None:
                self.rrt_graph.add_edge(edge1)
            if edge2 is not None:
                self.rrt_graph.add_edge(edge2)

            self.rrt_graph.add_edge(ai_edge)

    def rrt_path_gen(self):
        collision_detector = CollisionChecker(self.obs.get_obstacles(), self.world)

        self.rrt_graph.add_vertex(self.world.get_init_state())
        new_point = self.get_random_point()
        new_point.set_parent(self.world.get_init_state())

        ai_edge = Edge(self.world.get_init_state(), new_point)
        new_point = collision_detector.closest_pt_on_line_outside_obs(ai_edge)
        new_point.set_parent(self.world.get_init_state())

        ai_edge = Edge(self.world.get_init_state(), new_point)
        self.rrt_graph.add_edge(ai_edge)

        for i in range(self.max_iter):
            new_point = self.get_random_point()
            closest_edge = self.rrt_graph.get_closest_edge(new_point)
            edge1, edge2, closest_point_on_edge = closest_edge.split_edge(new_point)
            # TODO new addition be careful
            new_point.set_parent(closest_point_on_edge)
            ai_edge = Edge(closest_point_on_edge, new_point)

            if collision_detector.edge_in_collision(ai_edge):
                new_point = collision_detector.closest_pt_on_line_outside_obs(ai_edge)
                new_point.set_parent(closest_point_on_edge)
                ai_edge = Edge(closest_point_on_edge, new_point)

            self.rrt_graph.rm_edge(closest_edge)

            if edge1 is not None:
                self.rrt_graph.add_edge(edge1)
            if edge2 is not None:
                self.rrt_graph.add_edge(edge2)

            self.rrt_graph.add_edge(ai_edge)

            if ai_edge.point2 == self.world.get_goal_state():
                break
            if ai_edge.point1 == self.world.get_goal_state():
                print("ARE YOUR EDGES REVERSED")
                break


