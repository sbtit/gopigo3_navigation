#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from turtlesim.msg import Pose

def callback(msg):
    print(msg.pose.pose)
    #print(msg.pose.pose.position.x)
    #print(msg.pose.pose.position.y)
    #print(msg.pose.pose.orientation.z)

rospy.init_node('odometry')
odom_sub = rospy.Subscriber('/odom', Odometry, callback)
rospy.spin()
