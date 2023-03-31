class World:
    """A square world and all other user defined variables are initalized here

    The classs contains getters for all members
    """
    
    def __init__(self, x_min, x_max, y_min, y_max, dt, step_size, xG, xI) -> None:
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        self.dt = dt
        self.step_size = step_size
        
        self.init_state = xI
        self.goal_state = xG
        
        self.length = x_max - x_min
        self.width = y_max - y_min
    
    def get_x_min(self):
        return self.x_min
    
    def get_x_max (self):
        return self.x_max
    
    def get_y_min(self):
        return self.y_min
    
    def get_y_max(self):
        return self.y_max
    
    def get_length(self):
        return self.length
    
    def get_width(self):
        return self.width
    
    def get_init_state(self):
        return self.init_state
    
    def get_goal_state(self):
        return self.goal_state

    def get_step_size(self):
        return self.step_size
