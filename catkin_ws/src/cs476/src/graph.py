from geometry import Point, Edge


class Graph:
    """The main Graph class that holds the RRT Graph using an Adjacency list interpretation. Initialize it with Step size

    """
    def __init__(self, step_size) -> None:
        self.adj_list = dict()
        self.vert_list = set()
        self.step_size = step_size

    def add_vertex(self, vertex: Point):
        """ Adds a vertex to the graph, checking if it doesn't already exist

        @param vertex: The vertex to be added of type Point
        @return: Nothing
        """
        if vertex not in self.vert_list:
            self.adj_list[vertex] = []
            self.vert_list.add(vertex)

    def add_edge(self, e1: Edge):
        """Add an edge into the graph, checking if the edge is not None

        @param e1: The edge to be added, Must be of type Edge
        @return: Nothing
        """

        if e1 is not None:
            self.add_vertex(e1.point1)
            self.add_vertex(e1.point2)

            self.adj_list[e1.point1].append(e1.point2)
            # self.adj_list[e1.point2].append(e1.point1)

    def rm_edge(self, e: Edge):
        """ Removes an edge from the graph

        @param e: The edge to be removed
        @return:
        """
        self.adj_list[e.point1].remove(e.point2)
        # self.adj_list[e.point2].remove(e.point1)

    def get_neighbors(self, vertex: Point):
        """ returns all the neigbors of a Point i.e. it's adj list

        @param vertex:
        @return:
        """
        return self.adj_list[vertex]

    def get_all_graph_edges(self) -> list:
        """return all the graph's edges

        @return: A list with all the edges in the Graph
        """
        edges = []

        for org in self.adj_list.keys():
            for v in self.get_neighbors(org):
                edges.append(Edge(org, v))

        return edges

    def get_closest_edge(self, point: Point) -> Edge:
        """ returns the closest edge to a given point in the graph from all the edges in the graph

        @param point: Euclidean distance is calculated to edges from this point
        @return:
        """

        min_edge = Edge(Point(+100, +100), Point(+100, +100))
        min_dist = 100

        edges = self.get_all_graph_edges()

        for edge in edges:
            discretizations = edge.get_discritized_edge(self.step_size)
            for step in discretizations:
                dist = Edge.get_two_point_euclidean_distance(step, point)
                if dist < min_dist:
                    min_dist = dist
                    min_edge = edge

        return min_edge
