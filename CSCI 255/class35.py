'''
Madison Grace Austin
CSCI 255 Spring 2025
Programming Assignment # class35

I acknowledge that I have worked on this assignment independently, except where
explicitly noted and referenced. Any collaboration or use of external resources has been
properly cited. I am fully aware of the consequences of academic dishonesty and agree to abide by
the university's academic integrity policy.
'''

import lgpio
from time import sleep
from MTECH_SSD1306 import MTech_SSD1306 as OLED

# ---------------- GPIO ----------------
clk = 12
dt = 20
sw = 21

h = lgpio.gpiochip_open(0)

lgpio.gpio_claim_input(h, clk)
lgpio.gpio_claim_input(h, dt)
lgpio.gpio_claim_input(h, sw, lgpio.SET_PULL_UP)

last_encoded = 0
sw_last_state = lgpio.HIGH

# ---------------- OLED ----------------
oled = OLED()
oled.clear_screen()

# ---------------- GAME VARIABLES ----------------
paddle_y = 12
ball_x = 20
ball_y = 16
dx = 1
dy = 1

game_running = False

# ---------------- DRAW FUNCTIONS ----------------
def draw_border():
    for x in range(128):
        oled.set_pixel(x, 0, 1)
        oled.set_pixel(x, 31, 1)
    for y in range(32):
        oled.set_pixel(0, y, 1)
        oled.set_pixel(127, y, 1)

def draw_paddle(y):
    for py in range(y, y + 8):
        for px in range(2, 4):
            oled.set_pixel(px, py, 1)

def erase_paddle(y):
    for py in range(y, y + 8):
        for px in range(2, 4):
            oled.set_pixel(px, py, 0)

def draw_ball(x, y):
    for bx in range(x, x + 2):
        for by in range(y, y + 2):
            oled.set_pixel(bx, by, 1)

def erase_ball(x, y):
    for bx in range(x, x + 2):
        for by in range(y, y + 2):
            oled.set_pixel(bx, by, 0)

# --- New Global Variables for the Encoder ---
last_state_clk = 0

def encoder_callback(chip, gpio, level, tick):
    global paddle_y, last_state_clk
    
    # Read the current state of both pins
    clk_state = lgpio.gpio_read(h, clk)
    dt_state = lgpio.gpio_read(h, dt)
    
    # We only care when the CLK pin changes (Transition)
    if clk_state != last_state_clk:
        # If CLK is different from DT, it's rotating one way
        # If they are the same, it's rotating the other
        if clk_state != dt_state:
            paddle_y -= 1
        else:
            paddle_y += 1
        
        # Keep paddle within OLED bounds
        paddle_y = max(1, min(23, paddle_y))
        
    last_state_clk = clk_state

# --- Setup the Callback ---
# This tells lgpio to run 'encoder_callback' whenever CLK (12) changes
lgpio.gpio_claim_alert(h, clk, lgpio.BOTH_EDGES)
lgpio.callback(h, clk, lgpio.BOTH_EDGES, encoder_callback)


# ---------------- INITIAL DRAW ----------------
draw_border()
draw_paddle(paddle_y)
draw_ball(ball_x, ball_y)
# ---------------- INITIAL STATES ----------------
last_encoded = ((lgpio.gpio_read(h, dt) << 1) | lgpio.gpio_read(h, clk))


# ---------------- MAIN LOOP ----------------
try:
    old_paddle_y = paddle_y
    
    while True:
        # Check if we need to update the paddle on the screen
        if paddle_y != old_paddle_y:
            erase_paddle(old_paddle_y)
            draw_paddle(paddle_y)
            old_paddle_y = paddle_y

        # Handle Button
        sw_state = lgpio.gpio_read(h, sw)
        if sw_state == lgpio.LOW and sw_last_state == lgpio.HIGH:
            game_running = not game_running
            sleep(0.2) 
        sw_last_state = sw_state

        # Ball Logic
        if game_running:
            oled.show()

        sleep(0.01) 

        # ---------------- CLAMP + DRAW ----------------
        paddle_y = max(1, min(23, paddle_y))

        if paddle_y != old_paddle_y:
            erase_paddle(old_paddle_y)
            draw_paddle(paddle_y)
        #  Clamp and Redraw Paddle
        paddle_y = max(1, min(23, paddle_y))
        
        if paddle_y != old_paddle_y:
            erase_paddle(old_paddle_y)
            draw_paddle(paddle_y)

        #  Button Logic
        sw_state = lgpio.gpio_read(h, sw)
        if sw_state == lgpio.LOW and sw_last_state == lgpio.HIGH:
            game_running = not game_running
            sleep(0.1) 
        sw_last_state = sw_state

        #  Ball Logic
        if game_running:
            old_ball_x, old_ball_y = ball_x, ball_y
            ball_x += dx
            ball_y += dy

            # Collisions
            if ball_y <= 1 or ball_y >= 29: dy *= -1
            if ball_x >= 125: dx *= -1
            if 2 <= ball_x <= 4 and paddle_y <= ball_y <= paddle_y + 8:
                dx *= -1

            # Reset on Miss
            if ball_x <= 1:
                game_running = False
                erase_ball(ball_x, ball_y) # Clear the ball where it died
                ball_x, ball_y = 20, 16
                draw_ball(ball_x, ball_y)
                #oled.show()

            erase_ball(old_ball_x, old_ball_y)
            draw_ball(ball_x, ball_y)
            #oled.show()

        sleep(0.001)

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    oled.close()
    lgpio.gpiochip_close(h)
    print("Clean exit")