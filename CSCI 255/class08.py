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
inPin = 20
GPIO.setup(outPin, GPIO.OUT)
GPIO.setup(inPin, GPIO.IN)

print("--Press the switch to toggle the LED on/off. Press 'ESC' once to quit--")

#--------------------------------------------------------------------
repeat = True
onoff = 0
keyboardState = 0


kb = Keyboard()
if kb.initiation():
    try:
        while repeat:
            keyboardState = kb.get_buffer_count()
            if ( keyboardState != 0):
                b, l = kb.readKey()

                # The logic is now razor-sharp:
                # If 1 byte and it's 27 -> it's a standalone ESC key
                if l == 1 and b[0] == 27:
                    print("Exiting program", end ="\r")
                    repeat = False

            state = GPIO.input(inPin)
            if (state == 0 and prevstate == 1):
                if (onoff == 1):
                    onoff = 0
                    GPIO.output(outPin,onoff)
                    
                elif (onoff == 0):
                    onoff = 1
                    GPIO.output(outPin,onoff)
            prevstate = state
            sleep(.05)

    finally:
        kb.cleanUp()
        GPIO.cleanup()
else:
    print("Could not initialize keyboard.")


