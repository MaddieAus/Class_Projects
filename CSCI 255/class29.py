'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class29
I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy. I understand the importance the consequences of plagiarism.
'''

import lgpio
from time import sleep

# I2C address of ADS1110
ADS1110_ADDR = 0x48

# Value to write to the configuration register
CONFIG_VALUE = 0b0_00_0_11_00 #0b0_00_1_11_00
# continuous mode, no amplification, full resolution

# Initialize the connection to lgpio
try:
    # Open connection to the I2C port
    handle = lgpio.i2c_open(1, ADS1110_ADDR)  
    print(f"I2C connection to address 0x{ADS1110_ADDR:02x} opened.")

    # Write data to the configuration register
    result = lgpio.i2c_write_byte(handle, CONFIG_VALUE)
    
    if result == 0:
        pass
        #print(f"Configuration written: {CONFIG_VALUE}")
    else:
        print(f"Write error: code {result}")
        raise IOError("Configuration write error")

    # Time for conversion (may be required, check the datasheet)
    sleep(0.1)

    # Read 2 bytes (unchanged in this example)
    while True:
        # Read data from the device
        count, data = lgpio.i2c_read_device(handle, 2)
        
        if count == 2:
            # Combine two bytes into one value (little-endian)
            raw_value = (data[0] << 8) | data[1]        
            if raw_value > 32767: 
                raw_value -= 65536
            
            Temperature = ((raw_value * 2.048 / 32768) - 0.5) * 100
            Ftemp = Temperature * 1.8 + 32


            print(f'{Ftemp}', end = "\r")
        else:
            print(f"Read error. Read {count} bytes.")

        sleep(0.2)

except IOError as e:
    print(f"I/O error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the I2C connection
    if handle >= 0:
        lgpio.i2c_close(handle)
    print("Connection to lgpio closed.")
