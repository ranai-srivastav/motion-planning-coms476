from shapely import Polygon, LineString
import numpy
from functools import total_ordering

class Point:
    def __init__(self, x1, y1, parent = None) -> None:
        self.x = x1
        self.y = y1
        self.parent = parent
        
    # @total_ordering
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Point ) and \
            __value.x == self.x and \
            __value.y == self.y
    
    # @total_ordering
    # def __lt__(self, __value: object) -> bool:
    #     if not isinstance(__value, Point):
    #         return False
    #     else:
    #         if __value.x < self.x and __value.y < self.y:
    #             return False
            
    #     return True
    
    def __str__(self) -> str:
        return f"x:{self.x} y:{self.y}"



class Edge:
    def __init__(self, point1, point2) -> None:
        self.point1 = point1
        self.point2 = point2
        
    def __eq__(self, __value: object) -> bool:
        return isinstance(__value, Edge) and \
            (
                (__value.point1 == self.point1 and __value.point2 == self.point2) or \
                (__value.point1 == self.point2 and __value.point2 == self.point1)
            )
    
    def get_euclidean_distance(self):
        return ( (self.point1.x - self.point2.x) ** 2 + (self.point1.y - self.point2.y) ** 2)
    
    @staticmethod
    def get_two_point_euclidean_distance(point1: Point, point2: Point):
        return ( (point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

    def get_nearest_point(self, p: Point):
        vp_1 = numpy.array([p.x - self.point1.x, p.y - self.point1.y])
        v2_1 = numpy.array([self.point2.x - self.point1.x, self.point2.y - self.point1.y])
        
        t_dash = (vp_1 @ v2_1) / (self.get_euclidean_distance())
        t_dash = max(0, min(t_dash, 1))
        
        if t_dash == 0:
            return self.point1
        elif t_dash == 1:
            return self.point2
        else:
            return t_dash * v2_1
        
        
    def reverse(self):
        return Edge(self.point2, self.point1)
    
    
    def is_inside_obstacle(obstacle: Polygon):
        obstacle.contains(obstacle)
        
        
    def get_discritized_edge(self, step_size):
        point1 = Point(self.point1.x, self.point1.y)
        point2 = Point(self.point2.x, self.point2.y)
        line = LineString([point1, point2])
        length = line.length
        num_segments = int(length / step_size) + 1

        list_of_points = [line.interpolate(i * step_size) for i in range(num_segments)]
        
        return [Point(point.x, point.y) for point in list_of_points]
    
    # @staticmethod
    # def split_edge(edge:'Edge', point:Point):
        
    #     closet_point_on_edge = edge.get_nearest_point(point)
        
    #     edge1 = Edge(edge.point1, closet_point_on_edge)
    #     edge2 = Edge(closet_point_on_edge, edge.point2)
        
    #     return (edge1, edge2)