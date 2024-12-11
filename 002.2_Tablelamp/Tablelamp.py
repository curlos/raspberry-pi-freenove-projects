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
