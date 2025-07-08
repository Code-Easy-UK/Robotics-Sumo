# Code-Easy Lesson 4: Robot Sumo Wrestling Championship

<div align="center">

![Code-Easy Logo](https://img.shields.io/badge/Code--Easy-Robotics%20Lesson%204-blue?style=for-the-badge)
![Age Group](https://img.shields.io/badge/Ages-7--16-green?style=flat-square)
![Duration](https://img.shields.io/badge/Duration-60%20minutes-orange?style=flat-square)
![Week](https://img.shields.io/badge/Term%20Week-4-purple?style=flat-square)
![Competition](https://img.shields.io/badge/SUMO-WRESTLING-red?style=flat-square)

</div>

> **🥋 Ultimate Robot Challenge:** Students program strategic sumo wrestling robots that hunt, attack, defend, and avoid boundaries in head-to-head combat!

## 🎯 Learning Objectives

By the end of this lesson, students will be able to:
- ✅ Program strategic robot behaviors for competitive scenarios
- ✅ Implement multi-sensor coordination for complex decision-making
- ✅ Design and test different combat strategies (aggressive, defensive, tactical)
- ✅ Apply conditional logic for dynamic robot responses
- ✅ Understand real-world applications of competitive robotics

## 📦 Materials Needed

| Item | Quantity | Purpose |
|------|----------|---------|
| Pico Pi robots | 1 per student | Battle-ready sumo bots |
| Black electrical tape | 2 rolls | Sumo ring boundaries (multiple rings) |
| Measuring tape | 1 | Creating regulation sumo rings |
| Stopwatch/Timer | 1 | Match timing |
| Code-Easy championship stickers | 30+ | Tournament rewards |
| Whiteboard/markers | 1 set | Strategy planning |
| Small weights (optional) | Various | Robot customization |

## 🚀 WARM-UP ACTIVITY (15 minutes)

### "Human Sumo Strategy Workshop"
**🎯 Setup:** Create 2-3 black tape circles on the floor (2m diameter each)

#### 🥋 Activity 1: Human Sumo Rules (5 minutes)
- Demonstrate basic sumo rules:
  - Stay inside the ring (black boundary)
  - Push opponent out to win
  - No grabbing, only pushing
  - Match ends when someone touches/crosses the line

#### 🧠 Activity 2: Strategy Discussion (5 minutes)
Students brainstorm different sumo strategies:
- **🏃 Search for opponent:** Find opponent quickly and attack
- **🛡️ Defender:** Stay in center, wait for opponent to approach
- **🌪️ Spinner:** Circle around the ring, attack from sides
- **⚡ Dasher:** Quick forward attacks, then retreat

#### 🎮 Activity 3: Human Demo Matches (5 minutes)
- Quick 30-second human sumo matches
- Students test different strategies
- Observe what works and what doesn't

#### 💭 Strategy Questions:
- "Which strategy seemed most effective?"
- "How would you program a robot to do this?"
- "What sensors would help your robot win?"

## 📚 MAIN LESSON CONTENT

### 🧠 Phase 1: Sumo Strategy Programming (15 minutes)

#### Core Sumo Behaviors
| Behavior | Description | Sensors Used |
|----------|-------------|--------------|
| **🔍 Search** | Search for opponent when none detected | Ultrasonic + Movement |
| **⚔️ Attack** | Move toward detected opponent | Ultrasonic + Motors |
| **🛡️ Defend** | Back away from ring edge | Line sensor + Motors |
| **🎯 Ram** | Full-speed charge when opponent close | Ultrasonic + Maximum speed |

#### 🎬 Strategy Demonstration
Show students three different robot behaviors:
1. **Aggressive Bot:** Always moves forward, attacks immediately
2. **Defensive Bot:** Stays in center, only attacks when approached
3. **Tactical Bot:** Hunts carefully, positions strategically

#### Basic Sumo Code Structure
```pseudocode
REPEAT FOREVER:
  IF line sensor detects BLACK (ring edge):
    PRIORITY 1: Back away from edge + turn
  ELSE IF ultrasonic detects opponent VERY CLOSE (< 10cm):
    PRIORITY 2: ATTACK! Full speed forward
  ELSE:
    PRIORITY 4: HUNT - spin and search for opponent
```

### 💻 Phase 2: Programming Sumo Bots (20 minutes)

#### 🛠️ Implementation Steps (15 minutes)

**Step 1: Boundary Safety (5 minutes)**
```pseudocode
IF line sensor detects BLACK:
  Stop immediately
  Reverse 0.5 seconds
  Turn right
  Continue with main strategy
```

**Step 2: Add Opponent Detection (5 minutes)**
```pseudocode
IF ultrasonic distance < 10cm:
  Set motors to MAXIMUM SPEED
  Move forward (ATTACK!)
```

**Step 3: Add Hunting Behavior (5 minutes)**
```pseudocode
ELSE (no opponent detected):
  Move forward 1 second
  Turn right 90 degrees
  Repeat (creates searching pattern)
```

#### 🧪 Strategy Testing (5 minutes)
- Students test their basic sumo bot
- Practice against stationary objects
- Adjust sensor thresholds and speeds

> **🔧 Tuning Tips:**
> - Increase attack speed for more aggressive bots
> - Reduce turn angles for smoother hunting
> - Adjust ultrasonic thresholds based on ring size

### 🎯 Phase 3: Advanced Strategy Development (15 minutes)

#### Choose Your Fighting Style

<details>
<summary><strong>🗡️ BERSERKER STRATEGY (Aggressive)</strong></summary>

**Philosophy:** Find and destroy!
```pseudocode
REPEAT FOREVER:
  IF line sensor detects BLACK:
    Back away quickly
  ELSE IF ultrasonic detects ANYTHING:
    FULL SPEED ATTACK!
  ELSE:
    Spin fast and hunt
```
**Pros:** Quick victories, intimidating
**Cons:** Easy to trick, wastes energy

</details>

<details>
<summary><strong>🏰 FORTRESS STRATEGY (Defensive)</strong></summary>

**Philosophy:** Let them come to you
```pseudocode
REPEAT FOREVER:
  IF line sensor detects BLACK:
    Move to center of ring
  ELSE IF ultrasonic detects opponent < 15cm:
    Attack with controlled speed
  ELSE:
    Stay in center, slowly rotate
```
**Pros:** Conserves energy, hard to push out
**Cons:** Slow matches, requires patience

</details>

<details>
<summary><strong>🥷 NINJA STRATEGY (Tactical)</strong></summary>

**Philosophy:** Smart positioning and timing
```pseudocode
REPEAT FOREVER:
  IF line sensor detects BLACK:
    Smart retreat (back up + strategic turn)
  ELSE IF ultrasonic detects opponent < 8cm:
    Quick attack burst
  ELSE IF ultrasonic detects opponent < 25cm:
    Circle around opponent
  ELSE:
    Patrol ring edges, hunt systematically
```
**Pros:** Unpredictable, strategic
**Cons:** Complex to program, requires tuning

</details>

#### 🎨 Strategy Customization (10 minutes)
- Students choose their preferred strategy
- Modify code to match their fighting style
- Test and refine their approach

#### 🔧 Bot Customization (5 minutes)
- Add optional weights for stability
- Adjust wheel positions if possible
- Name their sumo bot warrior!

### 🏆 Phase 4: SUMO TOURNAMENT (10 minutes)

#### 🥋 Tournament Structure

**Round 1: Qualifying Matches (5 minutes)**
- 3 simultaneous rings running
- Each bot fights 2 matches
- Best 2 out of 3 wins advances

**Round 2: Championship Bracket (5 minutes)**
- Single elimination
- 60-second matches
- Winner announced as **SUMO CHAMPION**

#### 📏 Official Sumo Rules
- Ring diameter: 2 meters
- Match duration: 60 seconds maximum
- Win conditions:
  - Opponent touches/crosses black line
  - Opponent stops moving for 10 seconds
  - Time limit reached (judge decision)

#### 🎖️ Championship Categories
- **🏅 Overall Champion:** Tournament winner
- **🧠 Best Strategy:** Most creative programming approach
- **🛡️ Best Defense:** Hardest bot to push out
- **⚡ Fastest Victory:** Quickest match win

## 🎉 WRAP-UP & REFLECTION (5 minutes)

### 🏆 Championship Ceremony
- Announce winners in each category
- Award Code-Easy championship stickers
- Photo opportunity with winning bots

### 💭 Strategy Reflection
- "Which strategy worked best in the tournament?"
- "What would you change about your bot's behavior?"
- "How did sensor placement affect performance?"
- "What real-world robots use similar strategies?"

### 🔮 Preview Next Week
- "Next week we'll add wireless control for remote-controlled robot battles!"
- "Think about how you could improve your sumo bot with remote control"

## 🎯 DIFFERENTIATION STRATEGIES

<details>
<summary><strong>👶 For Younger Students (7-10)</strong></summary>

- Start with simple aggressive strategy (always attack)
- Use visual flowcharts for strategy planning
- Partner with older students for advanced features
- Focus on one strategy modification at a time

</details>

<details>
<summary><strong>🧑 For Older Students (11-16)</strong></summary>

- Encourage complex multi-behavior strategies
- Introduce variables for dynamic speed control
- Challenge them to create hybrid strategies
- Add sensor data analysis and optimization

</details>

<details>
<summary><strong>🚀 For Advanced Students</strong></summary>

- Implement machine learning-style adaptation
- Create strategies that counter specific opponents
- Add multiple ultrasonic sensors for 360° detection
- Research professional robot sumo competitions

</details>

## 📚 EXTENSION ACTIVITIES

### 🏠 Take-Home Challenge
- Design the "ultimate sumo robot" on paper
- Research famous robot sumo competitions (Robot World Cup)
- Create a strategy guide for different opponent types

### 🎮 Bonus Challenges
- **Team Tournament:** 2v2 sumo battles
- **King of the Hill:** One bot defends, others attack
- **Sumo Soccer:** Push a ball out of the ring instead of opponent

## ✅ ASSESSMENT CHECKLIST

### Technical Skills
- [ ] Successfully implemented boundary detection
- [ ] Robot responds appropriately to opponents
- [ ] Multi-sensor coordination working
- [ ] Strategy code executes as planned

### Strategic Thinking
- [ ] Chose appropriate strategy for their goals
- [ ] Adapted strategy based on testing
- [ ] Understood trade-offs between approaches
- [ ] Made strategic decisions during matches

### Problem-Solving
- [ ] Debugged sensor issues independently
- [ ] Optimized code for better performance
- [ ] Adapted to different opponents
- [ ] Helped teammates troubleshoot

### Competition Skills
- [ ] Demonstrated good sportsmanship
- [ ] Analyzed opponent strategies
- [ ] Made real-time strategic decisions
- [ ] Learned from losses and victories

## 🧑‍🏫 INSTRUCTOR NOTES

### ⏰ Pre-Lesson Setup (15 minutes before class)
- [ ] Create 2-3 sumo rings with black tape (2m diameter)
- [ ] Test all robots and sensors thoroughly
- [ ] Prepare tournament bracket chart
- [ ] Set up judging/timing station
- [ ] Prepare championship stickers and certificates

### 🛠️ Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| Robot spins in circles | Reduce turn duration, check motor balance |
| Inconsistent line detection | Ensure tape contrast, clean sensors |
| Robot too slow/fast | Adjust motor speeds for optimal performance |
| Ultrasonic false readings | Check for interference, adjust thresholds |
| Robot stuck in corners | Add corner escape logic to boundary code |

### 🎯 Tournament Management Tips
- Have backup robots ready for technical issues
- Keep matches short (60 seconds max) for engagement
- Encourage cheering and team spirit
- Take photos/videos for parent communication
- Have tie-breaker rules ready

### ⚠️ Safety Reminders
- No touching robots during matches
- Clear spectator zones around rings
- Handle robots gently between matches
- Report any damaged sensors immediately

### 🎪 Creating Excitement
- Use sports commentary during matches
- Create "robot introductions" before battles
- Encourage students to name their bots
- Build suspense with countdown timers

---

<div align="center">

*This lesson combines technical programming skills with strategic thinking and competitive excitement. Students learn that successful robotics isn't just about coding—it's about understanding your environment, anticipating challenges, and making smart decisions under pressure.*

**🏆 May the best bot win!**

**📞 Contact Code-Easy**  
WhatsApp Business | Email | [Website]

</div>
