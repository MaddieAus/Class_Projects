import time
import lgpio
from Keyboard import Keyboard

'''
John Maynard and Madison Austin
CSCI 255 Spring 2025
Programming Assignment #class31
I acknowledge that I have worked on this assignment independently, except where explicitly noted and referenced. Any collaboration or use of external resources has been properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by the university's academic integrity policy. I understand the importance the consequences of plagiarism
'''

def main():
    chip = lgpio.gpiochip_open(0)
    keyboard = Keyboard()

    PIN_S0 = 16
    PIN_S1 = 20
    PIN_S2 = 21

    PIN_SCL = 26
    PIN_SDA = 19

    lgpio.gpio_claim_output(chip, PIN_S0)
    lgpio.gpio_claim_output(chip, PIN_S1)
    lgpio.gpio_claim_output(chip, PIN_S2)

    i2cHandle = lgpio.i2c_open(1, 0x48)

    lgpio.gpio_write(chip, PIN_S0, 0)
    lgpio.gpio_write(chip, PIN_S1, 0)
    lgpio.gpio_write(chip, PIN_S2, 0)

    currentDevice = 0
    deviceList = ["LM36", "LDR"]
    try:
        config = lgpio.i2c_write_byte(i2cHandle, 0b10001100)
        if config != 0:
            raise IOError
        if not keyboard.initiation():
            raise OSError
        time.sleep(0.1)

        repeat = True
        while repeat:
            count, data = lgpio.i2c_read_device(i2cHandle, 2)

            if count == 2:
                rawValue = (data[0] << 8) | data[1]
                if rawValue > 32767:
                    rawValue -= 65536

                print(f"\r{deviceList[currentDevice]}: {rawValue / 9929:.2f} V        ", end="")

            if keyboard.get_buffer_count() != 0:
                keyPress, bytesGiven = keyboard.readKey()
                if bytesGiven == 1:
                    if keyPress[0] == 49 and currentDevice == 1:
                        lgpio.gpio_write(chip, PIN_S0, 0)
                        currentDevice = 0
                    elif keyPress[0] == 50 and currentDevice == 0:
                        lgpio.gpio_write(chip, PIN_S0, 1)
                        currentDevice = 1
                    elif keyPress[0] == 3:
                            print("\n\rExiting\r")
                            repeat = False

            time.sleep(0.1)


    except KeyboardInterrupt:
        print("Exiting")
    finally:
        keyboard.cleanUp()
        lgpio.i2c_close(i2cHandle)
        lgpio.gpiochip_close(chip)

if __name__ == "__main__":
    main()