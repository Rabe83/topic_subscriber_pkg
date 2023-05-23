#! /usr/bin/env python3

import rospy
from turtlesim.msg import Pose


def callback(msg):
    print("Robot's Position \nx:",msg.x," \ny:",msg.y, "\ntheta:",msg.theta)
    


# def listener():
rospy.init_node('pose_subscriber_node', anonymous=True)
rate = rospy.Rate(0.1)
msg = Pose()


while not rospy.is_shutdown():
    sub_PoseSubscriber = rospy.Subscriber('/turtle1/pose', Pose, callback)
    rate.sleep()
