#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import pyttsx3
import re
import os
import signal
import sys

# Initialize TTS engine once
engine = pyttsx3.init()

shutdown_pub = None

def speak(text):
    rospy.loginfo(f"Robot says: {text}")
    engine.say(text)
    engine.runAndWait()

def callback(data):
    global shutdown_pub
    command = data.data.lower()
    twist = Twist()

    # Movement commands
    if re.search(r'\b(forward|ahead|go forward|move forward)\b', command):
        twist.linear.x = 0.5
        speak("Moving forward")
    elif re.search(r'\b(back|backward|reverse|go back)\b', command):
        twist.linear.x = -0.5
        speak("Moving backward")
    elif re.search(r'\b(left|turn left|rotate left)\b', command):
        twist.angular.z = 1.0
        speak("Turning left")
    elif re.search(r'\b(right|turn right|rotate right)\b', command):
        twist.angular.z = -1.0
        speak("Turning right")
    elif re.search(r'\b(stop|halt|pause)\b', command):
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        speak("Stopping")

    # Exit command
    elif re.search(r'\b(exit|close the program|shut down everything|terminate)\b', command):
        speak("Shutting down the robot now. Goodbye!")
        os.system("rosnode kill /turtlesim")
        shutdown_pub.publish("shutdown")
        rospy.signal_shutdown("Voice command: exit")
        sys.exit(0)

    else:
        speak("Sorry, I did not understand")

    pub.publish(twist)

def listener():
    global pub
    global shutdown_pub
    rospy.init_node('command_controller_node', anonymous=True)
    rospy.Subscriber('/voice_cmd', String, callback)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    shutdown_pub = rospy.Publisher('/shutdown_signal', String, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
