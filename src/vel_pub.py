#!/usr/bin/env python
#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def talker():
    pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)
    rospy.init_node('mock_cmd', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    vel_msg = Twist()
    vel_msg.linear.x = 0.1
    vel_msg.linear.y = -0.1
    vel_msg.angular.z = 0.1
    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass