#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist, Point, Quaternion
import tf
from math import radians, copysign, sqrt, pow, pi, atan2, degrees
from tf.transformations import euler_from_quaternion
import numpy as np
from FinalProject.msg import Path, Point
import time

msg = """
control your Turtlebot3!
-----------------------
Insert xyz - coordinate.
x : position x (m)
y : position y (m)
z : orientation z (degree: -180 ~ 180)
If you want to close, insert 's'
-----------------------
"""


class GotoPoint():
    def __init__(self, point):
        # rospy.init_node('turtlebot3_pointop_key', anonymous=False)
        rospy.on_shutdown(self.shutdown)
        self.cmd_vel = rospy.Publisher('cmd_vel', Twist, queue_size=5)
        position = Point()
        move_cmd = Twist()
        r = rospy.Rate(10)
        self.tf_listener = tf.TransformListener()
        self.odom_frame = 'odom'
        self.goal_point = point

        try:
            self.tf_listener.waitForTransform(self.odom_frame, 'base_footprint', rospy.Time(), rospy.Duration(1.0))
            self.base_frame = 'base_footprint'
        except (tf.Exception, tf.ConnectivityException, tf.LookupException):
            try:
                self.tf_listener.waitForTransform(self.odom_frame, 'base_link', rospy.Time(), rospy.Duration(1.0))
                self.base_frame = 'base_link'
            except (tf.Exception, tf.ConnectivityException, tf.LookupException):
                rospy.loginfo("Cannot find transform between odom and base_link or base_footprint")
                rospy.signal_shutdown("tf Exception")

        (position, rotation) = self.get_odom()
        last_rotation = 0
        linear_speed = 1
        angular_speed = 1
        
        (goal_x, goal_y, goal_z) = self.getkey()
        if goal_z > 180 or goal_z < -180:
            self.shutdown()
        goal_z = np.deg2rad(goal_z)
        goal_distance = sqrt(pow(goal_x - position.x, 2) + pow(goal_y - position.y, 2))
        distance = goal_distance
        
        # print(f"[GZBO] ---- ---- ---- Caculated Goal distance is {goal_distance}")
        while distance > 0.1:
            print(f"[GZBO] ---- ---- ---- Distance: {distance} > 0.05")
            (position, rotation) = self.get_odom()
            x_start = position.x
            y_start = position.y
            path_angle = atan2(goal_y - y_start, goal_x- x_start)

            if path_angle < -pi/4 or path_angle > pi/4:
                if goal_y < 0 and y_start < goal_y:
                    path_angle = -2*pi + path_angle
                elif goal_y >= 0 and y_start > goal_y:
                    path_angle = 2*pi + path_angle
            if last_rotation > pi-0.1 and rotation <= 0:
                rotation = 2*pi + rotation
            elif last_rotation < -pi+0.1 and rotation > 0:
                rotation = -2*pi + rotation
            move_cmd.angular.z = angular_speed * path_angle-rotation

            distance = sqrt(pow((goal_x - x_start), 2) + pow((goal_y - y_start), 2))
            move_cmd.linear.x = min(linear_speed * distance, 0.1)

            if move_cmd.angular.z > 0:
                move_cmd.angular.z = min(move_cmd.angular.z, 1.5)
            else:
                move_cmd.angular.z = max(move_cmd.angular.z, -1.5)

            last_rotation = rotation
            self.cmd_vel.publish(move_cmd)
            r.sleep()
        (position, rotation) = self.get_odom()

        while abs(rotation - goal_z) > 0.05:
            print(f"[GZBO] ---- ---- ---- Rotation: {rotation} > 0.05")
            # print(f"----------------  Rotation > 0.05 rads  --------------------")
            (position, rotation) = self.get_odom()
            if goal_z >= 0:
                if rotation <= goal_z and rotation >= goal_z - pi:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = 0.2
                else:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = -0.2
            else:
                if rotation <= goal_z + pi and rotation > goal_z:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = -0.2
                else:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = 0.2
            self.cmd_vel.publish(move_cmd)
            r.sleep()

        # print(f"----------------  Publishing move_cmd x = {move_cmd.linear.x}  --------------------")

        rospy.loginfo(" ***** ***** **** Stopping the robot...")
        self.cmd_vel.publish(Twist())
        
    def getkey(self):
        print(f"{self.goal_point}")
        x = self.goal_point.x
        y = self.goal_point.y
        z = self.goal_point.theta
        
        x, y, z = [float(x), float(y), float(z)]
        
        x = x/1000
        y = y/1000
        z = (degrees(z) % 360)
        if z > 180 and z < 360:
            z = -(360 - z)
        return x, y, z


    def get_odom(self):
        try:
            (trans, rot) = self.tf_listener.lookupTransform(self.odom_frame, self.base_frame, rospy.Time(0))
            rotation = euler_from_quaternion(rot)

        except (tf.Exception, tf.ConnectivityException, tf.LookupException):
            rospy.loginfo("TF Exception")
            return

        return (Point(*trans), rotation[2])


    def shutdown(self):
        self.cmd_vel.publish(Twist())
        rospy.sleep(1)

    


if __name__ == '__main__':
    print("[GZBO] ---- ---- Entering Gazebo Node")
    try:
        rospy.init_node('turtlebot3_pointop_key', anonymous=False)
        msg = rospy.wait_for_message("coms476_finalproject_path", Path)
        time.sleep(3)
        
        print("[GZBO] ---- ---- Received path")
        path_to_follow = msg.path
    
        i = 0
        while not rospy.is_shutdown() and i < len(path_to_follow):
            print(f"[GZBO] ---- ---- MOVING TO POINT NUM {i} = {path_to_follow[i].x} {path_to_follow[i].y} {path_to_follow[i].theta}")
            GotoPoint(path_to_follow[i])
            i += 1
            
        print(f"i = {i}")
        rospy.signal_shutdown("Goal Reached")
    
        # path_sub = rospy.Subscriber("coms476_finalproject_path", Path, queue_size=1, callback=path_recieved)

    except Exception as e:
        rospy.loginfo("shutdown program.")
        rospy.logerr(e)