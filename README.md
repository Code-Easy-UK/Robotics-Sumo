# 🚀 Line Follower Robot Project  

**Duration**: 60 minutes  

## 🛠 Equipment Needed
- Robot cars
- KY-033 sensors (TCRT5000)
- Black electrical tape
- Laptops
- Jumper wires
- Breadboards (if needed)
- Pre-made test tracks

---

## 📝 Lesson Structure

| Part | Topic | Duration |
|------|-------|----------|
| 1 | Warm-up Programming Challenge | 15 minutes |
| 2 | Understanding the KY-033 Sensor | 10 minutes |
| 3 | Three Practical Activities | 30 minutes |
| 4 | Wrap-up and Next Steps | 5 minutes |

---

## Part 1: Programming Warm-up (15 minutes)
**Objective**: Get students thinking about conditional logic for sensor-based decisions

### Activity: "Traffic Light Controller"
- **Scenario**:  
  "Your robot approaches different colored markers on the ground"
  
- **Instructions**:
  - Students will write a simple program that simulates a robot responding to different colored signals
  - Code responses for different inputs
  - Prepares thinking for line-following logic

---

## Part 2: KY-033 Sensor Deep Dive (10 minutes)
**Objective**: Understand how the TCRT5000 sensor detects lines

### Key Concepts:
- Physical components (IR LED and phototransistor)
- Reflection vs absorption principles
- Digital vs analog output modes
- Wiring to the Pico
- Calibration considerations

### Demonstration:
- Live demonstration with sensor over black and white surfaces
- Show voltage readings on multimeter
- Connect to Pico and show digital readings

---

## Part 3: Three Hands-on Activities (30 minutes)

### Activity 1: Basic Sensor Reading (8 minutes)
- Test the sensor and understand its output
- Example code:
```python
from machine import Pin
sensor = Pin(16, Pin.IN)
while True:
    print(sensor.value())

## 📋 Lesson Plan  
| Part | Activity          | Duration |
|------|-------------------|----------|
| 1    | Warm-up Challenge | 15 min   |
| 2    | Sensor Demo       | 10 min   |

---

### 🔧 Equipment Needed  
- KY-033 Sensors  
- Raspberry Pi Pico  
- Black tape  

---

## 💻 Code Example  
```python
from machine import Pin  
sensor = Pin(16, Pin.IN)  
print(sensor.value())  
