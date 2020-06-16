#!/usr/bin/env python

import rospy
import tf
import roslib
roslib.load_manifest('beginner_tutorials')
import math
from math import sin, cos, pi
from beginner_tutorials.msg import Num, carOdom
from geometry_msgs.msg import Twist, Point, Pose, Quaternion, Vector3, Vector3Stamped
from nav_msgs.msg import Odometry
started = False

odom_pub = rospy.Publisher("odom", Odometry, queue_size=50)
odom_broadcaster = tf.TransformBroadcaster()
def callback(data):
    global started, last_data
    rospy.loginfo('Received a /Car_Odom message')
    print 'Car Odom: ', data
    last_data = data
    if not started:
        started = True

def timer_callback(event):
    global odom_pub, odom_broadcaster
    if started:
        x = 0.0
        y = 0.0
        th = 0.0

        #vx = last_data.vx
        #vy = last_data.vy
        #vth = last_data.vth

        vx = last_data.vector.x
        vy = last_data.vector.y
        vth = last_data.vector.z

        current_time = rospy.Time.now()
        last_time = rospy.Time.now()

        #r = rospy.Rate(1.0)
        #while not rospy.is_shutdown():
        current_time = rospy.Time.now()

        dt = (current_time - last_time).to_sec()
        delta_x = (vx * cos(th) - vy * sin(th)) * dt
        delta_y = (vx * sin(th) + vy * cos(th)) * dt
        delta_th = vth * dt

        x += delta_x
        y += delta_y
        th += delta_th

        ### camera_link or base_link
        ### original official code use base_link
        ### some gmapping tutorial says camera_link
        odom_quat = tf.transformations.quaternion_from_euler(0, 0, th)
        odom_broadcaster.sendTransform(
            (x, y, 0.),
            odom_quat,
            current_time,
            "base_link",
            #"camera_link"
            "odom"
        )

        odom = Odometry()
        odom.header.stamp = current_time
        odom.header.frame_id = "odom"

        #odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*odom_quat))
        odom.pose.pose.position = Point(x, y, 0.)
        odom.pose.pose.orientation = Quaternion(*odom_quat)
        odom.child_frame_id = "base_link"
        odom.twist.twist = Twist(Vector3(vx, vy, 0), Vector3(0, 0, vth))

        odom_pub.publish(odom)

        last_time = current_time
            #r.sleep

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

### rpm is the topic published by arduino including wheel speeds
    rospy.init_node('Odometry_publisher')
    rospy.Subscriber('rpm', Vector3Stamped, callback)

    timer = rospy.Timer(rospy.Duration(1), timer_callback)
    rospy.spin()
    timer.shutdown()

if __name__ == '__main__':
    started = False
    listener()
