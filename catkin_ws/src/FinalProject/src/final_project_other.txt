#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2

class FinalProject:
    
    x = 0.0
    y = 0.0
    theta = 0.0
    
    def __init__(self) -> None:
        
        #This is the current location of the robot
        self.curr_pose_sub = rospy.Subscriber("/odom", Odometry, self.callback)
        self.robot_speed_pub = rospy.Publisher()
            
    def callback(self, msg:Odometry):
        
        global curr_x
        global curr_y
        global curr_theta
        
        curr_x = msg.pose.pose.position.x
        curr_y = msg.pose.pose.position.y
        
        rot_quat = msg.pose.pose.orientation
        _, _, curr_theta = euler_from_quaternion([rot_quat.x, rot_quat.y, rot_quat.z, rot_quat.w])
        
    def go_to_point(self, goal_point):
        goal = Point()
        goal.x = goal_point[0]
        goal.y = goal_point[1]
        
        speed = Twist()
        
        dx = goal.x - curr_x
        dy = goal.y - curr_y
        
        angle_to_goal = atan2(dy, dx)
        
        if(abs(angle_to_goal - curr_theta) > 0.1):
            speed.linear.x = 0.0
            speed.angular = 0.3
        else:
            speed.linear.x = 0.5
            speed.angular = 0.0
            
        pub.publish()
        


if __name__ == '__main__':
    print("\n\n\n---------------------------------------------Running Final project File-------------------------------\n\n\n")
    rospy.init_node("traj_follower_node")
    
    node = FinalProject()
    rospy.spin()
    
    path_to_follow = [(0.25, 0.25, 0)]
    
    while not rospy.is_shutdown():
        node.go_to_point(path_to_follow[0])
        
        