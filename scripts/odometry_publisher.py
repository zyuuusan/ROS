#!/usr/bin/env python
## Simple talker demo that listens to std_msgs/Strings published
## to the 'chatter' topic

import rospy
import tf
import roslib
roslib.load_manifest('beginner_tutorials')
import math
from math import sin, cos, pi
from beginner_tutorials.msg import Num, carOdom
from geometry_msgs.msg import Twist, Point, Pose, Quaternion, Vector3
from nav_msgs.msg import Odometry

def callback(data):

    rospy.loginfo('Received a /Car_Odom message')

    print 'Car Odom: ', data

    odom_pub = rospy.Publisher("Odom", Odometry, queue_size=50)
    odom_broadcaster = tf.TransformBroadcaster()

    x = 0.0
    y = 0.0
    th = 0.0

    vx = data.vx
    vy = data.vy
    vth = data.vth

    current_time = rospy.Time.now()
    last_time = rospy.Time.now()

    r = rospy.Rate(1.0)
    while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        dt = (current_time - last_time).to_sec()
        delta_x = (vx * cos(th) - vy * sin(th)) * dt
        delta_y = (vx * sin(th) + vy * cos(th)) * dt
        delta_th = vth * dt

        x += delta_x
        y += delta_y
        th += delta_th

        odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)

        odom_broadcaster.sendTransform(
        (x, y, 0.),
        odom_quat,
        current_time,
        "base_link",
        "odom"
        )

        odom = Odometry()
        odom.header.stamp = current_time
        odom.header.frame_id = "odom"

        odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))

        odom.child_frame_id = "base_link"
        odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

        odom_pub.publish(odom)

        last_time = current_time
        r.sleep


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rospy.Subscriber('Car_Odom', carOdom, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    rospy.init_node('Odometry_publisher')
    listener()
