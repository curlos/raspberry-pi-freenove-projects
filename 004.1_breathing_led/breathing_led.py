'''
FILE NAME: breathing_led.py
DESCRIPTION: When an LED is connected to a PWM PIN (GPIO18), gradually increase the brightness from 0 to 100, wait 1 second, and then, gradually decrease the brightness from 100 to 0. Repeat this forever.
USAGE: "python breathing_led.py"
'''

# Imports
from gpiozero import PWMLED
import time

# Use GPIO18 pin, initially set the brightness to the lowest (0), and a frequency of 1000hz.
# A higher frequency like 1000hz will make the transitions extremely smooth and there'll be little to no flicker. Sort of like the frequency on a monitor. A 30hz monitor will not be anywhere near as smooth as a 144hz monitor due to a higher refresh rate.
led = PWMLED(18, initial_value=0, frequency=1000)

def gradually_increase_and_decrease_led_brightness():
    '''
    Gradually increase and decrease the brightness of the LED connected to GPIO18 forever.
    '''
    while True:
        # Gradually INCREASE the LED's brightness from 0 to 100 over a second.
        for b in range(0, 101, 1):
            led.value = b / 100.0
            time.sleep(0.01)
        
        # Once we've reached the max brightness (100), wait for a second before turning it back down to 0 brightness.
        time.sleep(1)

        # Gradually DECREASE the LED's brightness from 100 to 0 over a second.
        for b in range(100, -1, -1):
            led.value = b / 100.0
            time.sleep(0.01)
        
        # Once we've reached the lowest brightness (0), wait for a second before restarting the loop.
        time.sleep(1)



def destroy():
    led.close()

is_running_as_main_program = (__name__ == '__main__')

if is_running_as_main_program:
    print('Program is starting...')

    try:
        gradually_increase_and_decrease_led_brightness()
    except KeyboardInterrupt:
        destroy()
        print('Ending program!')