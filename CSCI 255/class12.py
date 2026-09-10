from Keyboard import Keyboard
from time import sleep
import MTECH_GPIO as GPIO
import numpy as np

'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class12
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''


# GPIO setup
RED = 21    # orange wire
GREEN = 20  # green wire
BLUE = 18   # brown wire    IT WAS THE GPIO 16 THAT WASN'T WORKING
BUTTON = 12 # yellow wire

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pins = [RED, GREEN, BLUE]
channel_names = ["RED", "GREEN", "BLUE"]

current_channel = 0
last_button_state = 1

GPIO.pwm_start(RED,frequency = 100, duty_cycle = 0)
GPIO.pwm_start(GREEN,frequency = 100, duty_cycle = 0)
GPIO.pwm_start(BLUE,frequency = 100, duty_cycle = 0)

steps = np.logspace(0, 2, num = 10)
step_index = [0, 0, 0]

kb = Keyboard()
kb.initiation()


print("--Press Button: Brightness (10 steps) | Arrows Left/Right: Change Channel| ESC: Quit--")
print("\r Current Channel:", channel_names[current_channel],"  ", end ="\r")

try:
    while True:

        # button handling
        button_state = GPIO.input(BUTTON)
        if button_state == 1 and last_button_state == 0:
            step_index[current_channel] += 1

            if step_index[current_channel] >= 10: #off
                step_index[current_channel] = 0
                duty = steps[step_index[current_channel]]
                GPIO.pwm_change_duty(pins[current_channel], duty)
            
            else:
                duty = steps[step_index[current_channel]]
                GPIO.pwm_change_duty(pins[current_channel],duty)

        last_button_state = button_state

        # keyboard handling
        if kb.get_buffer_count() > 0:
            key, l = kb.readKey()

            # ESC to exit
            if l == 1 and key[0] == 27:
                print("\r Exiting program.","     ",end ="\r")
                break

            # arrow keys
            elif l == 3:
                if key[0] == 27 and key[1] == 91 and key[2] == 68: # Left
                    current_channel = (current_channel - 1) % 3
                    print("\r Current Channel:", channel_names[current_channel], "  ", end="\r")

                elif key[0] == 27 and key[1] == 91 and key[2] == 67: # Right
                    current_channel = (current_channel + 1) % 3
                    print("\r Current Channel:", channel_names[current_channel], "  ", end="\r")

        sleep(0.05)

finally:
    kb.cleanUp()
    GPIO.pwm_stop(RED)
    GPIO.pwm_stop(GREEN)
    GPIO.pwm_stop(BLUE)
    GPIO.cleanup()
