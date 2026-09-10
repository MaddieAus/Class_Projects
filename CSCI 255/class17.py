'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class17
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''


import MTECH_GPIO as GPIO
import threading
import time
# import sys

#the set up 

BUTTON_PIN = 20
TRANSISTOR_PIN = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(TRANSISTOR_PIN, GPIO.OUT)

mode = 0
mode_lock = threading.Lock() #  is a synchronization primitive used to protect shared resources (like variables or files) [pulled from stack overflow]

notrun = 1

def button_monitor(): # function for button
    global mode
    global notrun
    last_state = 0
    while (notrun):
        current_state = GPIO.input(BUTTON_PIN)

        # Detect falling edge (HIGH → LOW)
        if last_state == GPIO.HIGH and current_state == GPIO.LOW:
            with mode_lock:
                mode = (mode + 1) % 3
                print(f"Mode changed to {mode}")

        last_state = current_state
        time.sleep(0.01) 


button_thread = threading.Thread(target=button_monitor, daemon=True)
button_thread.start()

try:
    while(notrun):
        with mode_lock:
            current_mode = mode

        if current_mode == 0:
            GPIO.pwm_stop(TRANSISTOR_PIN)

        elif current_mode == 1:
            GPIO.pwm_start(TRANSISTOR_PIN, 1,50)
            

        elif current_mode == 2:
            GPIO.pwm_change_frequency(TRANSISTOR_PIN, 8)
        time.sleep(.005)

except KeyboardInterrupt:
    notrun = 0
    print("\n Exiting Program.")

finally:
    GPIO.cleanup()
