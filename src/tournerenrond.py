#!/usr/bin/env python

# script qui fait tourner le robot en cercle
import rospy
from geometry_msgs.msg import Twist
from datetime import datetime
from math import floor

rospy.init_node("joy")
def move_circle():
    # creation du publisher qui peut "parler" a mybot et lui dire de bouger
    pub = rospy.Publisher('mybot/cmd_vel', Twist, queue_size=1)

    # creation du message Twist
    move_cmd = Twist()
    move_cmd.linear.x = 1.2
    move_cmd.angular.z = 1.8

    # memorise heure et publish rate a 10hz
    now = rospy.Time.now()
    debutprocess = datetime.now()
    rate = rospy.Rate(10) 

    # Pour les 6 prochaines secondes publication cmd_vel to mybot
    while not rospy.is_shutdown():
        dureeecoulee = datetime.now() - debutprocess
        print (dureeecoulee.total_seconds(), floor(dureeecoulee.total_seconds() % 5))
	if dureeecoulee.total_seconds() > 1 and (floor(dureeecoulee.total_seconds() % 5)) == 0 :
          move_cmd.linear.x += 0.01
          move_cmd.angular.z += 0.01
        # print (dureeecoulee , move_cmd.linear.x , rospy.Time.now(), now + rospy.Duration.from_sec(6))
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:       
        move_circle()
    except rospy.ROSInterruptException:
        pass
