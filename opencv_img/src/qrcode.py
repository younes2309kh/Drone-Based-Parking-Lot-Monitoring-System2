#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
from pyzbar.pyzbar import decode
import numpy as np

class QRCodeScanner:
    def __init__(self, output_file):
        rospy.init_node('qrcode', anonymous=True)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber('/firefly/vi_sensor/left/image_raw', Image, self.image_callback)
        self.detected_qr_codes = set()  # Keep track of detected QR codes
        self.output_file = output_file
        self.first_qr_code_detected = False  # Flag to indicate if the first QR code is detected
        rospy.spin()

    def image_callback(self, data):
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        except Exception as e:
            print(e)
            return

        # Scan for QR codes
        qr_codes = decode(cv_image)

        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')

            # If the first QR code is detected, refresh the set
            if not self.first_qr_code_detected:
                self.detected_qr_codes = set()
                self.first_qr_code_detected = True

            # Check if the QR code has already been detected and published
            if qr_data not in self.detected_qr_codes:
                qr_rect_points = qr_code.polygon

                # Draw a rectangle around the QR code
                pts = []
                for point in qr_rect_points:
                    pts.append((point.x, point.y))
                pts = np.array(pts, dtype=int)
                cv2.polylines(cv_image, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

                # Print the QR code data
                print("QR Code Data:", qr_data)

                # Save the QR code data to the text file
                self.save_to_text_file(qr_data)

                # Add the QR code to the set of detected codes
                self.detected_qr_codes.add(qr_data)
                if qr_data == "DELETE_CONDITION":  # Replace "DELETE_CONDITION" with the actual condition to delete the QR code
                    self.detected_qr_codes.clear()  # Clear the set	        
        # Display the image with QR codes highlighted
        cv2.imshow('QR Code Scanner', cv_image)
        cv2.waitKey(1)

    def save_to_text_file(self, qr_data):
        with open(self.output_file, 'a') as file:
            file.write(f"{qr_data}\n")

        # Check if the delete condition is met
        if qr_data == "DELETE_CONDITION":
            # If the condition is met, open the file in write mode to clear its content
            with open(self.output_file, 'w') as file:
                pass  # This will clear the file
if __name__ == '__main__':
    try:
        output_file = '/home/younes/flight_ws/src/opencv_img/src/output.txt'
        qr_code_scanner = QRCodeScanner(output_file)
    except rospy.ROSInterruptException:
        pass
