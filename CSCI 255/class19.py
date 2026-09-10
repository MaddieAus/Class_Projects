'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class19
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''

import MTECH_GPIO as GPIO
import threading
import time
import sys

import termios # provides an interface to the POSIX terminal control API, used for controlling asynchronous communications ports and manipulating terminal settings [python doc]
import tty # terminal control using built-in modules on Unix-like systems, or third-party libraries for creating interactive command-line interfaces [python doc]
import select

BUZZER_PIN = 21
ENCODER_CLK = 12
ENCODER_DT = 18
ENCODER_SW = 20


state = {
    "mode": "AUTO",          
    "frequency": 440,        # Current frequency
    "running": True
}

state_lock = threading.Lock()#  is a synchronization primitive used to protect shared resources (like variables or files) [pulled from stack overflow]

# set up stuff

GPIO.setmode(GPIO.BCM)

GPIO.setup(ENCODER_CLK, GPIO.IN)
GPIO.setup(ENCODER_DT, GPIO.IN)
GPIO.setup(ENCODER_SW, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.pwm_start(BUZZER_PIN,440, 50)


# sound threading

def sound_thread():

    sweep_direction = 1
    sweep_freq = 150

    while True:

        with state_lock:
            if not state["running"]:
                break
            mode = state["mode"]
            freq = state["frequency"]

        if mode == "AUTO":

            GPIO.pwm_change_frequency(BUZZER_PIN, sweep_freq)

            sweep_freq += sweep_direction * 20

            if sweep_freq >= 2000:
                sweep_direction = -1
            elif sweep_freq <= 150:
                sweep_direction = 1

            time.sleep(0.02)

        else:  # manual mode
            GPIO.pwm_change_frequency(BUZZER_PIN, freq)
            time.sleep(0.05)

    GPIO.pwm_stop(BUZZER_PIN)


# input controler

def encoder_thread():

    last_clk = GPIO.input(ENCODER_CLK)
    last_button = GPIO.input(ENCODER_SW)

    while True:

        with state_lock:
            if not state["running"]:
                break
            mode = state["mode"]

        # button
        button_state = GPIO.input(ENCODER_SW)

        if last_button == 1 and button_state == 0:
            with state_lock:
                if state["mode"] == "AUTO":
                    state["mode"] = "MANUAL"
                else:
                    state["mode"] = "AUTO"

            time.sleep(0.2)  # debounce

        last_button = button_state

        # manual mode only
        clk_state = GPIO.input(ENCODER_CLK)

        if clk_state != last_clk and mode == "MANUAL":

            dt_state = GPIO.input(ENCODER_DT)

            with state_lock:
                if dt_state != clk_state:
                    state["frequency"] += 50
                else:
                    state["frequency"] -= 50

                # Clamp frequency
                state["frequency"] = max(100, min(5000, state["frequency"]))

        last_clk = clk_state

        time.sleep(0.01)


# starter threads
t_sound = threading.Thread(target=sound_thread)
t_encoder = threading.Thread(target=encoder_thread)

t_sound.start()
t_encoder.start()

# esc key 
print("\x0d-- Rotate encoder to change frequency (Manual Mode).")
print("\x0d-- Press encoder button to toggle mode.")
print("\x0d-- Press ESC to exit.")

fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)

tty.setraw(fd)

try:
    while True:

        if select.select([sys.stdin], [], [], 0.1)[0]:
            key = sys.stdin.read(1)
            if key == '\x1b':  # ESC key
                break

except KeyboardInterrupt:
    pass

finally:
    # Stop system
    with state_lock:
        state["running"] = False

    t_sound.join()
    t_encoder.join()

    GPIO.pwm_stop(BUZZER_PIN)
    GPIO.cleanup()

    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)# Set the tty attributes for file descriptor fd from the attributes, which is a list like the one returned by tcgetattr(). The when argument determines when the attributes are changed [python doc]

    print("\x0d Exiting program.")
    sys.exit(0)