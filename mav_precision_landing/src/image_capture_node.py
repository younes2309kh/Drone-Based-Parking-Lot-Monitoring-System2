#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import time

i=1
class ImageCapture:
    def __init__(self):
        rospy.init_node("image_capture_node")
        self.bridge = CvBridge()

        # Define the image topic you want to subscribe to
        self.image_topic = "/firefly/vi_sensor/left/image_raw"  # Replace with your actual camera topic

        # Subscribe to the camera image topic
        rospy.Subscriber(self.image_topic, Image, self.image_callback)

    def image_callback(self, data):
        try:
            # Convert ROS Image message to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")

            current_time = rospy.Time.now()
            time_elapsed = current_time - self.last_capture_time

            # Capture an image every 17 seconds
            if time_elapsed.to_sec() >= 17.0:
                # Save the image as a file
                image_filename = "/home/younes/flight_ws/src/mav_precision_landing/img/qrcode",i,".jpg".format(current_time.to_sec())
                cv2.imwrite(image_filename, cv_image)
		 i+=1
                rospy.loginfo("Image saved as %s", image_filename)

                # Update the last capture time
                self.last_capture_time = current_time

        except Exception as e:
            rospy.logerr("Error processing image: %s", str(e))

    def run(self):
        # Sleep for 25 seconds before starting image captures
        rospy.sleep(25)
        self.last_capture_time = rospy.Time.now()

        while not rospy.is_shutdown():
            rospy.sleep(1.0)

if __name__ == '__main__':
    try:
        image_capture = ImageCapture()
        image_capture.run()
    except rospy.ROSInterruptException:
        pass
