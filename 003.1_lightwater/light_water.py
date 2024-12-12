'''
FILE NAME: light_water.py
DESCRIPTION: When an LED Bar Graph is connected, all the LEDs will be turned off in the start and then when this is run, this will go through the row of 10 LEDs and turn them on and off from left to right and then turn them on and off from right to left forever.
USAGE: "python light_water.py"
'''

# Imports
from gpiozero import LED
from time import sleep

# The schematic diagram from Freenove wanted the 4th LED to be connected to GPIO22 however for some reason this LED would be lit up by default before the code ran. I don't know why and I assume it's left over voltage or something so not 100% sure. In any case, I used GPIO5 instead for the 4th LED (5).
led_pin_numbers = [17, 18, 27, 5, 23, 24, 25, 2, 3, 8]

# Intialize the LEDs with an intiial value of "True". This will TURN ON all the LEDs by default. This is necessary so that the LEDs DO NOT light up from the start because in the circuit the GPIO pins are connected to the cathode ("-"), not the anode ("+") so it's working through an inverse setup. Meaning for the LEDs to be off by default, we need to set the output to HIGH.
# Without this, it will intiially be turned "off" (output set to LOW) which will show the LEDs with the light on due to the inverse cathode connection setup.
leds = [LED(pin=pin_number, initial_value=True) for pin_number in led_pin_numbers]

def blinkRowOfLEDs():
    '''
    The schematic diagram is designed in such a way that in this circuit, the cathodes ("-", the negative) of the LEDs are connected to the GPIO pins, which is different from the previous circuit where the ANODES ("+") where connected to the GPIO pins. This is the inverse of normal behavior. This means that LEDs turn ON when the GPIO output is set to LOW level in the program.

    - IMPORTANT: "led.on()" will TURN OFF the LED because that sets it to HIGH level output.
    - IMPORTANT: "led.off()" will TURN ON the LED because that sets it to a LOW level output.
    '''

    while True:
        # From left to right, turn on and off the individual LEDs.
        for i in range(0, len(leds), 1):
            leds[i].off()
            sleep(0.1)
            leds[i].on()
        
        # From right to left, turn on and off the individual LEDs
        for i in range(len(leds) - 1, -1, -1):
            leds[i].off()
            sleep(0.1)
            leds[i].on()

is_running_as_main_program = (__name__ == '__main__')

if is_running_as_main_program:
    print('Program is starting...')

    try:
        blinkRowOfLEDs()
    except KeyboardInterrupt:
        print('Ending program!')
    finally:
        for i in range(0, len(leds)):
            leds[i].close()