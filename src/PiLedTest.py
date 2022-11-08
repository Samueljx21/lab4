from hal import hal_input_switch as switch
from hal import hal_led as led
from PiDemo import blink_led
from time import sleep
import time

def main():
    led.init()
    switch.init()
    t_end = time.time() + 5
    while True:

        if switch.read_slide_switch():
            t_end = time.time() + 5
            blink_led(0.2)

        else:
            while time.time() < t_end:
                blink_led(0.1)
            led.set_output(0, 0)


# Main entry point
if __name__ == "__main__":
    main()
