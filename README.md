# 🤖 Code-Easy Robotics Lesson 2: Smart Line Following with Obstacle Detection

---

## 📝 Lesson Overview

- **Duration:** 60 minutes  
- **Age Group:** 7–16 years  
- **Topic:** Line following with ultrasonic sensor obstacle detection and avoidance  
- **Equipment:** Pico Pi robots, ultrasonic sensors, black tape lines, small obstacles  

---
## 🎯 Learning Objectives

By the end of this lesson, students will be able to:

- Understand how ultrasonic sensors measure distance  
- Program a robot to follow a line **and** detect obstacles  
- Implement basic decision-making in robotics code  
- Combine multiple sensors for smarter robot behavior  

---

## 🧩 Lesson Structure

### 1. Live Warm-Up Activity (15 minutes)

#### "Human Ultrasonic Challenge" (10 minutes)

**Setup:** Create a simple obstacle course with chairs/boxes around the room.

**Activity:**

- Students work in pairs – one is the "robot", the other is the "programmer"  
- The "robot" closes their eyes and navigates using only sound cues  
- The "programmer" uses clicking sounds (like echolocation) to guide them  
- Switch roles after 3 minutes  

#### Discussion Questions (5 minutes)

- "How did you know when something was close without seeing it?"  
- "What happened when you heard the clicks echo back quickly?"  
- "How is this similar to how bats or dolphins navigate?"  

**💬 Connection to Lesson:**  
> "Today we're teaching our robots to 'see' with sound, just like you did!"

---

### 2. Main Teaching Content (35 minutes)

#### Part A: Understanding Ultrasonic Sensors (8 minutes)

**Demonstration:**

- Show the ultrasonic sensor on the robot  
- Explain: *"It sends out sound waves we can't hear and measures how long they take to bounce back"*  
- Live demo: Move your hand closer/further from sensor while showing distance readings  

**Key Concepts:**

- *Ultrasonic = sound waves above human hearing*  
- *Closer objects = shorter time = smaller distance reading*  
- *Further objects = longer time = larger distance reading*  

---

#### Part B: Basic Line Following Review (7 minutes)

**Quick Recap:**

- *"Who remembers what we learned about line following last week?"*  
- Demonstrate: Robot following a simple straight line  
- Review: Light sensors detect **dark line** vs. **light floor**  
---
# Tasks: Line-Following Robot with Advanced Obstacle Handling

This project enhances a basic line-following robot with **obstacle detection**, **avoidance**, and **path reversal** capabilities. Built as an extension of Lesson 1's line follower, it demonstrates adaptive robotics using sensors and logic.

## Features

### 1. Obstacle Detection & Auto-Stop  
- **Behavior:** Stops immediately when an obstacle is detected on its path.  
- **Use Case:** Prevents collisions during line-following tasks.  

### 2. Dynamic Obstacle Avoidance  
- **Behavior:** Detects obstacles, navigates around them, and resumes line tracking.  
- **Use Case:** Maintains mission continuity in cluttered environments.  

### 3. Line Detection & Reverse Navigation  
- **Behavior:** Recognizes dead-ends/intersections and reverses direction autonomously.  
- **Use Case:** Enables closed-loop circuits without manual intervention.  

---
