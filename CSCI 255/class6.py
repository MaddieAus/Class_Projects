from Keyboard import Keyboard
from time import sleep
import MTECH_GPIO as GPIO

'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class6
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''

# --- MAIN PROGRAM ---
print("PROFESSIONAL MODE: ioctl/FIONREAD active\r")
print("Instructions: Press ESC to exit, arrows to test.\r")
#--------------------------------------------------------------------

GPIO.setmode(GPIO.BCM)
outPin = 21
GPIO.setup(outPin, GPIO.OUT)

("--press 'UP arrow' to trun on the LED, 'DOWN arrow' to turn it off, or 'ESC' once to quit")

#--------------------------------------------------------------------
repeat = True
kb = Keyboard()
if kb.initiation():
    try:
        while repeat:
            b, l = kb.readKey()

            # The logic is now razor-sharp:
            # If 1 byte and it's 27 -> it's a standalone ESC key
            if l == 1 and b[0] == 27:
                print("Exiting program", end ="\r")
                repeat = False

            # this is the on and off function of the LED
            if b[0] == 27 and b[1] == 91 and b[2] == 65:
                GPIO.output(outPin,1)
                print("LED is on! ", end="\r")
                
            elif b[0] == 27 and b[1] == 91 and b[2] == 66:
                GPIO.output(outPin,0)
                print("LED is off!", end ="\r")

    finally:
        kb.cleanUp()
        GPIO.cleanup()
else:
    print("Could not initialize keyboard.")