#1. Test the code and make the line detector work. (You might have to adjust the white handle)
#2. Add an LED to light up when black line is detected
#3. Make the car follow the line with the method we talked about from the worksheet

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
    print(left_line_sensor.value()) 
    
    utime.sleep_ms(10)  # Tiny delay to reduce sensor noise
