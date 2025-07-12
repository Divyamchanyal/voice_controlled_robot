#!/usr/bin/env python3

import rospy
import speech_recognition as sr
from std_msgs.msg import String
import sys

def shutdown_callback(msg):
    if msg.data == 'shutdown':
        print("Shutdown command recieved. Terminating")
        rospy.signal_shutdown("shutdown")
        sys.exit(0)

def listen_and_publish():
    rospy.init_node('voice_listener_node', anonymous=True)
    pub = rospy.Publisher('/voice_cmd', String, queue_size=10)
    shutdown_sub = rospy.Subscriber('/shutdown_signal', String, shutdown_callback)
    rate = rospy.Rate(0.2)  

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    rospy.loginfo("Robot is listening. Say something...")

    while not rospy.is_shutdown():
        try:
            with mic as source:
                rospy.loginfo("Listening...")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
                
        except rospy.ROSInterruptException:
            break
        except Exception as e:
            rospy.logwarn(f"Listener error: {e}")
            continue

        try:
            command = recognizer.recognize_google(audio).lower()
            rospy.loginfo(f"Recognized: {command}")
            pub.publish(command)
        except sr.UnknownValueError:
            rospy.logwarn("Audio is not clear due to some noise.")
        except sr.RequestError as e:
            rospy.logerr(f"Request failed; {e}")
        
        rate.sleep()

if __name__ == '__main__':
    try:
        listen_and_publish()
    except rospy.ROSInterruptException:
        pass