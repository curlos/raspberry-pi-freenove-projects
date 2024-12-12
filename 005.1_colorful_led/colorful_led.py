'''
FILE NAME: colorful_led.py
DESCRIPTION: Changes the value of an RGB LED to a random color every 0.5 seconds. The RGB LED must be connected on a Raspberry Pi with the configuration described below for the pins (17, 18, 27).
USAGE: "python colorful_led.py"
'''

# Imports
from gpiozero import RGBLED
from time import sleep
from random import randint

# Red = GPIO17, Green = GPIO18, Blue = GPIO27, active_high = False because in the freenove kit, the provided RGB LED is a common anode (meaning we have three cathodes for RGB in 3 pins, and 1 pin that these cathodes share which is an anode ("+"))
# If the physical RGBLED you have is a common cathode LED, set "active_high" to True
led = RGBLED(red = 17, green = 18, blue = 27, active_high = False)

def set_led_random_color():
    '''
    Change the 3 RGB values to a random number between 0 and 1.
    '''

    # Generate a random number between 0 and 100 for red, green, and blue.
    red_val = randint(0, 100)
    green_val = randint(0, 100)
    blue_val = randint(0, 100)

    # Set the LED's RGB values to the value above divided by 100. This needs to be divided by 100 because the RGBLED class from GPIOZero ONLY accepts values between 0 and 1 (like 0.56 or something).
    led.red = red_val / 100
    led.green = green_val / 100
    led.blue = blue_val / 100

    print(f'red = {red_val}, green = {green_val}, blue = {blue_val}')

def change_to_random_color_loop():
    '''
    Change the RGB value to a random color every 0.5 seconds infinitely.
    '''
    while True:
        set_led_random_color()
        sleep(0.5)

def destroy():
    '''
    Cleanup after the program is done using RGB LED.
    '''
    led.close()

is_running_as_main_program = (__name__ == '__main__')

if is_running_as_main_program:
    print('Program is starting...')

    try:
        change_to_random_color_loop()
    except KeyboardInterrupt:
        destroy()
        print('Ending program!')