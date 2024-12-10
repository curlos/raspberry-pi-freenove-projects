from gpiozero import LED
from time import sleep

led = LED("GPIO27")

def blinkEveryX(sleep_time):
    '''
    Infinitely turn the LED on and off every "sleep_time" seconds until manually stopped by the user.

    Parameters:
    sleep_time (float or int): Number of seconds the LED remains in each state (on or off).
    '''
    while True:
        # Turn it on
        led.on()
        print('LED turned on >>>')
        sleep(sleep_time)

        # Turn it off
        led.off()
        print('LED turned off <<<')
        sleep(sleep_time)

is_running_as_main_program = (__name__ == '__main__')

if (is_running_as_main_program):
    print("Program is starting...\n")
    
    try:
        blinkEveryX(0.1)
    except KeyboardInterrupt:
        print("Ending Program")