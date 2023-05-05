#! /root/miniconda3/envs/cs476/bin/python3

import sys, math, argparse
import numpy as np
import matplotlib.pyplot as plt

from RRTandPRM.planning import (
    rrt,
    prm,
    EdgeCreator,
    DistanceComputator,
    ObstacleCollisionChecker, StraightEdgeCreator,
)
from dubins import shortest_path
from RRTandPRM.edge import Edge
from RRTandPRM.obstacle import construct_circular_obstacles, WorldBoundary2D
from RRTandPRM.draw_cspace import draw

import rospy
from std_msgs.msg import Bool

from FinalProject.msg import Path, Point

ALG_RRT = "rrt"
ALG_PRM = "prm"


class DubinsEdgeCreator(EdgeCreator):
    def __init__(self, rho_min, step_size):
        self.rho_min = rho_min
        self.step_size = step_size

    def make_edge(self, s1, s2):
        return EdgeDubins(s1, s2, self.rho_min, self.step_size)


class DubinsDistanceComputator(DistanceComputator):
    def __init__(self, rho_min):
        self.rho_min = rho_min

    def get_distance(self, s1, s2):
        """Return the Euclidean distance between s1 and s2"""
        path = shortest_path(s1, s2, self.rho_min)
        return path.path_length()


class EdgeDubins(Edge):
    """Store the information about an edge representing a Dubins curve between 2 points"""

    def __init__(self, s1, s2, rho_min, step_size=0.5, length=None, states=None):
        super().__init__(s1, s2, step_size)

        # The shortest dubins curve and the discretized points along the path
        self.rho_min = rho_min
        if length is None or states is None:
            self._update_path()
        else:
            self.length = length
            self.states = states

    def _update_path(self):
        path = shortest_path(self.s1, self.s2, self.rho_min)
        self.length = path.path_length()

        # Change the step_size to make equal spacing between consecutive states
        # First, compute the number of states (excluding the first one) so that the new step_size
        # is not larger than teh given step_size
        num_states = math.ceil(self.length / self.step_size)
        self.step_size = self.length / num_states

        (self.states, _) = path.sample_many(self.step_size)
        self.states = [np.array(state) for state in self.states]

        # Make sure the last state s2 is also in self.states (possibly missing due to
        # numerical error
        if len(self.states) < num_states + 1:
            self.states.append(self.s2)
        assert len(self.states) == num_states + 1

    def get_path(self):
        """Return the path, representing the geometry of the edge"""
        return self.states

    def reverse(self):
        """Reverse the origin/destination of the edge"""
        super().reverse()
        self._update_path()

    def get_discretized_state(self, i):
        """Return the i^{th} discretized state"""
        if i >= len(self.states):
            return None
        return self.states[i]

    def get_nearest_point(self, state):
        """Compute the nearest point on this edge to the given state

        @return (s, t) where s is the point on the edge that is closest to state
        and it is at distance t*length from the beginning of the edge
        """
        nearest_dist = math.inf
        nearest_ind = None
        for ind, s in enumerate(self.states):
            path = shortest_path(s, state, self.rho_min)
            dist = path.path_length()
            if dist < nearest_dist:
                nearest_dist = dist
                nearest_ind = ind

        if nearest_ind == 0:
            return (self.s1, 0)

        if nearest_ind == len(self.states) - 1:
            return (self.s2, 1)

        t = nearest_ind * self.step_size / self.length
        assert t > 0 and t < 1
        return (self.states[nearest_ind], t)

    def split(self, t):
        """Split the edge at distance t/length where length is the length of this edge

        @return (edge1, edge2) edge1 and edge2 are the result of splitting the original edge
        """
        split_length = t * self.length
        split_ind = round(split_length / self.step_size)
        assert split_ind > 0 and split_ind < len(self.states) - 1

        s = self.states[split_ind]
        edge1 = EdgeDubins(
            self.s1,
            s,
            self.rho_min,
            self.step_size,
            length=split_length,
            states=self.states[0 : split_ind + 1],
        )
        edge2 = EdgeDubins(
            s,
            self.s2,
            self.rho_min,
            self.step_size,
            length=self.length - split_length,
            states=self.states[split_ind:],
        )

        return (edge1, edge2)

    def get_length(self):
        """Return the length of the edge"""
        return self.length


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="Run sampling-based motion planning algorithm"
    )
    parser.add_argument(
        "--alg",
        choices=[ALG_RRT, ALG_PRM],
        required=False,
        default=ALG_RRT,
        dest="alg",
        help="algorithm, default to rrt",
    )
    args = parser.parse_args(sys.argv[1:])
    return args


def findPathLength(G, path):
    # # a dictionary whose key = id of the vertex and value = state of the vertex
    # self.vertices = {}

    # a dictionary whose key = (v1, v2) and value = (cost, edge).
    # v1 is the id of the origin vertex and v2 is the id of the destination vertex.
    # cost is the cost of the edge.
    # edge is of type Edge and stores information about the edge, e.g.,
    # the origin and destination states and the discretized points along the edge
    # self.edges = {}

    totalLength = 0

    for i in range(len(path) - 1):

        # find the first vertex
        firstVertexId = path[i]
        firstVertex = G.vertices.get(firstVertexId)

        # find the second vertex
        secondVertexId = path[i + 1]
        secondVertex = G.vertices.get(secondVertexId)

        # Put the vertices in key format
        key = (firstVertexId, secondVertexId)

        # find the edge associated with those
        edge = G.edges.get(key)

        # find the length of that edge
        length = edge[0]

        totalLength = totalLength + length


    return totalLength

def arg_parse(argv):
    retval = {}
    
    for i, arg in enumerate(argv[:-1]):
        if arg.lower() == "--alg":
            if argv[i+1].lower() == "rrt":
                retval["alg"] = ALG_RRT
                return retval
            elif argv[i+1].lower() == "prm":
                retval["alg"] = ALG_PRM
                return retval
            
    print("No algorithm specified. Correct usage `python3 hw5.py --alg [RRT/PRM]`")
    sys.exit()
    


if __name__ == "__main__":
    
    rospy.init_node("path_node", log_level=rospy.DEBUG)
    
    # TODO: Change min turning radius
    # rho_min = 0.5
    rho_min = 10

    cspace = [(-1000, 1000), (-1000, 1000), (-math.pi / 2, math.pi / 2)]
    qI = (-500, 0, 0)
    qG = (500, 0, math.pi / 2)

    # TODO: Edit how our obstacles are created.
    # Might have to pass them in as arguments
    # We will only have circular obstacles for now
    # obstacles = construct_circular_obstacles(0.2)
    obstacles = construct_circular_obstacles(95)

    obs_boundaries = [obstacle.get_boundaries() for obstacle in obstacles]
    world_boundary = WorldBoundary2D(cspace[0], cspace[1])
    obstacles.append(world_boundary)
    # edge_creator = DubinsEdgeCreator(rho_min, 0.1)
    edge_creator = StraightEdgeCreator(0.1)
    collision_checker = ObstacleCollisionChecker(obstacles)
    distance_computator = DubinsDistanceComputator(rho_min)

    # Our robot W = 178 and L = 138
    
    try:
        
        path_is_gen = Bool()
        path_is_gen.data = False
        
        # validity_publisher = rospy.Publisher("is_published", Bool, queue_size=1)
        path_publisher = rospy.Publisher("coms476_finalproject_path", Path, queue_size=1)
        
        # validity_publisher.publish(path_is_gen)
        
        rate = rospy.Rate(10)
        
        args = rospy.get_param("CS476_finalproject_pathnode/alg")
        if args.lower() == "rrt":
            alg = ALG_RRT
        elif args.lower() == "prm":
            alg = ALG_PRM
        
        # args = arg_parse(sys.argv)

        if alg == ALG_RRT:
            title = "RRT planning"
            rospy.loginfo("Running RRT")
            print("INSIDE RRT")
            (G, root, goal, count, stoppingConfigTime) = rrt(
                cspace=cspace,
                qI=qI,
                qG=qG,
                edge_creator=edge_creator,
                distance_computator=distance_computator,
                collision_checker=collision_checker,
            )
            print("DONE WITH  RRT")
        elif alg == ALG_PRM:
            title = "PRM planning"
            rospy.loginfo("Running PRM")
            print("INSIDE PRM")
            (G, root, goal) = prm(
                cspace=cspace,
                qI=qI,
                qG=qG,
                edge_creator=edge_creator,
                distance_computator=distance_computator,
                collision_checker=collision_checker,
                k=15,
            )
            print("DONE WITH  PRM")
        else:
            print("[!!ERR!!] - Invalid input")
            
        path = []
        print("BUILDING PATH")
        if root is not None and goal is not None:
            
            # validity_publisher.publish(path_is_gen)
            path = G.getVertexIdsAlongPath(root, goal)
            pathLength = findPathLength(G, path)
            
            # validity_publisher.publish(path_is_gen)
            path_to_publish = []
            
            for pid in path:
                x, y, theta = G.vertices.get(pid)
            
                point = Point()
                point.x = x
                point.y = y
                point.theta = theta
                
                path_to_publish.append(point)
                print("[PATH]: ---- Added a point")
            
            print(path_to_publish)
                
            
            # print("[PATH]: ---- We are drawing the graph")
            # fig, ax = plt.subplots(1, 1)
            # draw(ax, cspace, obs_boundaries, qI, qG, G, path, title)
            # plt.show()
            # validity_publisher.publish(path_is_gen)
            pub_this = Path()
            pub_this.path = path_to_publish
            
            print("[PATH]: ---- About to publish")
            # print(f"Is rospy shutdown?: {rospy.is_shutdown()}")
            while not rospy.is_shutdown():
                path_publisher.publish(pub_this)
                rospy.spin()
                rate.sleep()
                # path_is_gen.data = True
                # validity_publisher.publish(path_is_gen)
                # print("In the loop")
                # rospy.loginfo("sent path value")
            
            # This gets a very discretized path
            # This is what I want to send to ROS
            # path = G.get_path(root, goal)
        else:
            rospy.logerr("Could not Find a path")
            raise rospy.ROSException("Could not Find a path")
                
    except Exception as e:
        rospy.logerr('ERROR IN PATH TRANSFER NODE: ')
        rospy.logerr(e)
    
    rospy.loginfo("-------- Code terminated --------")
                   





