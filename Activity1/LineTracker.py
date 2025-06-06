"""
Activity 1: Basic KY-033 Sensor Reading (8 minutes)
==================================================

OBJECTIVE: Test the KY-033 sensor and understand its digital output

SETUP:
1. Connect KY-033 to your Pico:
   - VCC → 3V3 (pin 36)
   - GND → GND (pin 38) 
   - OUT → GP16 (pin 21)

2. Position sensor 2-3mm above a surface

TASK: Run this code and test the sensor over black and white surfaces
"""

from machine import Pin
import time

# Set up the KY-033 line sensor
LINE_SENSOR = Pin(16, Pin.IN)

def read_line_sensor():
    """
    Read the digital output from KY-033 sensor
    Returns:
        1 if sensor detects BLACK surface (line)
        0 if sensor detects WHITE surface (background)
    
    Note: KY-033 outputs LOW (0) when it detects black,
          and HIGH (1) when it detects white.
          We invert this to match our logic.
    """
    raw_value = LINE_SENSOR.value()
    # Invert the reading so 1 = black line, 0 = white background
    return 1 if raw_value == 0 else 0

def sensor_test():
    """
    Continuously read and display sensor values
    """
    print("KY-033 Line Sensor Test")
    print("======================")
    print("Hold sensor over different surfaces:")
    print("- Black surfaces should show: 1")
    print("- White surfaces should show: 0")
    print("Press Ctrl+C to stop")
    print()
    
    try:
        while True:
            # Read sensor value
            sensor_value = read_line_sensor()
            raw_value = LINE_SENSOR.value()
            
            # Determine surface type
            surface_type = "BLACK LINE" if sensor_value == 1 else "WHITE BACKGROUND"
            
            # Display results
            print(f"Raw sensor: {raw_value} | Processed: {sensor_value} | Surface: {surface_type}")
            
            # Wait before next reading
            time.sleep(0.2)
            
    except KeyboardInterrupt:
        print("\nSensor test stopped")

# STUDENT TASKS:
# 1. Run the code and test over black electrical tape
# 2. Test over white paper
# 3. Try different heights (1mm, 5mm, 10mm) - what happens?
# 4. Test under different lighting conditions
# 5. Record your observations in comments below:

"""
OBSERVATIONS:
- Black tape readings: 
- White paper readings:
- Effect of height:
- Effect of lighting:
- Optimal sensor height:
"""

# DISCUSSION QUESTIONS:
# 1. Why do we invert the sensor reading?
# 2. What could cause inconsistent readings?
# 3. How might we improve sensor reliability?

if __name__ == "__main__":
    sensor_test()
