#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def scan_callback(data):
    print(data)

if __name__ == "__main__":
    #initialize node
    rospy.init_node("scan_node", anonymous=True)
    #sub topic /scan_front
    rospy.Subscriber("scan", LaserScan, scan_callback)
    rospy.spin()
