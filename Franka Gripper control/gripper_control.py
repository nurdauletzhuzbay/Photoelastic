# !/usr/bin/env python

import rospy
from std_msgs.msg import String, Float64, Float32
import franka_gripper.msg
from franka_gripper.msg import MoveGoal, MoveActionGoal
# Brings in the SimpleActionClient
import actionlib

import rosbag
from std_msgs.msg import String, Float64, Float32
from numpy import asarray
import pandas as pd
from wittenstein_msgs.msg import wittenstein
import sys
from time import sleep, time
import csv
import pandas as pd
import numpy as np
import threading


def move_gripper():
    
    # Creates the SimpleActionClient, passing the type of the action
    client = actionlib.SimpleActionClient('/franka_gripper/move', franka_gripper.msg.MoveAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client.wait_for_server()

    # Creates a goal to send to the action server.
    goal = franka_gripper.msg.MoveGoal(width=0.01, speed=1.0)
    
    # Sends the goal to the action server.
    client.send_goal(goal)

    # Waits for the server to finish performing the action.
    client.wait_for_result()

def close_gripper():
    
    # Creates the SimpleActionClient, passing the type of the action
    client2 = actionlib.SimpleActionClient('/franka_gripper/move', franka_gripper.msg.MoveAction)

    # Waits until the action server has started up and started
    # listening for goals.
    client2.wait_for_server()

    # Creates a goal to send to the action server.
    goal = franka_gripper.msg.MoveGoal(width=0.0008, speed=1.0)
    
    # Sends the goal to the action server.
    client2.send_goal(goal)

    # Waits for the server to finish performing the action.
    client2.wait_for_result()

if __name__ == '__main__':


    try:
        rospy.init_node('move_gripper')

        for i in range(5):
            move_gripper()
            sleep(0.5)
            close_gripper()
            sleep(0.5)
            i = i + 1

        move_gripper()


    except rospy.ROSInterruptException:
        print("program interrupted before completion")



