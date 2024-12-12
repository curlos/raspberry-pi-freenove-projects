'''
FILE NAME: button_led.py
DESCRIPTION: By default the LED is turned OFF. When the connected button is PRESSED, the LED will remain on for as long as the button is continued to be pressed. As soon as the button is NOT PRESSED, the LED will turn OFF. 
USAGE: "python button_led.py"
'''

# Imports
from gpiozero import LED, Button

led = LED(17)
button = Button(23)

def buttonLED():
    while True:
        if button.is_pressed:
            led.on()
            print("Button is pressed, LED turned on!")
        else:
            led.off()
            print("Button is released, LED turned off!")

is_running_as_main_program = (__name__ == '__main__')

if (is_running_as_main_program):
    print("Program is starting...\n")
    
    try:
        buttonLED()
    except KeyboardInterrupt:
        print("Ending Program")