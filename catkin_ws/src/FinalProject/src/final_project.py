#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist, Point, Quaternion
import tf
from math import radians, copysign, sqrt, pow, pi, atan2, degrees
from tf.transformations import euler_from_quaternion
import numpy as np

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
        rospy.init_node('turtlebot3_pointop_key', anonymous=False)
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
        
        print(f"----------------  In code  --------------------")
        print(f"----------------  {self.getkey()}  --------------------")
        (goal_x, goal_y, goal_z) = self.getkey()
        print(f"----------------  self.getkey() successful  --------------------")
        if goal_z > 180 or goal_z < -180:
            print("you input wrong z range.")
            print("------------------------------ -180 < z < 180 -------------------------------")
            self.shutdown()
        goal_z = np.deg2rad(goal_z)
        goal_distance = sqrt(pow(goal_x - position.x, 2) + pow(goal_y - position.y, 2))
        distance = goal_distance
        
        print(f"----------------  Caculated Goal sitance as {goal_distance}  --------------------")

        while distance > 0.2:
            print(f"----------------  Distance > 0.5  --------------------")
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

        print(f"----------------  Rotation {rotation}  --------------------")
        while abs(rotation - goal_z) > 0.05:
            print(f"----------------  Rotation > 0.05 rads  --------------------")
            (position, rotation) = self.get_odom()
            if goal_z >= 0:
                if rotation <= goal_z and rotation >= goal_z - pi:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = 0.5
                else:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = -0.5
            else:
                if rotation <= goal_z + pi and rotation > goal_z:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = -0.5
                else:
                    move_cmd.linear.x = 0.00
                    move_cmd.angular.z = 0.5
            self.cmd_vel.publish(move_cmd)
            r.sleep()

        print(f"----------------  Publishing move_cmd x = {move_cmd.linear.x}  --------------------")

        rospy.loginfo("Stopping the robot...")
        self.cmd_vel.publish(Twist())
        
    def getkey(self):
        print(f"{self.goal_point}")
        x = self.goal_point[0]
        y = self.goal_point[1]
        z = self.goal_point[2]
        
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
    print("\n\n********************* In main ***************************")
    try:
        path_to_follow = \
            [
                (-500,    0,    0), 
                (-371.40971236, -275.84055741,    4.13464134), 
                (-291.06389892, -134.29255887,    5.70539163), 
                (-462.97616933, -416.28981647,    4.13464134), 
                (-481.31227173, -449.62849058,    4.90845239), 
                (-479.72336398, -453.37598614,   -0.96482681), 
                (-169.85338278, -756.70378733,    5.50887295), 
                ( -59.77561858, -864.36761163,    5.50887295), 
                ( 2.85702956e+02, -6.74095686e+02,  5.21898587e-01), 
                ( 4.51886279e+02, -5.78555888e+02,  4.49964944e-01), 
                (500.        ,   0.        ,   1.57079633)
            ]
            
        i = 0
        while not rospy.is_shutdown() and i < len(path_to_follow):
            print(f"MOVING TO POINT NUM {i} = {path_to_follow[i]}")
            GotoPoint(path_to_follow[i])
            i += 1
        print("\n\n********************* Program ****** Over ***************************")
        print(f"is_shutdown() == {rospy.is_shutdown}")
        print(f"i = {i}")

    except Exception as e:
        rospy.loginfo("shutdown program.")
        rospy.logerr(e)