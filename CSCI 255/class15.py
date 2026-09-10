from time import sleep
import MTECH_GPIO as GPIO
import numpy as np

'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class15
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''

# LED pins
RED = 26
GREEN = 19
BLUE = 13

# rotary pins
DT  = 18
CLK = 20
SW  = 21

# all the GPIO stuff
GPIO.setmode(GPIO.BCM)

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

GPIO.setup(DT, GPIO.IN)
GPIO.setup(CLK, GPIO.IN)
GPIO.setup(SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.pwm_start(RED, frequency=100, duty_cycle=0)
GPIO.pwm_start(GREEN, frequency=100, duty_cycle=0)
GPIO.pwm_start(BLUE, frequency=100, duty_cycle=0)

pins = [RED, GREEN, BLUE]
channel_names = ["RED", "GREEN", "BLUE"]

# brightness
steps = np.logspace(0, 2, num=10)

# Brightness index per channel
step_index = [0, 0, 0]

# Active channel
current_channel = 0


# Encoder State Variables
last_encoded = ((GPIO.input(DT) << 1) | GPIO.input(CLK))
sw_last_state = GPIO.HIGH

print("RGB PWM Control with Rotary Encoder")
print("Ctrl+C to exit")
print("\rActive: RED | R: 0% G: 0% B: 0%", end="\r")

try:
    while True:

        # encoder rotary code
        msb = GPIO.input(DT)
        lsb = GPIO.input(CLK)

        current_encoded = (msb << 1) | lsb
        sum_state = (last_encoded << 2) | current_encoded

        match sum_state:
            # Clockwise
            case 0b1110 | 0b1000 | 0b0001 | 0b0111:
                if step_index[current_channel] > 0:
                    step_index[current_channel] -= 1

            # Counter-Clockwise
            case 0b1101 | 0b0100 | 0b0010 | 0b1011:
                if step_index[current_channel] < 9:
                    step_index[current_channel] += 1

            case _:
                pass

        last_encoded = current_encoded

        # PWM no wrap around
        for i in range(3):
            if step_index[i] == 0:
                duty = 0
            else:
                duty = steps[step_index[i]]

            GPIO.pwm_change_duty(pins[i], duty)

        # button = channel change
        sw_state = GPIO.input(SW)

        if sw_state == GPIO.LOW and sw_last_state == GPIO.HIGH:
            current_channel = (current_channel + 1) % 3
            sleep(0.2)  # debounce

        sw_last_state = sw_state

        # status output
        r_percent = int(steps[step_index[0]]) if step_index[0] > 0 else 0
        g_percent = int(steps[step_index[1]]) if step_index[1] > 0 else 0
        b_percent = int(steps[step_index[2]]) if step_index[2] > 0 else 0

        print(f"\rActive: {channel_names[current_channel]} | "
              f"R: {r_percent}% "
              f"G: {g_percent}% "
              f"B: {b_percent}% ", end="\r")

        sleep(0.001)

except KeyboardInterrupt:
    print("\n Exiting program.")

finally:
    GPIO.pwm_stop(RED)
    GPIO.pwm_stop(GREEN)
    GPIO.pwm_stop(BLUE)
    GPIO.cleanup()