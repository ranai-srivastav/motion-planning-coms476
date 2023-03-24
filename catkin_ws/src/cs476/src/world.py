class World:
    """A square world
    """
    
    def __init__(self, x_min, x_max, y_min, y_max) -> None:
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
    
    def get_x_min(self):
        return self.x_min
    def get_x_max (self):
        return self.x_max
    def get_y_min(self):
        return self.y_min
    def get_y_max(self):
        return self.y_max