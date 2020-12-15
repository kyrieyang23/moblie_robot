#!/usr/bin/env python
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from math import radians, degrees
from actionlib_msgs.msg import *
from geometry_msgs.msg import Point

def move_to_goal(x,y):
    
    ac = actionlib.SimpleActionClient('move_base', MoveBaseAction)

    while(not ac.wait_for_server(rospy.Duration.from_sec(5.0))):
        rospy.loginfo('Waiting for move_base sever')

    goal = MoveBaseGoal()

    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.header.stamp = rospy.Time.now()

    goal.target_pose.pose.position = Point(x,y,0.0)
    goal.target_pose.pose.orientation.x = 0.0
    goal.target_pose.pose.orientation.y = 0.0
    goal.target_pose.pose.orientation.z = 0.0
    goal.target_pose.pose.orientation.w = 1.0

    rospy.loginfo('sending location...')
    ac.send_goal(goal)

    ac.wait_for_result(rospy.Duration(60))

    if(ac.get_state() == GoalStatus.SUCCEEDED):
        rospy.loginfo("I'm here now motherfucker!!")
        return True
    else:
        rospy.loginfo("I can't go to that destination you son of a bitch!!")
        return False


if __name__ == '__main__':
    rospy.init_node('map_nav', anonymous=False)
    x_goal = float(input("X:"))
    y_goal = float(input("Y:"))
    print("Start going")
    move_to_goal(x_goal,y_goal)