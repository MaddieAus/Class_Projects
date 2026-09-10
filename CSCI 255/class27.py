'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class27
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''

import lgpio
from time import sleep
from multiprocessing import Process, Value

def analyzer(temp, hum, running):
    gpio = lgpio.gpiochip_open(0)
    pin1 = 21
    myDHT = DHT11(pin1, gpio)

    red = 13
    green = 19
    blue = 26

    lgpio.gpio_claim_output(gpio, red)
    lgpio.gpio_claim_output(gpio, green)
    lgpio.gpio_claim_output(gpio, blue)

    # current LED values for smooth transitions
    current_r = 0
    current_g = 0
    current_b = 0

    try:
        while running.value:
            result = myDHT.read()

            if result.is_valid():
                temp.value = result.temperature
                hum.value = result.humidity

                # color based on humidity
                if hum.value < 30:
                    target_r, target_g, target_b = 100, 0, 0   # red

                elif hum.value < 60:
                    target_r, target_g, target_b = 100, 100, 0  # yellow

                else:
                    target_r, target_g, target_b = 0, 100, 0   # green

                # smooth transition ooh fancy
                step = 5

                if current_r < target_r:
                    current_r += step
                elif current_r > target_r:
                    current_r -= step

                if current_g < target_g:
                    current_g += step
                elif current_g > target_g:
                    current_g -= step

                if current_b < target_b:
                    current_b += step
                elif current_b > target_b:
                    current_b -= step

                # apply PWM
                lgpio.tx_pwm(gpio, red, 1000, current_r)
                lgpio.tx_pwm(gpio, green, 1000, current_g)
                lgpio.tx_pwm(gpio, blue, 1000, current_b)

            sleep(0.1)

    finally:
        # turn off LED and clean up GPIO
        lgpio.tx_pwm(gpio, red, 1000, 0)
        lgpio.tx_pwm(gpio, green, 1000, 0)
        lgpio.tx_pwm(gpio, blue, 1000, 0)

        lgpio.gpiochip_close(gpio)


def reporter(temp, hum, running):
    while running.value:
        print(f"temp = {temp.value:.1f}°C   humidity = {hum.value:.1f}%")
        sleep(0.5)


def main():

    temperature = Value('d', 0.0)
    humidity = Value('d', 0.0)
    running = Value('b', True)

    sensor_process = Process(
        target=analyzer,
        args=(temperature, humidity, running)
    )

    display_process = Process(
        target=reporter,
        args=(temperature, humidity, running)
    )

    sensor_process.start()
    display_process.start()

    try:
        while True:
            sleep(0.1)
            
    except KeyboardInterrupt:
        print("Exiting...")

        running.value = False

        sensor_process.join(timeout=2)
        display_process.join(timeout=2)

        if sensor_process.is_alive():
            print("Warning: forcing sensor process shutdown")
            sensor_process.terminate()

        if display_process.is_alive():
            print("Warning: forcing display process shutdown")
            display_process.terminate()

        sensor_process.join()
        display_process.join()


# ---------------- DHT11 CLASSES (UNCHANGED) ----------------

class DHT11Result:
    ERR_NO_ERROR = 0
    ERR_MISSING_DATA = 1
    ERR_CRC = 2

    def __init__(self, error_code, temperature, humidity):
        self.error_code = error_code
        self.temperature = temperature
        self.humidity = humidity

    def is_valid(self):
        return self.error_code == DHT11Result.ERR_NO_ERROR


class DHT11:
    def __init__(self, pin, gpio):
        self.__pin = pin
        self.__gpio = gpio

    def read(self):
        lgpio.gpio_claim_output(self.__gpio, self.__pin)

        self.__send_and_sleep(lgpio.HIGH, 0.05)
        self.__send_and_sleep(lgpio.LOW, 0.02)

        lgpio.gpio_claim_input(self.__gpio, self.__pin)

        data = self.__collect_input()
        pull_up_lengths = self.__parse_data_pull_up_lengths(data)

        if len(pull_up_lengths) != 40:
            return DHT11Result(DHT11Result.ERR_MISSING_DATA, 0, 0)

        bits = self.__calculate_bits(pull_up_lengths)
        the_bytes = self.__bits_to_bytes(bits)

        checksum = self.__calculate_checksum(the_bytes)
        if the_bytes[4] != checksum:
            return DHT11Result(DHT11Result.ERR_CRC, 0, 0)

        temperature = the_bytes[2] + float(the_bytes[3]) / 10
        humidity = the_bytes[0] + float(the_bytes[1]) / 10

        return DHT11Result(DHT11Result.ERR_NO_ERROR, temperature, humidity)

    def __send_and_sleep(self, output, sleep_time):
        lgpio.gpio_write(self.__gpio, self.__pin, output)
        sleep(sleep_time)

    def __collect_input(self):
        unchanged_count = 0
        max_unchanged_count = 100

        last = -1
        data = []

        while True:
            current = lgpio.gpio_read(self.__gpio, self.__pin)
            data.append(current)

            if last != current:
                unchanged_count = 0
                last = current
            else:
                unchanged_count += 1
                if unchanged_count > max_unchanged_count:
                    break

        return data

    def __parse_data_pull_up_lengths(self, data):
        STATE_INIT_PULL_DOWN = 1
        STATE_INIT_PULL_UP = 2
        STATE_DATA_FIRST_PULL_DOWN = 3
        STATE_DATA_PULL_UP = 4
        STATE_DATA_PULL_DOWN = 5

        state = STATE_INIT_PULL_DOWN
        lengths = []
        current_length = 0

        for current in data:
            current_length += 1

            if state == STATE_INIT_PULL_DOWN and current == lgpio.LOW:
                state = STATE_INIT_PULL_UP
                continue

            if state == STATE_INIT_PULL_UP and current == lgpio.HIGH:
                state = STATE_DATA_FIRST_PULL_DOWN
                continue

            if state == STATE_DATA_FIRST_PULL_DOWN and current == lgpio.LOW:
                state = STATE_DATA_PULL_UP
                continue

            if state == STATE_DATA_PULL_UP and current == lgpio.HIGH:
                current_length = 0
                state = STATE_DATA_PULL_DOWN
                continue

            if state == STATE_DATA_PULL_DOWN and current == lgpio.LOW:
                lengths.append(current_length)
                state = STATE_DATA_PULL_UP

        return lengths

    def __calculate_bits(self, pull_up_lengths):
        shortest = min(pull_up_lengths)
        longest = max(pull_up_lengths)

        halfway = shortest + ((longest - shortest) >> 1)

        return [length > halfway for length in pull_up_lengths]

    def __bits_to_bytes(self, bits):
        the_bytes = []
        byte = 0

        for i, bit in enumerate(bits):
            byte = (byte << 1) | int(bit)
            if (i + 1) % 8 == 0:
                the_bytes.append(byte)
                byte = 0

        return the_bytes

    def __calculate_checksum(self, the_bytes):
        return (the_bytes[0] + the_bytes[1] + the_bytes[2] + the_bytes[3]) & 255


main()