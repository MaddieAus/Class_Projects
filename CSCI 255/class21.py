'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class21
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''
from Keyboard import Keyboard
import MTECH_GPIO as GPIO
from time import sleep
import threading
import time

SERVO = 21
dutyC = 98
running = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO, GPIO.OUT)

GPIO.pwm_start(SERVO, frequency=50, duty_cycle=dutyC)

print("-- Press '↑' to increase the angle, '↓' to decrease, ESC to exit. --")

#-----------------------------------servo--------------------------------#
def servo_control():
    global dutyC
    global running

    lastDuty = dutyC

    while running:
        if dutyC != lastDuty:
            GPIO.pwm_change_duty(SERVO, dutyC)
            sleep(0.3)
            GPIO.pwm_change_duty(SERVO, 0)
            lastDuty = dutyC

        sleep(0.1)

#-----------------------------------------------------------------------#

#-----------------------------------keyboard--------------------------------#
def key_board():
    global dutyC
    global running

    kb = Keyboard()

    if kb.initiation():
        try:
            while running:
                b, l = kb.readKey()

                # ESC
                if l == 1 and b[0] == 27:
                    running = False

                # UP arrow
                elif l == 3 and b[0] == 27 and b[1] == 91 and b[2] == 65:
                    dutyC += 0.2
                    if dutyC > 98:     # prevents moving past 0
                        dutyC = 98

                # DOWN arrow
                elif l == 3 and b[0] == 27 and b[1] == 91 and b[2] == 66:
                    dutyC -= 0.2
                    if dutyC < 88:     # prevents moving past -180
                        dutyC = 88

        finally:
            kb.cleanUp()
            GPIO.pwm_stop(SERVO)
            GPIO.cleanup()

#-------------------------------------------------------------------------# 

t_servo_control = threading.Thread(target=servo_control)
t_key_board = threading.Thread(target=key_board)

t_servo_control.start()
t_key_board.start()

t_servo_control.join()
t_key_board.join()