# Import necessary modules
import RPi.GPIO as GPIO
import time

HIGH = True
LOW = False

LED = 26
BUTTON = 19

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)

# pull_up_down=GPIO.PUD_DOWN or pull_up_down=GPIO.PUD_UP
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(LED,GPIO.OUT)

def setup():
    # setup somthing (do 1 time)
    global i
    i = 0
    GPIO.output(LED,LOW)
    

def loop():
    # continuously do something
    global i, LED, BUTTON
    
    try:
        while True:
            # Read button state
            if GPIO.input(BUTTON):
                GPIO.output(LED,HIGH)
            else:
                GPIO.output(LED,LOW)
            
            # wait 10 ms to give CPU chance to do other things
            time.sleep(0.01)
            print(i)
            i += 1

    except KeyboardInterrupt: # if Ctrl C is pressed...
        print("Program stopped and furnace shut off.") # print a clean exit message
    GPIO.cleanup()


def main():
    setup()
    loop()

if __name__ == '__main__':
    main()