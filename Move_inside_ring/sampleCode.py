from machine import Pin
import utime

# Line sensor setup
left_line_sensor = Pin(17, Pin.IN)  # TCRT5000 on pin 17 (adjust if needed)
right_line_sensor = Pin(18, Pin.IN)  # TCRT5000 on pin 18 (adjust if needed)

# Motor control pins (same as before)
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

def move_backward(duration=70):
    IN1.low(); IN2.high(); IN3.low(); IN4.high()
    utime.sleep_ms(duration)
    stop()

def move_forward():
    IN1.high(); IN2.low(); IN3.high(); IN4.low()

def turn_left(duration=70):  # Default turn: 500ms
    IN1.low(); IN2.high(); IN3.high(); IN4.low()
    utime.sleep_ms(duration)
    stop()  # Brief pause after turning

def turn_right(duration=70): # Default turn: 500ms
    IN1.high(); IN2.low(); IN3.low(); IN4.high()
    utime.sleep_ms(duration)
    stop()  # Brief pause after turning

# Main loop
while True:
    
    distance = measure_distance()
    print(distance)
    if distance < 20:
        move_forward()
    else:
        
        if left_line_sensor.value() == 0 and right_line_sensor.value() == 0 :  # On the line?
            move_forward()  # Keep going straight!
        elif left_line_sensor.value() == 1 or right_line_sensor.value() == 1 :
            # First, try turning right
            move_backward()
            turn_left()

            utime.sleep_ms(50)  # Small delay to check sensor again
            if measure_distance() < 20:
                continue  # Found the line! Resume forward motion.
    
    utime.sleep_ms(10)  # Tiny delay to reduce sensor noise
