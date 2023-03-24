from shapely import Polygon
import shapely.affinity
from shapely.geometry import Point

class Obstacles:
    """Class that stores a list of Obstacles as Shapely Polygons
    
    Class contains methods to add to the list of Obstacles 
    """
    def __init__(self) -> None:
        self.list_of_obstacles = []
        
    def get_obstacles(self):
        return self.list_of_obstacles
    
    def add_to_obstacle_list(self, obs: Polygon):
        self.list_of_obstacles.append(obs)
        

class CircularObstacle():
    """Creates the 2 circular obstacles for HW4
    """
    def __init__(self, dt, world) -> None:
        self.radius = (width_of_map - dt) / 2.0
        
        