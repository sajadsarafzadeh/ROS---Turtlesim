#!/usr/bin/python3



import rospy
import math
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn 




def move_forward(distance,coord,direction, ang):
    vel_msg = Twist()
    linear_vel = 1
    rate = rospy.Rate(20)

    if direction == 0:
        linear_vel = linear_vel
    else:
        linear_vel = -linear_vel

    
   

    
    if coord == 1:
        vel_msg.linear.x = linear_vel
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = ang
        current_distance = 0
    elif coord == 2:
        vel_msg.linear.x = 0
        vel_msg.linear.y = linear_vel
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = ang
        current_distance = 0
    t0 = rospy.Time().now().to_sec()

    while abs(current_distance) <= distance :
        pub.publish(vel_msg)
        t1 = rospy.Time().now().to_sec()-t0
        current_distance = linear_vel * t1
        rate.sleep()


def rotate(angle,direction):
    vel_msg = Twist()
    angular_vel = 0.4
    if direction == 0 :
        angular_vel = angular_vel
    if direction == 1 :
        angular_vel = -angular_vel
    rate = rospy.Rate(20)
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angular_vel
    current_rotation = 0
    t0 = rospy.Time().now().to_sec()

    while abs(current_rotation) <= angle :
        pub.publish(vel_msg)
        t1 = rospy.Time().now().to_sec()-t0
        current_rotation = angular_vel * t1
        rate.sleep()


if __name__ =="__main__":
    
    rospy.init_node('turtle_move')


    rospy.wait_for_service('/spawn')
    add_turtle =rospy.ServiceProxy('/spawn',Spawn)
    response = add_turtle(4,5,0,"turtle2")
    response = add_turtle(8.2,5.6,0,"turtle3")
    

    
   


   

    #s
    pub = rospy.Publisher('/turtle2/cmd_vel',Twist,queue_size=10)
    desired_rotation=math.radians(93)
    rotate(desired_rotation,0)

    move_forward(4,1,0, 1.2)
    move_forward(3,1,0, -1.2)

    #j
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    move_forward(1,1,0,0)
    desired_rotation=math.radians(92)
    rotate(desired_rotation,1)

    
    move_forward(2,1,0, 0)
    move_forward(2.5,1,0, -1)
    

    #d
    pub = rospy.Publisher('/turtle3/cmd_vel',Twist,queue_size=10)
    desired_distance = 3.8
    desired_rotation=math.radians(100)
    rotate(desired_rotation,1)
    move_forward(2.2,1,0, 0)
    move_forward(desired_distance,1,0, -1.3)

    
    