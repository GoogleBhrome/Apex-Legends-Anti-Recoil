
import pyautogui
import time
import win32api
import random
import keyboard

## Configuration
# Set the horizontal limit: 5 means a maximum of 5 pixels to the left or to the right every shot
horizontal_range = 1
# Set the minimum and maximum amount of pixels to move the mouse every shot
min_vertical = 1
max_vertical = 3
# Set the minimum and maximum amount of time in seconds to wait until moving the mouse again
min_firerate = 0.03
max_firerate = 0.05
# Set the toggle button
toggle_button = 'num lock'
# Set whether the anti-recoil is enabled by default
enabled = False

def is_mouse_down():    # Returns true if the left mouse button is pressed
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0

# Some prints for startup
print("Anti-recoil script started!")
if enabled:
    print("Currently ENABLED")
else:
    print("Currently DISABLED")

last_state = False
while True:
    key_down = keyboard.is_pressed(toggle_button)
    # If the toggle button is pressed, toggle the enabled value and print
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print("Anti-recoil ENABLED")
            else:
                print("Anti-recoil DISABLED")
    
    if is_mouse_down() and enabled:
        # Offsets are generated every shot between the min and max config settings
        offset_const = 1000
        horizontal_offset = random.randrange(-horizontal_range * offset_const, horizontal_range * offset_const, 1) / offset_const
        vertical_offset = random.randrange(min_vertical * offset_const, max_vertical * offset_const, 1) / offset_const

        # Move the mouse with these offsets
        win32api.mouse_event(0x0001, int(horizontal_offset), int(vertical_offset))

        # Generate random time offset with the config settings
        time_offset = random.randrange(min_firerate * offset_const, max_firerate * offset_const, 1) / offset_const
        time.sleep(time_offset)
    # Delay for the while loop
    time.sleep(0.001)
