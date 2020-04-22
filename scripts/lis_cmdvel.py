#!/usr/bin/env python
## Simple talker demo that listens to std_msgs/Strings published
## to the 'chatter' topic

import rospy
import roslib
roslib.load_manifest('beginner_tutorials')
import math
from beginner_tutorials.msg import Num
from geometry_msgs.msg import Twist

def callback(data):
    rospy.loginfo('Received a /cmd_vel message')

    rotation = data.angular.z
    vx = data.linear.x
    vy = data.linear.y

    radius = 0.1188
    wheel1 = radius*rotation - vx
    wheel2 = vx/2-math.sqrt(3)*vy/2+radius*rotation
    wheel3 = vx/2+math.sqrt(3)*vy/2+radius*rotation

    print rotation, vx, vy
    print wheel1, wheel2, wheel3
    msg = Num()
    pub = rospy.Publisher('CmdWheel', Num, queue_size=10)
    #rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg.w1 = wheel1
        msg.w2 = wheel2
        msg.w3 = wheel3
        pub.publish(msg)
        rate.sleep()

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('lis_cmd', anonymous=True)

    rospy.Subscriber('cmd_vel', Twist, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
