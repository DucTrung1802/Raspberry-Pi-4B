# Import necessary modules
import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# pins = [26]
# for pin in pins:
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26,GPIO.OUT)
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
GPIO.output(26,0)
i = 0

try:
    while True:
        # if GPIO.input(19):
        #     print('Input was HIGH')
        # # while GPIO.input(19) == GPIO.LOW:
        # #     time.sleep(0.01)  # wait 10 ms to give CPU chance to do other things
        if GPIO.input(19):
            GPIO.output(26,1)
        else:
            GPIO.output(26,0)
        time.sleep(0.01)
        print(i)
        i += 1
    
except KeyboardInterrupt: # if Ctrl C is pressed...
    pass
    # GPIO.output(26,0) # shut off the boiler
    # print("Program stopped and furnace shut off.") # print a clean exit message
GPIO.cleanup()
