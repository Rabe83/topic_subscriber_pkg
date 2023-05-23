#include <ros/ros.h>
#include <topic_subscriber_pkg/Age.h>

void talk()
{
  ros::NodeHandle nh;
  ros::Publisher pub_AgePublisher = nh.advertise<topic_subscriber_pkg::Age>("/age_chatter", 1);
  ros::Rate rate(0.1);
  ROS_INFO("Publisher Node started, Now Publishing Messages");

  while (ros::ok())
  {
    topic_subscriber_pkg::Age data;
    data.years = 1991;
    data.months = 12;
    data.days = 24;
    pub_AgePublisher.publish(data);
    rate.sleep();
  }
}

int main(int argc, char** argv)
{
  ros::init(argc, argv, "age_node");
  
  try
  {
    talk();
  }
  catch (const ros::Exception& e)
  {
    ROS_ERROR("An exception occurred: %s", e.what());
  }

  return 0;
}
