# Import necessary modules
import threading
import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
pins = [26, 19]
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)
    # GPIO.output(pin,1)

# # Set variables (change these to change behaviour as desired)
# runcycles = 2
# ontime = 45 # minutes
# offtime = 20 #  minutes

# # Convert run times from minutes to seconds for sleep function
# ontime *= 60
# offtime *= 60

# # Run furnace on cycle
# cycle = 0

def blink_LED(pin, freq):
    while True:
        GPIO.output(pin,1)
        time.sleep(1/(freq*2))
        GPIO.output(pin,0)
        time.sleep(1/(freq*2))


try:
    t1 = threading.Thread(target=blink_LED, args=(26,1,))
    t2 = threading.Thread(target=blink_LED, args=(19,10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    while True:
        pass

except KeyboardInterrupt: # if Ctrl C is pressed...
    pass
GPIO.cleanup()
