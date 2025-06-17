from machine import Pin
import utime

# Motor control pins setup
IN1 = Pin(0, Pin.OUT)  # Left motor forward
IN2 = Pin(1, Pin.OUT)  # Left motor backward
IN3 = Pin(2, Pin.OUT)  # Right motor forward
IN4 = Pin(3, Pin.OUT)  # Right motor backward

# Ultrasonic sensor setup
trig = Pin(8, Pin.OUT)
echo = Pin(7, Pin.IN)

def measure_distance():
    trig.low()
    utime.sleep_us(2)
    trig.high()
    utime.sleep_us(10)
    trig.low()
    
    timeout = utime.ticks_us() + 100000  # 100ms timeout
    while echo.value() == 0:
        if utime.ticks_us() > timeout:
            return -1
    pulse_start = utime.ticks_us()
    
    timeout = utime.ticks_us() + 100000  # 100ms timeout
    while echo.value() == 1:
        if utime.ticks_us() > timeout:
            return -1
    pulse_end = utime.ticks_us()
    
    pulse_duration = pulse_end - pulse_start
    return (pulse_duration * 0.0343) / 2  # Convert to cm

def stop():
    IN1.low(); IN2.low(); IN3.low(); IN4.low()

def move_forward():
    IN1.high(); IN2.low(); IN3.high(); IN4.low()

def move_backward():
    IN1.low(); IN2.high(); IN3.low(); IN4.high()

def turn_right():
    IN1.high(); IN2.low(); IN3.low(); IN4.high()

def turn_left():
    IN1.low(); IN2.high(); IN3.high(); IN4.low()

# Main obstacle avoidance loop
while True:
    distance = measure_distance()
    
    if distance < 15:  # If an obstacle is detected within 15 cm
        stop()
        print("Obstacle detected! Stopping.")
        utime.sleep(1)
        
        # Decide to turn left or right (e.g., turn left in this case)
        print("Turning Left.")
        turn_left()
        
    else:
        move_forward()  # Move forward if no obstacle is detected
        print("No Obstacle. Moving Forward.")
        
    utime.sleep(0.1)  # Wait a bit before measuring again

