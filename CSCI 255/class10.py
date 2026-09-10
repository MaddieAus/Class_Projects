
'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class10
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''


from Keyboard import Keyboard
from time import sleep
import MTECH_GPIO as GPIO

# GPIO setup
RED = 21
GREEN = 20
BLUE = 16
BUTTON = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(BUTTON, GPIO.IN)

pins = [RED, GREEN, BLUE]
channel_names = ["RED", "GREEN", "BLUE"]

current_channel = 0
led_states = [0, 0, 0] 
last_button_state = 0

kb = Keyboard()
kb.initiation()


print("-- Press the Switch to cycle RGB channels. "
      "Use Arrows UP/DOWN to toggle light. Press 'ESC' to quit. --")
print("\r Current Channel:", channel_names[current_channel],"  ", end ="\r")

try:
    while True:

        # button handling
        button_state = GPIO.input(BUTTON)
        if button_state == 1 and last_button_state == 0:
            current_channel = (current_channel + 1) % 3
            print("\r Current Channel:", channel_names[current_channel],"  ", end ="\r")
            sleep(0.1)   # debounce

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
                if key[0] == 27 and key[1] == 91 and key[2] == 65:
                    led_states[current_channel] = 1   # UP 

                elif key[0] == 27 and key[1] == 91 and key[2] == 66:
                    led_states[current_channel] = 0   # DOWN 

        # update LEDs
        for i in range(3):
            GPIO.output(pins[i], led_states[i])

        sleep(0.05)

finally:
    kb.cleanUp()
    GPIO.output(RED, 0)
    GPIO.output(GREEN, 0)
    GPIO.output(BLUE, 0)
    GPIO.cleanup()
