# 1. Blink LED 

Blinking LED in embedded is considered as running "Hello World" in programming

## 1. Breadborad

![Breadboard](Wiring/1-blink-LED-bb.png)

## 2. Schematic

![Schematic](Wiring/1-blink-LED_schem.png)

## 3. Source code

```
import RPi.GPIO as GPIO
import time

HIGH = True
LOW = False

GPIO.setmode(GPIO.BCM)

pins = [26]
for pin in pins:
    GPIO.setup(pin,GPIO.OUT)

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
```

## 4. Explanation

### 4.1 Import necessary modules

```
import RPi.GPIO as GPIO
```

### 4.2 Setup type of GPIO pins

- GPIO.BCM option is considering number of pins as numbers of GPIO.
```
GPIO.setmode(GPIO.BCM)
```

- GPIO.BOARD option is considering number of pins as numbers of plug pins (in the red frame). 
```
GPIO.setmode(GPIO.BOARD)
```

![Pins of Pi 4B](Images/1_Blink_LED_Pins_of_Pi_4B.png)

### 4.3 Setup mode Input/Output for pins

Syntax:
```
GPIO.setup(pin,GPIO.OUT)
```

<!-- No PUD_UP -->












