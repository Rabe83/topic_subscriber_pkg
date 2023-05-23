#!/usr/bin/env python3

import rospy
import calendar
from topic_subscriber_pkg.msg import Age
from datetime import datetime
from std_msgs.msg import Float32

rospy.init_node('subscriber_publisher_node', anonymous=True)

def callback(data):
    rospy.loginfo("Received data:\n%s", data)
    calculated_age = calculate_age(data)
    publish_age(calculated_age)

def listen():
    rospy.init_node('subscriber_publisher_node', anonymous=True)
    rospy.Subscriber('/age_chatter', Age, callback)
    rospy.spin()

def calculate_age(birthdata):
    current_date = datetime.now()

    # Calculate the difference in years
    age_of_robot_year = current_date.year - birthdata.years

    # Calculate the difference in months
    age_of_robot_month = current_date.month - birthdata.months
    if age_of_robot_month < 0:  # Adjust for negative month difference
        age_of_robot_year -= 1
        age_of_robot_month += 12

    # Calculate the difference in days
    age_of_robot_day = current_date.day - birthdata.days
    if age_of_robot_day < 0:  # Adjust for negative day difference
        # Get the number of days in the previous month
        _, prev_month_days = calendar.monthrange(current_date.year, current_date.month - 1)
        age_of_robot_month -= 1
        age_of_robot_day += prev_month_days

    print("Age of the robot:")
    print("Years:", age_of_robot_year)
    print("Months:", age_of_robot_month)
    print("Days:", age_of_robot_day)

    # Calculate the age in a format compatible with Float32 message
    calculated_age = age_of_robot_year + age_of_robot_month / 12 + age_of_robot_day / 365

    return calculated_age



def publish_age(calculated_age):
    pub = rospy.Publisher('/calculated_robot_age_topic', Float32, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz (adjust the publishing rate as needed)
    

    while not rospy.is_shutdown():
        message = Float32()
        message.data = calculated_age
        pub.publish(message)
        # print(message)
        rate.sleep()

if __name__ == '__main__':
    try:
        listen()
    except rospy.ROSInterruptException:
        pass
