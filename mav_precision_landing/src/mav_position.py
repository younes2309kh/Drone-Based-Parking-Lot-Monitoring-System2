#!/usr/bin/env python3
import rospy
from rospy.topics import Publisher
from geometry_msgs.msg import PoseStamped
import time


if __name__ == '__main__':
    rospy.init_node('Hover', anonymous=False)
    pub = rospy.Publisher('/firefly/command/pose', PoseStamped, queue_size=5)
    dPoint = PoseStamped()
    rate = rospy.Rate(1)
    button = False
    time.sleep(10.5)
    while not rospy.is_shutdown():
        time.sleep(5.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 4
        dPoint.pose.position.y = -9
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = -7.75
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = -6.4
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = -4.8
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()

        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = -3.3
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()       

        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = -2
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()       
            
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = 0
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()       
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = 2.3
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()       
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = 3.9
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()       
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = 5.2
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()       
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = 6.7
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()       
      
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 0
        dPoint.pose.position.y = 8.3
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()       
       
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = 8.3
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()       
             
       
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = 6.7
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()        
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = 5.2
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()        
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = 3.9
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()        
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = 2.3
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()         
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = 0
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()           

        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = -2
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()           
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = -3.3
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()   
        pub.publish(dPoint)
        rate.sleep()
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = -4.8
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()       
       
       
        
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = -6.4
        dPoint.pose.position.z = 2       
       
       
        pub.publish(dPoint)
        rate.sleep()
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 7.5
        dPoint.pose.position.y = -7.75
        dPoint.pose.position.z = 2


        pub.publish(dPoint)
        rate.sleep()      
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 4
        dPoint.pose.position.y = -9
        dPoint.pose.position.z = 1


        pub.publish(dPoint)
        rate.sleep()

        time.sleep(20.5)
        dPoint.header.stamp = rospy.Time.now()
        dPoint.header.frame_id = "world"
        dPoint.pose.orientation.z = 0.0
        dPoint.pose.orientation.w = 0.0

        dPoint.pose.position.x = 4
        dPoint.pose.position.y = -9
        dPoint.pose.position.z = 0


        pub.publish(dPoint)
        rate.sleep()
        time.sleep(50.5)




