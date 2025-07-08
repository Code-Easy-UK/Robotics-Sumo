from machine import Pin
import utime

# Line sensor setup
left_line_sensor = Pin(17, Pin.IN, Pin.PULL_UP)  # TCRT5000 on pin 17 (adjust if needed)
right_line_sensor = Pin(18, Pin.IN, Pin.PULL_UP)  # TCRT5000 on pin 18 (adjust if needed)

# Motor control pins (same as before)
IN1 = Pin(0, Pin.OUT)  # Left motor forward
IN2 = Pin(1, Pin.OUT)  # Left motor backward
IN3 = Pin(2, Pin.OUT)  # Right motor forward
IN4 = Pin(3, Pin.OUT)  # Right motor backward

# Ultrasonic sensor setup
trig = Pin(8, Pin.OUT)
echo = Pin(7, Pin.IN)

state = "searching" # searching, attack and line_detected
attack_range = 20
last_interrupt_time = 0

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

def stop(duration=70):
    IN1.low(); IN2.low(); IN3.low(); IN4.low()
    utime.sleep_ms(duration)
    

def move_backward(duration=70):
    IN1.low(); IN2.high(); IN3.low(); IN4.high()
    utime.sleep_ms(duration)
    stop()

def move_forward(duration=70):
    IN1.high(); IN2.low(); IN3.high(); IN4.low()
    utime.sleep_ms(duration)
    stop()

def turn_left(duration=70):  # Default turn: 500ms
    IN1.low(); IN2.high(); IN3.high(); IN4.low()
    utime.sleep_ms(duration)
    stop()  # Brief pause after turning

def turn_right(duration=70): # Default turn: 500ms
    IN1.high(); IN2.low(); IN3.low(); IN4.high()
    utime.sleep_ms(duration)
    stop()  # Brief pause after turning

def search_opponent(duration=70):
    global state, attack_range
    
    repeat_turns = 5
    
    while repeat_turns > 0:
        distance = measure_distance()
        
        turn_right(duration)
        if distance < attack_range and distance != -1:
            print(distance , " < " , attack_range)
            stop(200)
            state = "attack"
            print(state)
            break
        
        repeat_turns = repeat_turns - 1
        
def attack(duration=70):
    global state, attack_range
    
    engage_opponent = True
    
    while engage_opponent:
        move_forward(100)
        distance = measure_distance()
        if distance > attack_range:
            state = "searching"
            print(state)
            break

def escape(duration=100):
    global state, last_interrupt_time
    
    # Debounce - ignore interrupts within 100ms of last one
    current_time = utime.ticks_ms()
    if utime.ticks_diff(current_time, last_interrupt_time) < 100:
        return
    
    state = "line_detected"
    print(state)

    move_backward(duration)
    state = "searching"
    print(state)


# Start with a pause
utime.sleep_ms(2000)

# Main loop
while True:
    
    distance = measure_distance()
    
    if left_line_sensor.value() == 1 or right_line_sensor.value() == 1:
        escape()
    elif state == "searching":
        search_opponent()
    elif state == "attack":
        attack()
        
    
    utime.sleep_ms(10)  # Tiny delay to reduce sensor noise
