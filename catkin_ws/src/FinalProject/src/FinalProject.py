#!/usr/bin/env python3

import rospy
from nav_msgs import Odometry

class FinalProject:
    
    def __init__(self) -> None:
        
        #This is the current location of the robot
        curr_pose = rospy.Subscriber("/odom", Odometry, queue_size=1)
            


if __name__ == '__main__':
    rospy.init_node("/476/traj_follower")
    rospy.spin()
        
        
        