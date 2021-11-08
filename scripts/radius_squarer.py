#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64


def callback(data):
    radius = data.data
    squared_radius = radius * radius
    rospy.loginfo("radius: %f, squared_radius: %f", radius, squared_radius)
    pub.publish(squared_radius)


rospy.init_node("radius_squarer")
pub = rospy.Publisher("/radius_squared", Float64, queue_size=10)
rospy.Subscriber("/radius", Float64, callback)
rospy.spin()

