from abc import abstractmethod, ABC
from queue import Queue, LifoQueue, PriorityQueue
from hw1 import Grid2DStates


class AbstractQueue(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def insert(self, x):
        pass

    def is_empty(self):
        pass


class QueueBFS(AbstractQueue):
    def __init__(self):
        self.q = Queue()

    def pop(self):
        return self.q.get()

    def insert(self, x):
        self.q.put(x)

    def is_empty(self):
        self.q.empty()


class QueueDFS(AbstractQueue):
    def __init__(self):
        self.stack = LifoQueue()

    def pop(self):
        return self.stack.get()

    def insert(self, x):
        self.stack.put(x)

    def is_empty(self):
        return self.stack.empty()


class QueueAStar:
    def __init__(self, X, XG, xI, parents):
        self.pq = PriorityQueue()
        self.goals = XG
        self.state_space = X
        self.init_state = xI
        self.C = {self.init_state: 0}
        self.visited = []
        self.parents = parents

    def pop(self):
        return self.pq.get()[1]

    def insert(self, x):
        """
        x is what is to be inserted
        x should look like tuple(priority, <data>)
        """
        # Calculating Cost-to-Come using C(x') = C(x) + 1
        parent = self.parents[x]
        cost_to_come = parent[1] + 1

        # Calculating Cost-to-Go
        min_goal_dist = 99
        min_goal = tuple()
        for goal in self.goals:
            curr_dist = self.state_space.get_distance_lower_bound(x1=x, x2=goal)
            if curr_dist < min_goal_dist:
                min_goal_dist = curr_dist
                min_goal = goal

        self.pq.put(((min_goal_dist + cost_to_come), x))

    def is_empty(self):
        return self.pq.empty()
