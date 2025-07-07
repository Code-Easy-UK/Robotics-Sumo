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

def stop():
    IN1.low(); IN2.low(); IN3.low(); IN4.low()

def move_forward():
    IN1.high(); IN2.low(); IN3.high(); IN4.low()

def turn_left(duration=700):  # Default turn: 500ms
    IN1.low(); IN2.high(); IN3.high(); IN4.low()
    utime.sleep_ms(duration)
    stop()  # Brief pause after turning

def turn_right(duration=700): # Default turn: 500ms
    IN1.high(); IN2.low(); IN3.low(); IN4.high()
    utime.sleep_ms(duration)
    stop()  # Brief pause after turning

# Main loop
while True:
    if left_line_sensor.value() == 0 and right_line_sensor.value() == 0 :  # On the line?
        move_forward()  # Keep going straight!
    elif left_line_sensor.value() == 1 and right_line_sensor.value() == 0 :  # Left line sensor detected black line!
        # First, try turning right
        turn_right()
        utime.sleep_ms(50)  # Small delay to check sensor again
    elif left_line_sensor.value() == 0 and right_line_sensor.value() == 1 : # Right line sensor detected black line!
        # If still no line, turn left
        turn_left()
        utime.sleep_ms(50)
    elif left_line_sensor.value() == 1 and right_line_sensor.value() == 1 : # both line sensor detected black line!
        stop()
    else:
        print(f"Error! {left_line_sensor.value()} : {right_line_sensor.value()}")
    
    utime.sleep_ms(10)  # Tiny delay to reduce sensor noise
