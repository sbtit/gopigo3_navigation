#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
import rospy
import cv2
import sys
import message_filters
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
 
class image_bridge:
    def __init__(self):
        rospy.init_node('image_view', anonymous=True)
        self.bridge = CvBridge()
        sub_right = message_filters.Subscriber("right/image_raw",Image)
        sub_left = message_filters.Subscriber("left/image_raw",Image)
        self.mf = message_filters.ApproximateTimeSynchronizer([sub_right, sub_left], 100, 10.0)
        self.mf.registerCallback(self.ImageCallback)
 
    def ImageCallback(self, right_data , left_data):
        try:
            right_image = self.bridge.imgmsg_to_cv2(right_data, 'passthrough')
            left_image = self.bridge.imgmsg_to_cv2(left_data, 'passthrough')
        except CvBridgeError, e:
            rospy.logerr(e)
 
        right_image.flags.writeable = True
        left_image.flags.writeable = True
 
        cv2.namedWindow("right_image")
        cv2.namedWindow("left_image")
        cv2.imshow("right_image", right_image)
        cv2.imshow("left_image", left_image)
        #print(right_image)
	#print(left_image)
        cv2.waitKey(10)
 
if __name__ == '__main__':
    try:
        ib = image_bridge()
        rospy.spin()
    except rospy.ROSInterruptException: pass
