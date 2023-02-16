ALG_BFS = "bfs"
ALG_DFS = "dfs"
ALG_ASTAR = "astar"


class StateSpace:
    """A base class to specify a state space X"""

    def __contains__(self, x):
        """Return whether the given state x is in the state space"""
        raise NotImplementedError

    def get_distance_lower_bound(self, x1, x2):
        """Return the lower bound on the distance between the given states x1 and x2"""
        return 0


class ActionSpace:
    """A base class to specify an action space"""

    def __call__(self, x):
        """ Return the list of all the possible actions at the given state x"""
        raise NotImplementedError


class StateTransition:
    """A base class to specify a state transition function"""

    def __call__(self, x, u):
        """Return the new state obtained by applying action u at state x"""
        raise NotImplementedError


def path_gen(goal_state, parents):
    path = []
    state = goal_state

    while state is not None:
        path.append(state)
        state = parents[state][0]

    path.reverse()
    return path


def fsearch(X, U, f, xI, XG, alg):
    """Return the list of visited nodes and a path from xI to XG based on the given algorithm

    This is the general template for forward search describe in Figure 2.4 in the textbook.

    @type X:   an instance of the StateSpace class (or its derived class) that represent the state space
    @type U:   an instance of the ActionSpace class (or its derived class) such that
               U(x) returns the list of all the possible actions at state x
    @type f:   an instance of the StateTransition class  (or its derived class) such that
               f(x, u) returns the new state obtained by applying action u at cell x
    @type xI:  an initial state such that xI in X
    @type XG:  a list of states that specify the goal set
    @type alg: a string in {"bfs", "dfs", "astar"} that specifies the discrete search algorithm to use

    @return:   a dictionary {"visited": visited_states, "path": path} where visited_states is the list of
               states visited during the search and path is a path from xI to a state in XG
    """
    from DataStructs import QueueBFS, QueueDFS, QueueAStar

    visited = list()
    parents = {xI: (None, 0)}

    if alg == "bfs":
        data_structure = QueueBFS()
    elif alg == "dfs":
        data_structure = QueueDFS()
    else:
        data_structure = QueueAStar(X, XG, xI, parents)

    # inserts it into the appropriate data structure based on the dynamic type
    data_structure.insert(xI)
    visited.append(xI)

    # do only while there are no other nodes to process
    while not data_structure.is_empty():
        curr = data_structure.pop()

        if curr in XG:
            return {"visited": list(visited), "path": path_gen(curr, parents)}

        for neighbor in U(curr):
            if neighbor not in visited:
                visited.append(neighbor)
                parents[neighbor] = (curr, parents[curr][1] + 1)
                data_structure.insert(neighbor)
            else:
                if (neighbor[0] != xI[0] and neighbor[1] != xI[1]) or neighbor != xI:
                    if parents[curr][1] + 1 < parents[neighbor][1]:
                        parents[neighbor] = (curr, parents[neighbor][1] + 1)
                        


    return list(), list()
