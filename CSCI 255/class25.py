'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class25
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''

from Keyboard import Keyboard
import lgpio
from time import sleep
from multiprocessing import Process, Value

# pins
pin = 21

def brain(shared_freq):

    while True:
        # Sweep Up
        for f in range(150, 5001, 50):
            shared_freq.value = f 
            sleep(0.01) 
        
        # Sweep Down
        for f in range(5000, 149, -50):
            shared_freq.value = f 
            sleep(0.01) 

def voice(shared_freq):

    try:
        h = lgpio.gpiochip_open(0)
        lgpio.gpio_claim_output(h, pin)
        while True:
            current_f = shared_freq.value 
            # lgpio.tx_pwm(handle, pin, frequency, duty_cycle)
            lgpio.tx_pwm(h, pin, current_f, 50) 
            sleep(0.05) # Small sleep to prevent CPU hogging
    except KeyboardInterrupt:
        lgpio.tx_pwm(h, pin, 0, 0) # Silence PWM
        lgpio.gpiochip_close(h)

def main():

    # 1. Initialize Shared Memory (integer type 'i')
    shared_freq = Value('i', 150)



    # 3. Define Processes [cite: 9, 34]
    p1 = Process(target=brain, args=[shared_freq])
    p2 = Process(target=voice, args=[shared_freq]) 

    try:
        # 4. Start Processes 
        p1.start()
        p2.start()
        
        print("Siren running... Press Ctrl+C to stop.")
        # 5. Wait for interrupt 
        while True:
            sleep(1)

    except KeyboardInterrupt:
        print("\n Exiting program")

    finally:
        # 6. Cleanup: Stop processes, silence buzzer, and close handle 
        p1.terminate()
        p2.terminate()
        print("Hardware cleaned up.")

main()