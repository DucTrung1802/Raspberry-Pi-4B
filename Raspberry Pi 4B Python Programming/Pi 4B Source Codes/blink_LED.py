# Import necessary modules
import RPi.GPIO as GPIO
import time

HIGH = True
LOW = False

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)

pins = [26]
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)

def setup():
    pass
    # setup somthing

def loop():
    try:
        while True:
            GPIO.output(26,HIGH)
            time.sleep(0.5)
            GPIO.output(26,LOW)
            time.sleep(0.5)

    except KeyboardInterrupt: # if Ctrl C is pressed...
        for pin in pins:
            GPIO.output(pin,LOW)
        # print("Program stopped and furnace shut off.") # print a clean exit message
    GPIO.cleanup()


def main():
    setup()
    loop()

if __name__ == '__main__':
    main()


