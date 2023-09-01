This folder contains the code to control the Franka Emika gripper. 
To control it, the code uses the actionlib library and creates the SimpleActionClient. 
And by entering the gripper width and speed can be controlled.
To launch this Python code, franka_gripper launch file should be launched. 
To launch the gripper source your catkin_ws, which contains franka_ros package. Then type in the terminal roslaunch franka_gripper franka_gripper.launch robot_ip:=172.17.0.2.
After this you can go to the folder conatining your gripper_control.py file and launch it.
