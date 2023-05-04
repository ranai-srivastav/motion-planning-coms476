#!/usr/bin/env python3

import rospy
from std_msgs.msg import Bool

class can_i_ros():
    def __init__(self) -> None:
        pub = rospy.Publisher("publisher", Bool, queue_size=1)
        
        while not rospy.is_shutdown():
            pub.publish(False)
    


def main(args=None):
    rospy.init_node('can_i_ros')
    node = can_i_ros()
    rospy.spin()
    
    


if __name__ == '__main__':
    main()
