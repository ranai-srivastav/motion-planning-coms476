from geometry import Point, Edge

class Graph:
    def __init__(self, step_size) -> None:
        self.adj_list = dict()
        self.vert_list = set()
        self.step_size = step_size
        
    def add_vertex(self, vertex: Point):
        if vertex not in self.vert_list:
            self.adj_list[vertex] = []
            self.vert_list.add(vertex)
            
    def add_edge(self, e1:Edge):
        
        if e1 != None:
            self.add_vertex(e1.point1)
            self.add_vertex(e1.point2)
            
            self.adj_list[e1.point1].append(e1.point2)
            self.adj_list[e1.point2].append(e1.point1)
        
    def rm_edge(self, e:Edge):
        self.adj_list[e.point1].remove(e.point2)
        self.adj_list[e.point2].remove(e.point1)
    
    def get_neighbors(self, vertex: Point):
        return self.adj_list[vertex]
                
    def get_all_graph_edges(self) -> list:
        edges = []
        
        for org in self.adj_list.keys():
            for v in self.get_neighbors(org):
                edges.append(Edge(org, v))
        
        return edges
    
    def get_closest_edge(self, point: Point) -> Edge:
        
        min_edge, min_dist = Edge(-1, -1), -1
        
        edges = self.get_all_graph_edges()
        
        for edge in edges:
            discretizations = edge.get_discritized_edge(self.step_size)
            for step in discretizations:
                dist = Edge.get_two_point_euclidean_distance(step, point)
                if dist < min_dist:
                    dist = min_dist
                    min_edge = edge
        
        return min_edge