import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

p = GPIO.PWM(26, 50)  # channel=12 frequency=50Hz
p.start(0)
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
            print(round(time.time() * 1000))
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.output(26,0) # shut off the boiler
    print("Program stopped and furnace shut off.") # print a clean exit message
p.stop()
GPIO.cleanup()