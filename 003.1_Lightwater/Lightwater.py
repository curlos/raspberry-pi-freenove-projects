from gpiozero import LED
from time import sleep

led_pin_numbers = [17, 18, 27, 22, 23, 24, 25, 2, 3, 8]

# Intialize the LEDs with an intiial value of "True". This will TURN ON all the LEDs by default. This is necessary so that the LEDs DO NOT light up from the start because in the circuit the GPIO pins are connected to the cathode ("-"), not the anode ("+") so it's working through an inverse setup. Meaning for the LEDs to be off by default, we need to set the output to HIGH.
# Without this, it will intiially be turned "off" (output set to LOW) which will show the LEDs with the light on due to the inverse cathode connection setup.
leds = [LED(pin=pin_number, initial_value=True) for pin_number in led_pin_numbers]

def blinkRowOfLEDs():
    '''
    The schematic diagram is designed in such a way that in this circuit, the cathodes ("-", the negative) of the LEDs are connected to the GPIO pins, which is different from the previous circuit where the ANODES ("+") where connected to the GPIO pins. This is the inverse of normal behavior. This means that LEDs turn ON when the GPIO output is set to LOW level in the program.

    - "led.on()" will TURN OFF the LED because that sets it to HIGH level output.
    - "led.off()" will TURN ON the LED because that sets it to a LOW level output.
    '''

    while True:
        # From left to right, turn on and off the individual LEDs.
        for i in range(0, len(leds), 1):
            leds[i].off() # Set LOW, LED turns ON
            sleep(0.1)
            leds[i].on() # Set HIGH, LED turns OFF
        
        # From right to left, turn on and off the individual LEDs
        for i in range(len(leds) - 1, -1, -1):
            leds[i].off() # Set LOW, LED turns ON
            sleep(0.1)
            leds[i].on() # Set HIGH, LED turns OFF

is_running_as_main_program = (__name__ == '__main__')

if is_running_as_main_program:
    print('Program is starting...')

    try:
        for led in leds:
            led.on()

        blinkRowOfLEDs()
    except KeyboardInterrupt:
        print('Ending program!')
    finally:
        for i in range(0, len(leds)):
            leds[i].close()