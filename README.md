# 🐢 Voice-Controlled Robot using ROS Noetic

This project is a simple yet functional **voice-controlled robot simulation** built using **ROS Noetic**, Python, and speech technologies. It allows control of the `turtlesim_node` in ROS using natural voice commands, with both **speech recognition** and **text-to-speech feedback**.

> ⚙️ This is my first step towards full-stack ROS development. The project is actively being expanded with more features.

---

## 🎯 Features

- 🎤 Voice control via **Google Speech Recognition API**
- 🗣️ Text-to-speech feedback with `pyttsx3`
- 🧠 Flexible keyword-based command matching (e.g., "move forward", "turn left")
- 🧵 ROS Publisher/Subscriber architecture with proper node shutdown
- 🐢 Controls the official ROS `turtlesim_node`
- 🔁 "Exit" voice command shuts down all related ROS nodes and windows
