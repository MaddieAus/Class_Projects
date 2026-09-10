'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class35

I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy.
'''
# light moving the dog: the darker it is the faster the dog moves the brighter it is the slower the dog moves

import lgpio
import threading
from time import sleep
from PIL import Image, ImageDraw, ImageOps
from Keyboard import Keyboard


# set up
# -----------------------------
chip = lgpio.gpiochip_open(0)
Pin = 21   # Light sensor pin

light_value = 0
running = True

print("\r-- Light Controlled OLED Dog --")
print("\rThe brightness controls how fast or slow he will run!.")
print("\r...but he's scared of the dark.")
print("\rPress ESC to exit.")

# I just moved this here because i feel like I have enough inputs
# -----------------------------
SSD1306_I2C_ADDRESS = 0x3C
SSD1306_SETCONTRAST = 0x81
SSD1306_DISPLAYALLON_RESUME = 0xA4
SSD1306_NORMALDISPLAY = 0xA6
SSD1306_INVERTDISPLAY = 0xA7
SSD1306_DISPLAYOFF = 0xAE
SSD1306_DISPLAYON = 0xAF
SSD1306_SETDISPLAYCLOCKDIV = 0xD5
SSD1306_SETMULTIPLEX = 0xA8
SSD1306_SETDISPLAYOFFSET = 0xD3
SSD1306_SETSTARTLINE = 0x40
SSD1306_CHARGEPUMP = 0x8D
SSD1306_MEMORYMODE = 0x20
SSD1306_COLUMNADDR = 0x21
SSD1306_PAGEADDR = 0x22
SSD1306_COMSCANDEC = 0xC8
SSD1306_SEGREMAP = 0xA1
SSD1306_SETCOMPINS = 0xDA

SSD1306_ACTIVATE_SCROLL = 0x2F
SSD1306_DEACTIVATE_SCROLL = 0x2E
SSD1306_RIGHT_HORIZONTAL_SCROLL = 0x26

DATA_MODE = 0x40
COMMAND_MODE = 0x00


class MTech_SSD1306:
    """
    Hardware driver for SSD1306 OLED displays using lgpio.
    """

    def __init__(self, bus=1, address=SSD1306_I2C_ADDRESS, width=128, height=32):
        self.width = width
        self.height = height
        self.address = address
        self.pages = height // 8
        self._buffer = [0] * (width * self.pages)

        try:
            self.handle = lgpio.i2c_open(bus, address)
            self._initialize()
        except Exception as e:
            print(f"I2C Init Error: {e}")
            self.handle = -1

    def command(self, cmd):
        lgpio.i2c_write_device(self.handle, [COMMAND_MODE, cmd])

    def _initialize(self):
        cmds = [
            SSD1306_DISPLAYOFF,
            SSD1306_SETDISPLAYCLOCKDIV, 0x80,
            SSD1306_SETMULTIPLEX, 0x1F,
            SSD1306_SETDISPLAYOFFSET, 0x00,
            SSD1306_SETSTARTLINE | 0x00,
            SSD1306_CHARGEPUMP, 0x14,
            SSD1306_MEMORYMODE, 0x00,
            SSD1306_SEGREMAP,
            SSD1306_COMSCANDEC,
            SSD1306_SETCOMPINS, 0x02,
            SSD1306_SETCONTRAST, 0x8F,
            0xD9, 0xF1,
            0xDB, 0x40,
            SSD1306_DISPLAYALLON_RESUME,
            SSD1306_NORMALDISPLAY,
            SSD1306_DISPLAYON
        ]
        for c in cmds:
            self.command(c)

    # --- GRAPHICS ---

    def draw_pixel(self, x, y, color, transmit=True):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return

        page = y // 8
        bit = y % 8
        index = (page * self.width) + x

        if color:
            self._buffer[index] |= (1 << bit)
        else:
            self._buffer[index] &= ~(1 << bit)

        if transmit:
            self.command(SSD1306_COLUMNADDR)
            self.command(x)
            self.command(x)

            self.command(SSD1306_PAGEADDR)
            self.command(page)
            self.command(page)

            lgpio.i2c_write_device(self.handle, [DATA_MODE, self._buffer[index]])

    def set_pixel(self, x, y, color):
        if 0 <= x < self.width and 0 <= y < self.height:
            page = y // 8
            bit = y % 8
            index = (page * self.width) + x

            if color:
                self._buffer[index] |= (1 << bit)
            else:
                self._buffer[index] &= ~(1 << bit)

    def show(self):
        self.command(SSD1306_COLUMNADDR)
        self.command(0)
        self.command(self.width - 1)
        self.command(SSD1306_PAGEADDR)
        self.command(0)
        self.command(self.pages - 1)

        for i in range(0, len(self._buffer), 64):
            chunk = self._buffer[i:i+64]
            lgpio.i2c_write_device(self.handle, [DATA_MODE] + chunk)

    def load_image(self, image):
        img = image.convert('1').resize((self.width, self.height))
        pix = img.load()
        self.clear_buffer()

        for y in range(self.height):
            for x in range(self.width):
                if pix[x, y]:
                    self.set_pixel(x, y, True)

    def clear_buffer(self):
        self._buffer = [0] * len(self._buffer)

    def clear_screen(self):
        self.clear_buffer()
        self.show()

    # --- HARDWARE FEATURES ---

    def start_scroll_right(self, start=0, stop=3):
        self.command(SSD1306_RIGHT_HORIZONTAL_SCROLL)
        self.command(0x00)
        self.command(start)
        self.command(0x00)
        self.command(stop)
        self.command(0x00)
        self.command(0xFF)
        self.command(SSD1306_ACTIVATE_SCROLL)

    def stop_scroll(self):
        self.command(SSD1306_DEACTIVATE_SCROLL)

    def set_contrast(self, level):
        self.command(SSD1306_SETCONTRAST)
        self.command(level & 0xFF)

    def close(self):
        if self.handle >= 0:
            self.clear_buffer()
            self.show()
            self.command(SSD1306_DISPLAYOFF)
            lgpio.i2c_close(self.handle)

# light sensor
# -----------------------------
def sensor():
    global light_value, running

    while running:
        counter = 0

        # Discharge capacitor
        lgpio.gpio_claim_output(chip, Pin)
        lgpio.gpio_write(chip, Pin, 0)
        sleep(0.05)

        # Switch to input
        lgpio.gpio_claim_input(chip, Pin)

        # Count charge time
        while lgpio.gpio_read(chip, Pin) == 0 and counter < 5000:
            counter += 1

        light_value = counter


# animation oOoOOOOOoo
# -----------------------------

def oled_animation():
    global light_value, running
    oled = MTech_SSD1306(width=128, height=32) 

    # Load images once
    dog_frame1 = Image.open("dog.png").convert("L").rotate(180).resize((60, 30), Image.NEAREST).convert("1")
    dog_frame2 = Image.open("dog2.png").convert("L").rotate(180).resize((60, 30), Image.NEAREST).convert("1")
    
    # Invert so dog is white on black background
    dog_frame1 = ImageOps.invert(dog_frame1).convert("1")
    dog_frame2 = ImageOps.invert(dog_frame2).convert("1")
    dog_frames = [dog_frame1, dog_frame2]
    
    x_pos = -30
    
    try:
        while running:
            # 1. Select frame based on position for a synchronized walk
            current_dog = dog_frames[(x_pos // 2) % 2]

            # 2. Create a fresh black canvas
            frame = Image.new("1", (128, 32))
            frame.paste(current_dog, (x_pos, 3))
            pix = frame.load()

            # 3. Double For Loop using your new draw_pixel method
            # We use transmit=False to build the frame in the background buffer
            for y in range(32):
                for x in range(128):
                    color_val = 1 if pix[x, y] > 0 else 0
                    oled.draw_pixel(x, y, color_val, transmit=False)

            oled.show()

            # 5. SMOOTH MOVEMENT:
            x_pos += 10 
            if x_pos > 128:
                x_pos = -40

            # 6. SPEED MAPPING: (Darker = Higher light_value = Lower delay = Faster)
            # Your sensor caps at 5000. This math makes him run fast in the dark.
            delay = 0.2 - ((light_value / 5000) * 0.18)
            sleep(max(0.01, delay))

    finally:
        oled.close()


# threads
# -----------------------------
sensor_thread = threading.Thread(target=sensor)
oled_thread = threading.Thread(target=oled_animation)

sensor_thread.start()
oled_thread.start()


# keyboard
# -----------------------------
kb = Keyboard()
kb.initiation()

try:
    while True:
        bytes_data, length = kb.readKey()

        if length > 0:
            if bytes_data[0] == 27:  # ESC
                break

        sleep(0.1)

finally:
    running = False

    sensor_thread.join()
    oled_thread.join()

    kb.cleanUp()
    lgpio.gpiochip_close(chip)

    print("\rEnding Program                     ")