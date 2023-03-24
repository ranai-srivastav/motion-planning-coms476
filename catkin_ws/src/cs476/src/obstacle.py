from shapely import Polygon
import shapely.affinity
from shapely.geometry import Point
from .world import World

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
        

class CircularObstacle:
    """Creates the 2 circular obstacles for HW4
    """
    def __call__(self, dt, world: World):
        self.radius = (world.get_width() - dt) / 2.0
        
        bot_circle = Point(0, world.get_y_max()).buffer(self.radius)
        top_circle = Point(0, world.get_y_min()).buffer(self.radius)
        
        return bot_circle, top_circle
        
        
        