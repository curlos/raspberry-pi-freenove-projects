'''
FILE NAME: table_lamp.py
DESCRIPTION: When you press the connected button, toggle the LED state to be on or off. If the LED is turned ON, then pressing the button will turn it OFF. If the LED is turned OFF, then pressing the button will turn it OFF. Unlike the "button_led.py" module above this, the button only needs to be pressed once for the state to change and remain in that state. So, if you press the button to turn on the LED, you can let go and the LED will continue to be ON.
USAGE: "python table_lamp.py"
'''

# Imports
from gpiozero import LED, Button
import time

led = LED(17)
button = Button(23)

def on_button_pressed():
    led.toggle()

    if led.is_lit:
        print("LED turned on!")
    else:
        print("LED turned off!")

def loop():
    button.when_pressed = on_button_pressed

    while True:
        time.sleep(1)

def destroy():
    '''
    Reset the state of the two pins connected to the LED and the Button. In this case, reset pins "GPIO17" and "GPIO23".
    '''
    led.close()
    button.close()

is_running_as_main_program = (__name__ == '__main__')

if is_running_as_main_program:
    print('Program is starting...')

    try:
        loop()
    except KeyboardInterrupt:
        destroy()
        print('Ending program')
