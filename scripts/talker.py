#!/usr/bin/env python

import roslib
roslib.load_manifest('beginner_tutorials')
import rospy
from beginner_tutorials.msg import carOdom

def talker():
    pub = rospy.Publisher('Car_Odom', carOdom, queue_size=10)
    rospy.init_node('testtalker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    count = 0.0
    while not rospy.is_shutdown():
        msg = carOdom()
        msg.vx = count
        msg.vy = -count
        msg.vth = count + 0.1
        rospy.loginfo(msg)
        pub.publish(msg)
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
