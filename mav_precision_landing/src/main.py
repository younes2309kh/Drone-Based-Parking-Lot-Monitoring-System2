#!/usr/bin/env python3
from inspect import Traceback
import cv2
import numpy as np
import rospy
from marker_pose_estimator import MarkerPose
from rospy.core import is_shutdown
from sensor_msgs.msg import Image
from geometry_msgs.msg import Point
from geometry_msgs.msg import PoseStamped
import time
from land_mav import MakeTrajectory

GO_TO_POINT = True

if __name__ == '__main__':
    rospy.init_node('markerDetector', anonymous=False)
    pub = rospy.Publisher('/firefly/command/pose', PoseStamped, queue_size=5)

    raw_image_topic = "/firefly/vi_sensor/left/image_raw"
    disparity_topic = "/mav_precision_landing/vi_stereo/disparity" 

    if GO_TO_POINT == True:
        point_msg = PoseStamped()

        point_msg.header.stamp = rospy.Time.now()
        point_msg.header.frame_id = "world"
        point_msg.pose.orientation.z = 0.0
        point_msg.pose.orientation.w = 0.0

        point_msg.pose.position.x = 3
        point_msg.pose.position.y = 3
        point_msg.pose.position.z = 5

        time.sleep(2)

    test = MarkerPose(raw_image_topic=raw_image_topic, disparity_topic=disparity_topic)
    test.loop()
