#!/usr/bin/env python

import cv2
import numpy as np
import threading
import time
import pandas as pd
import rospy
from std_msgs.msg import String, Float64, Float32, Int32, Float32MultiArray

pub = rospy.Publisher('intensity_photo', Float32, queue_size=10)
pub2 = rospy.Publisher('non_zero', Float32, queue_size=10)

rospy.init_node('photoelastic_pub')
r = rospy.Rate(10)

my_msg = Float32MultiArray() 
while not rospy.is_shutdown():
    # Creating a VideoCapture object to read the video
    

    cap = cv2.VideoCapture(0)

    int_g = []
    non_z_b = []

    # Loop until the end of the video
    while (cap.isOpened()):
        # Capture frame-by-frame
        ret, frame = cap.read()



        # Display the resulting frame
        cv2.imshow('Frame', frame)
        #first is row, second is column
        #instances of image with leds
        led11 = frame[140:190, 160:210]
        led12 = frame[150:200, 310:360]
        led13 = frame[155:205, 450:500]

        led21 = frame[285:335, 165:220]
        led22 = frame[285:335, 310:360]
        led23 = frame[275:325, 455:505]

        led31 = frame[410:470, 165:215]
        led32 = frame[420:480, 300:350]
        led33 = frame[420:480, 440:490]
        
        led_arr = [led11, led12, led13, led21, led22, led23, led31, led32, led33]
        # cv2.imwrite('max_force.jpg', frame)

        # conversion of BGR to grayscale is necessary to apply this operation
        gray1 = cv2.cvtColor(led11, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(led12, cv2.COLOR_BGR2GRAY)
        gray3 = cv2.cvtColor(led13, cv2.COLOR_BGR2GRAY)
        gray4 = cv2.cvtColor(led21, cv2.COLOR_BGR2GRAY)
        gray5 = cv2.cvtColor(led22, cv2.COLOR_BGR2GRAY)
        gray6 = cv2.cvtColor(led23, cv2.COLOR_BGR2GRAY)
        gray7 = cv2.cvtColor(led31, cv2.COLOR_BGR2GRAY)
        gray8 = cv2.cvtColor(led32, cv2.COLOR_BGR2GRAY)
        gray9 = cv2.cvtColor(led33, cv2.COLOR_BGR2GRAY)
        gray_arr = [gray1, gray2, gray3, gray4, gray5, gray6, gray7, gray8, gray9]
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        # cv2.imshow('Gray1', gray1)
        # cv2.imshow('Gray2', gray2)
        # cv2.imshow('Gray3', gray3)
        # cv2.imshow('Gray4', gray4)
        # cv2.imshow('Gray5', gray5)
        # cv2.imshow('Gray6', gray6)
        # cv2.imshow('Gray7', gray7)
        # cv2.imshow('Gray8', gray8)
        # cv2.imshow('Gray9', gray9)

        cv2.imshow('Gray', gray)

        gray_int_arr = []
        # M = cv2.moments(gray)
        # x = M.get("m00")
        # gray_int = x/(gray.shape[0]*gray.shape[1])

        for i in range(9):
            M = cv2.moments(gray_arr[i])
            x = M.get("m00")

            gray_int = x/(gray_arr[i].shape[0]*gray_arr[i].shape[1])  #Intensity calculation for grayscale
            gray_int_arr.append(gray_int)
            my_msg.data = gray_int_arr

        gray_int = np.sum(gray_int_arr)/9 
        
        if gray_int <7:
            # force = -8.017*pow(gray_int, 2) + 107.7*gray_int - 357.5
            force = 3.63*gray_int-23.2
        elif gray_int >=7:
            force = -0.00169*pow(gray_int, 4) + 0.0881*pow(gray_int, 3) - 1.69*pow(gray_int, 2) + 14.6*gray_int - 41.5


        int_g.append(gray_int)
        non_z_b.append(force)

        format_gray_int = "{:.2f}".format(gray_int)
        format_force = "{:.2f}".format(force)

        print('Intensity: ' + format_gray_int + '   |   force: ' + format_force + 'N')

        #publish into two topics

        pub.publish(gray_int)
        pub2.publish(force)
        

        
        # define q as the exit button
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    
    # release the video capture object
    cap.release()

    # Closes all the windows currently opened.
    cv2.destroyAllWindows()
