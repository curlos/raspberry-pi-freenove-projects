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