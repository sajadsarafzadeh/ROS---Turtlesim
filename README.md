# ROS Turtlesim Name Drawing

## Overview
This project demonstrates how to use the ROS turtlesim simulator to draw a name using multiple turtles.  
A Python node is used to control turtle motion through linear and angular velocity commands, while the ROS `/spawn` service is used to create additional turtles for drawing different letters.

The final output is the name **SJD**, written inside the turtlesim environment.

## Features
- Motion control using `geometry_msgs/Twist`
- Custom forward motion and rotation functions
- Multi-turtle drawing using the `/spawn` service
- Automated execution using a ROS launch file
- Simple path generation for writing letters in simulation

## Project Structure
- `scripts/demo_turtle_move.py`  
  Main Python node for controlling turtle movements and drawing the letters
- `launch/drawing.launch`  
  Launch file for running turtlesim and the drawing node together
- `package.xml`  
  ROS package configuration and dependencies
- `docs/report.pdf`  
  Project report and screenshots

## Technologies Used
- ROS
- Python
- turtlesim
- rospy
- geometry_msgs
- ROS services and publishers

## How It Works
The project defines two main motion functions:
- `move_forward()` for linear movement
- `rotate()` for angular motion

The `/spawn` service is used to create extra turtles, and each turtle is assigned to draw a specific letter.  
By combining forward motion and rotation with different parameters, the turtles trace the shapes of the letters **S**, **J**, and **D**.

## How to Run
1. Start ROS:
   ```bash
   roscore
