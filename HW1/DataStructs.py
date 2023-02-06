from abc import abstractmethod, ABC
from queue import Queue, LifoQueue, PriorityQueue
from hw1 import StateSpace


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


class QueueAStar(AbstractQueue):
    def __init__(self):
        self.pq = PriorityQueue()

    def pop(self):
        return self.pq.get()

    def insert(self, x):
        # TODO insert
        x = StateSpace()
        pass

    def is_empty(self):
        return self.pq.empty()

