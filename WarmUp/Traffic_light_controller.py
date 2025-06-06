"""
Traffic Light Robot Controller - 15 Minute Challenge
==================================================

Your robot is approaching different colored markers on the ground.
Write a program that tells the robot what to do based on the color it detects.

SCENARIO:
- Red marker (value = 1) → STOP
- Green marker (value = 2) → GO FORWARD  
- Yellow marker (value = 3) → SLOW DOWN
- No marker/White ground (value = 0) → SEARCH FOR LINE

This exercise prepares you for line-following logic!
"""

import time
import random

def read_color_sensor():
    """
    Simulates reading from a color sensor
    Returns:
        0 = White/No marker
        1 = Red marker
        2 = Green marker  
        3 = Yellow marker
    """
    return random.randint(0, 3)

def robot_action(sensor_reading):
    """
    STUDENT CHALLENGE: Complete this function!
    
    Based on the sensor reading, return what the robot should do.
    
    Parameters:
        sensor_reading: Integer from 0-3 representing detected color
        
    Returns:
        String describing the robot's action
    """
    
    # TODO: Write your if/elif/else logic here
    # Example structure:
    # if sensor_reading == 1:
    #     return "STOP - Red marker detected!"
    # elif sensor_reading == 2:
    #     return "GO FORWARD - Green marker detected!"
    # ... continue for other cases
    
    pass  # Remove this line when you add your code

def run_traffic_simulation():
    """
    Run the traffic light simulation
    """
    print("🚦 Traffic Light Robot Controller 🚦")
    print("=====================================")
    print("Robot is moving through a course with colored markers...")
    print()
    
    for step in range(1, 11):
        print(f"Step {step}:")
        
        # Read the color sensor
        color_detected = read_color_sensor()
        
        # Convert number to color name for display
        colors = ["White/No marker", "Red", "Green", "Yellow"]
        print(f"   Sensor detects: {colors[color_detected]} (value: {color_detected})")
        
        # Get robot action based on sensor reading
        action = robot_action(color_detected)
        
        if action:
            print(f"   Robot action: {action}")
        else:
            print("   Robot action: No action defined!")
        
        print("-" * 40)
        time.sleep(0.5)
    
    print("Simulation complete! 🏁")

# BONUS CHALLENGES:
# 1. Add a counter for how many times each color was detected
# 2. Make the robot remember the last color and react differently
# 3. Add logic for color combinations (e.g., red followed by green)

# DISCUSSION QUESTIONS:
# 1. How is this similar to line following?
# 2. What happens if the sensor gives unexpected readings?
# 3. How could we make the robot's behavior more sophisticated?

if __name__ == "__main__":
    run_traffic_simulation()


# SOLUTION (Show after students attempt):
def robot_action_solution(sensor_reading):
    """
    Solution to the traffic light controller
    """
    if sensor_reading == 1:
        return "STOP - Red marker detected!"
    elif sensor_reading == 2:
        return "GO FORWARD - Green marker detected!"
    elif sensor_reading == 3:
        return "SLOW DOWN - Yellow marker detected!"
    elif sensor_reading == 0:
        return "SEARCH FOR LINE - No marker detected"
    else:
        return "ERROR - Unknown sensor reading!"
