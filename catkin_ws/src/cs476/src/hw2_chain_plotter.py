#!/usr/bin/env python
import rospy
import matplotlib.pyplot as plt
# from cs476.msg import Chain2D
import numpy
import math

# def get_chain_msg():
#     """Return a message from the "chain_config" channel.
#     This function will wait until a message is received.
#     """
#     rospy.init_node("chain_recv", anonymous=True)
#     recv_msg = rospy.wait_for_message("chain_config", Chain2D)
#     rospy.loginfo(f"Got config as {recv_msg.config} and W={recv_msg.W}, L={recv_msg.L}, D={recv_msg.D}")
#     return recv_msg


def plot_chain(config, W, L, D):
    """Plot a 2D kinematic chain A_1, ..., A_m
    @type config: a list [theta_1, ..., theta_m] where theta_1 represents the angle between A_1 and the x-axis,
        and for each i such that 1 < i <= m, \theta_i represents the angle between A_i and A_{i-1}.
    @type W: float, representing the width of each link
    @type L: float, representing the length of each link
    @type D: float, the distance between the two points of attachment on each link
    """

    (joint_positions, link_vertices) = get_link_positions(config, W, L, D)

    fig, ax = plt.subplots()
    plot_links(link_vertices, ax)
    plot_joints(joint_positions, ax)
    ax.axis("equal")
    plt.show()


def plot_links(link_vertices, ax):
    """Plot the links of a 2D kinematic chain A_1, ..., A_m on the axis ax
    @type link_vertices: a list [V_1, ..., V_m] where V_i is the list of [x,y] positions of vertices of A_i
    """

    for vertices in link_vertices:
        x = [vertex[0] for vertex in vertices]
        y = [vertex[1] for vertex in vertices]

        x.append(vertices[0][0])
        y.append(vertices[0][1])
        ax.plot(x, y, "k-", linewidth=2)


def plot_joints(joint_positions, ax):
    """Plot the joints of a 2D kinematic chain A_1, ..., A_m on the axis ax
    @type joint_positions: a list [p_1, ..., p_{m+1}] where p_i is the position [x,y] of the joint between A_i and A_{i-1}
    """
    x = [pos[0] for pos in joint_positions]
    y = [pos[1] for pos in joint_positions]
    ax.plot(x, y, "k.", markersize=10)
    

def get_homogenous_rotn_mat(theta, x_t, y_t):
    mat = numpy.array([[math.cos(theta), -(math.sin(theta)), x_t], [math.sin(theta), math.cos(theta), y_t], [0, 0, 1]])
    
    return mat
    
    
def get_transformation_matrix(config, D, link_index):
    
    if link_index == 0:
        ret_val = get_homogenous_rotn_mat(config[link_index], 0, 0)
        return ret_val
    
    mat_left = get_transformation_matrix(config, D, (link_index - 1))
    mat_right = get_homogenous_rotn_mat(config[link_index], D, 0)
    
    return numpy.dot(mat_left, mat_right)
    

def get_vertices(config, W, L, D):
    """
    W = the width of a link
    L = total length of each link
    D = the distance between the joints
    p = poistion of a join represented as a single tuple
    v = is a list of 4 vertices, each a tuple is one vertex of 
    
      |-----base right----|
     _____________________A   
    | .                 . |
    |_____________________|B
    |-| <---- base left == joint_to_edge
    
    
    """
    v_ret = []
    joint_to_edge = (L-D)/2.0
    
    base_right = D + joint_to_edge
    v_top_right = (base_right,  W/2.0)
    v_bot_right = (base_right, -W/2.0)
    
    base_left = joint_to_edge
    v_top_left = (-base_left,   W/2.0)
    v_bot_left = (-base_left,  -W/2.0)
    
    for i in range(len(config)):
        v = []
        
        coord =  numpy.array([v_bot_left[0], v_bot_left[1], 1]).reshape(-1, 1)
        trans_coord = numpy.dot(get_transformation_matrix(config, D, i), coord)
        v.append( (trans_coord[0], trans_coord[1]) )
        
        coord =  numpy.array([v_bot_right[0], v_bot_right[1], 1]).reshape(-1, 1)
        trans_coord = numpy.dot(get_transformation_matrix(config, D, i), coord)
        v.append( (trans_coord[0], trans_coord[1]) )
        
        coord =  numpy.array([v_top_right[0], v_top_right[1], 1]).reshape(-1, 1)
        trans_coord = numpy.dot(get_transformation_matrix(config, D, i), coord)
        v.append( (trans_coord[0], trans_coord[1]) )
        
        coord =  numpy.array([v_top_left[0], v_top_left[1], 1]).reshape(-1, 1)
        trans_coord = numpy.dot(get_transformation_matrix(config, D, i), coord)
        v.append( (trans_coord[0], trans_coord[1]) )

        v_ret.append(v)
    
    return v_ret
    
def get_joints(config, D):
    links = []
    num_links = len(config)
    config = list(config)
    # config.reverse()
    
    for i, theta in enumerate(config):
        coord =  numpy.array([D, 0, 1]).reshape(-1, 1)
        links.append(numpy.dot(get_transformation_matrix(config, D, i), coord))
    
        
    return links
    

def get_link_positions(config, W, L, D):
    """Compute the positions of the links and the joints of a 2D kinematic chain A_1, ..., A_m
    @type config: a list [theta_1, ..., theta_m] where theta_1 represents the angle between A_1 and the x-axis,
        and for each i such that 1 < i <= m, \theta_i represents the angle between A_i and A_{i-1}.
    @type W: float, representing the width of each link
    @type L: float, representing the length of each link
    @type D: float, the distance between the two points of attachment on each link
    @return: a tuple (joint_positions, link_vertices) where
        * joint_positions is a list [p_1, ..., p_{m+1}] where p_i is the position [x,y] of the joint between A_i and A_{i-1}
        * link_vertices is a list [V_1, ..., V_m] where V_i is the list of [x,y] positions of vertices of A_i
    """
    """
    # p = poistion of a join represented as a single tuple
    # v = is a list of 4 vertices, each a tuple is one vertex of 
    
   D _____________________A
    |                     |
   C|_____________________|B
    
    """
    
    joint_list = get_joints(config, D)
    
    vert_list = get_vertices(config, W, L, D)
    
    return joint_list, vert_list
    
        
        

if __name__ == "__main__":
    chain = get_chain_msg()
    plot_chain(chain.config, chain.W, chain.L, chain.D)