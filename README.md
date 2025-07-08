# Code-Easy Lesson 3: Line Avoidance & Object Tracking Robot

<div align="center">

![Code-Easy Logo](https://img.shields.io/badge/Code--Easy-Robotics%20Lesson%203-blue?style=for-the-badge)
![Age Group](https://img.shields.io/badge/Ages-7--16-green?style=flat-square)
![Duration](https://img.shields.io/badge/Duration-60%20minutes-orange?style=flat-square)
![Week](https://img.shields.io/badge/Term%20Week-3-purple?style=flat-square)

</div>

> **🤖 Advanced Robotics:** Students program robots to avoid boundaries and track objects using multiple sensors simultaneously.

## 🎯 Learning Objectives

By the end of this lesson, students will be able to:
- ✅ Program a robot to detect and avoid black lines using sensors
- ✅ Implement ultrasonic sensor object detection and tracking
- ✅ Combine multiple sensors for complex robot behaviors
- ✅ Understand basic conditional logic in robotics programming

## 📦 Materials Needed

| Item | Quantity | Purpose |
|------|----------|---------|
| Pico Pi robots | 1 per student | Pre-assembled from previous lessons |
| Black electrical tape | 1 roll | Creating boundaries |
| Various objects | 5-10 items | Tracking targets (blocks, balls, etc.) |
| Laptops/tablets | 1 per student | Programming environment |
| Measuring tape | 1 | Setup assistance |
| Code-Easy stickers | 20+ | Project completion rewards |

## 🚀 WARM-UP ACTIVITY (15 minutes)

### "Human Robot Challenge"
**🎯 Setup:** Create a large black tape square/circle on the floor (3m x 3m)

#### 🔄 Activity 1: Line Avoidance (7 minutes)
- Students work in pairs - one is the "robot," one is the "programmer"
- Programmer gives verbal commands: `"forward"`, `"turn left"`, `"turn right"`, `"stop"`
- Robot must stay inside the black boundary
- When robot reaches the black line, they must immediately turn away
- 🔄 Switch roles after 3 minutes

#### 🎯 Activity 2: Object Hunt (8 minutes)
- Place a colorful object inside the taped area
- "Robot" student closes eyes, "programmer" guides them toward the object
- Use distance clues: "getting warmer/colder" or "3 steps forward, 2 steps left"
- 🎉 Celebrate when object is found!

#### 💭 Debrief Questions:
- "What was challenging about avoiding the boundary?"
- "How did you know when you were close to the object?"
- "How is this similar to what we'll program our robots to do?"

## 📚 MAIN LESSON CONTENT

### 🔍 Phase 1: Understanding Sensors (10 minutes)

#### Quick Sensor Review
| Sensor | Function | Real-World Example |
|--------|----------|-------------------|
| **Line/Color Sensor** | "Eyes" that detect light/dark surfaces | Lane-keeping in cars |
| **Ultrasonic Sensor** | "Ears" that measure distance using sound waves | Parking sensors |

> 💡 **Key Concept:** Sensors send information to the robot's "brain" (Pico Pi)

#### 🎬 Demonstration
Set up the black tape boundary and demonstrate:
1. ➡️ Robot moving forward until it hits the black line
2. 👁️ Sensor detecting the line and robot turning away
3. 📏 Ultrasonic sensor detecting objects at different distances

### 💻 Phase 2: Programming Line Avoidance (15 minutes)

#### Code Structure Introduction
```pseudocode
REPEAT FOREVER:
  IF line sensor detects BLACK:
    Turn right
    Move forward 1 second
  ELSE:
    Move forward
```

#### 🖥️ Hands-On Programming (10 minutes)
- Students open their programming environment
- Guide them through creating the line avoidance program
- **👶 Younger students (7-10):** Use visual block programming
- **🧑 Older students (11-16):** Introduce text-based coding concepts

#### 🧪 Testing Phase (5 minutes)
- Place robots inside the black tape boundary
- Students test their programs and adjust as needed

> **🔧 Troubleshooting Tips:**
> - If robot doesn't turn: Check sensor connection
> - If robot turns too much: Adjust turn duration
> - If robot moves too fast: Reduce speed setting

### 🎯 Phase 3: Adding Ultrasonic Object Tracking (15 minutes)

#### Enhanced Program Logic
```pseudocode
REPEAT FOREVER:
  IF line sensor detects BLACK:
    Turn right
    Move forward 1 second
  ELSE IF ultrasonic sensor detects object CLOSE:
    Move toward object
  ELSE:
    Move forward and search
```

#### 📋 Implementation Steps (10 minutes)
1. Add ultrasonic sensor code to existing program
2. Set distance threshold (e.g., object within 20cm = "close")
3. Program robot to move toward detected objects
4. Test object tracking behavior

#### ✅ Challenge Testing (5 minutes)
- Place objects inside the boundary
- Students test combined line avoidance + object tracking
- **🏆 Success criteria:** Robot stays within boundary AND approaches objects

### 🎮 Phase 4: Challenge Missions (10 minutes)

#### Mission Options (Students choose based on skill level):

| Mission | Difficulty | Description | Success Criteria |
|---------|------------|-------------|------------------|
| **🛡️ Boundary Guard** | Beginner | Robot patrols the boundary without crossing | Longest time without crossing |
| **💎 Treasure Hunter** | Intermediate | Find and approach 3 different objects | Complete in under 2 minutes |
| **🗺️ Smart Explorer** | Advanced | Map area by following boundaries + investigate objects | Return to patrol after investigation |

## 🎉 WRAP-UP & REFLECTION (5 minutes)

### 📸 Project Showcase
- Each student demonstrates their robot's behavior
- Quick 30-second explanation of their programming approach
- Award Code-Easy stickers for:
  - 🎨 Most creative solution
  - 🤝 Best teamwork
  - 🔧 Most persistent debugging

### 💭 Reflection Questions
- "What real-world robots use similar sensors?"
- "How could you improve your robot's behavior?"
- "What was the trickiest part of combining both sensors?"


## 🎯 DIFFERENTIATION STRATEGIES

<details>
<summary><strong>👶 For Younger Students (7-10)</strong></summary>

- Use larger visual programming blocks
- Provide printed code templates
- Pair with older students for support
- Focus on one sensor at a time before combining

</details>

<details>
<summary><strong>🧑 For Older Students (11-16)</strong></summary>

- Introduce variables for sensor thresholds
- Challenge them to optimize turning angles
- Encourage experimentation with different movement patterns
- Introduce basic debugging techniques

</details>

<details>
<summary><strong>🚀 For Advanced Students</strong></summary>

- Add multiple objects with different response behaviors
- Implement sensor data logging
- Create custom movement patterns (spiral search, etc.)
- Research real-world applications of similar robotics

</details>

## 📚 EXTENSION ACTIVITIES

### 🏠 Take-Home Challenge
- Students sketch their ideal robot arena design
- Research one real robot that uses similar sensors
- Plan improvements for next week's lesson

## ✅ ASSESSMENT CHECKLIST

### Technical Skills
- [ ] Successfully implemented line detection
- [ ] Robot avoids crossing black boundary
- [ ] Ultrasonic sensor responds to objects
- [ ] Combined both sensors effectively

### Problem-Solving
- [ ] Debugged issues independently
- [ ] Adapted code when first attempt didn't work
- [ ] Helped classmates troubleshoot

### Understanding
- [ ] Explained how sensors work
- [ ] Identified real-world applications
- [ ] Made connections to previous lessons

## 🧑‍🏫 INSTRUCTOR NOTES

### ⏰ Pre-Lesson Setup (10 minutes before class)
- [ ] Create black tape boundaries on floor
- [ ] Test all robots and sensors
- [ ] Prepare various objects for tracking
- [ ] Set up demonstration area

### 🛠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Sensor not responding | Check cable connections |
| Robot spinning in circles | Adjust turn duration in code |
| Inconsistent line detection | Ensure good contrast with floor |
| Ultrasonic false readings | Keep area clear of obstacles |

### ⚠️ Safety Reminders
- Students walk carefully around tape boundaries
- No running when collecting robots
- Handle sensors gently

---

<div align="center">

**📞 Contact Code-Easy**  
WhatsApp Business | Email | [Website]

</div>
