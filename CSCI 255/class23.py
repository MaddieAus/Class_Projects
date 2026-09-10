'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class23
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''
from Keyboard import Keyboard
import MTECH_GPIO as GPIO
from time import sleep
import threading


Pin = 21
BuzzerP = 20

light_value = 0
running = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(Pin, GPIO.OUT)
GPIO.setup(BuzzerP, GPIO.OUT)

print("-- Light Controlled Buzzer --")
print("Brightness controls beep speed.")
print("Press ESC to exit.")


# -----------Light Sensor--------------------
def sensor():

    global light_value, running

    while running:

        counter = 0

        GPIO.setup(Pin, GPIO.OUT)
        GPIO.output(Pin, 0)
        sleep(0.1)

        GPIO.setup(Pin, GPIO.IN)

        while GPIO.input(Pin) == 0:
            counter += 1

        light_value = counter


# -------------------------------------


# ------------Buzzer-------------------
def buzzer():

    global light_value, running

    while running:

        if light_value < 300:
            delay = 0.1
        elif light_value < 800:
            delay = 0.5
        else:
            delay = 1.0

        print("/r\x0dLight value:", light_value, "Beep delay:", delay, "s", end="\r")

        GPIO.output(BuzzerP, 1)
        sleep(0.1)

        GPIO.output(BuzzerP, 0)
        sleep(delay)
# --------------------------------------


sensor_thread = threading.Thread(target=sensor)
buzzer_thread = threading.Thread(target=buzzer)

sensor_thread.start()
buzzer_thread.start()



# ---------Keyboard Handling-------------------

kb = Keyboard()
kb.initiation()

try:

    while True:

        bytes_data, length = kb.readKey()

        if length > 0:

            key = bytes_data[0]

            if key == 27:   # ESC key
                break

        sleep(0.1)

finally:

    running = False

    sensor_thread.join()
    buzzer_thread.join()

    kb.cleanUp()
    GPIO.cleanup()

    print("\x0dEnding Program                                                   ")