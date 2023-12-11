#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import pyqrcode
from PIL import Image

class TxtToQRCodeROS:
    def __init__(self, file_path):
        rospy.init_node('user_guide', anonymous=True)
        self.file_path = file_path
        self.publisher = rospy.Publisher('/qr_code', String, queue_size=10)

    def read_data_from_text_file(self):
        try:
            with open(self.file_path, 'r') as file:
                data = file.read().strip()
            return data
        except Exception as e:
            rospy.logerr("Error reading from text file: %s", str(e))
            return None

    def generate_qr_code(self, data):
        try:
            qr = pyqrcode.create(data)
            qr.png("/home/younes/flight_ws/src/opencv_img/src/qr_code.png", scale=10)  # Save PNG image

            # Display the QR code image
            img = Image.open("/home/younes/flight_ws/src/opencv_img/src/qr_code.png")
            img.show()

            # Publish the data to the '/qr_code' topic
            self.publisher.publish(data)

        except Exception as e:
            rospy.logerr("Error generating QR code: %s", str(e))

    def run(self):
        rate = rospy.Rate(10)  # 1 Hz
        while not rospy.is_shutdown():
            data = self.read_data_from_text_file()
            if data is not None:
                rospy.loginfo("Read data from text file: %s", data)
                self.generate_qr_code(data)
            rate.sleep()

if __name__ == '__main__':
    file_path = '/home/younes/flight_ws/src/opencv_img/src/output.txt'
    txt_to_qr_node = TxtToQRCodeROS(file_path)
    txt_to_qr_node.run()

