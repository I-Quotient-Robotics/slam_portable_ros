#!/usr/bin/env python

import sys

import cv2
from cv_bridge import CvBridge, CvBridgeError

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image


def main():
    rospy.init_node('camera_node')

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    rospy.loginfo(cap.get(cv2.CAP_PROP_FPS))
    rospy.loginfo(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    rospy.loginfo(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    image_pub = rospy.Publisher("image", Image, queue_size=100)

    bridge = CvBridge()

    rate = rospy.Rate(50)
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        try:
            image_pub.publish(bridge.cv2_to_imgmsg(frame, 'bgr8'))
        except CvBridgeError as e:
            rospy.logwarn(e)
        rate.sleep()


if __name__ == '__main__':
    main()