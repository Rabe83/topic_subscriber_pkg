#! /usr/bin/env python3

import rospy
from topic_subscriber_pkg.msg import Age

def talk():
    rospy.init_node('age_node', anonymous=True)
    pub_AgePublisher = rospy.Publisher('/age_chatter', Age, queue_size=1)
    rate = rospy.Rate(0.1)
    rospy.loginfo("Publisher Node started, Now Publishing Messages")
    
    while not rospy.is_shutdown():
         data = Age()
         data.years=1991
         data.months=12
         data.days=24
         pub_AgePublisher.publish(data)
         rate.sleep()

if __name__ == '__main__':
    try:
        talk()
    except rospy.ROSInternalException:
        pass
