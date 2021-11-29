# ?. Blink two LEDs with different frequencies

In this tutorial, we will study about `Multithreading`.

Running several threads is similar to running several different programs concurrently, but with the following benefits:

- Multiple threads within a process share the same data space with the main thread and can therefore share information or communicate with each other more easily than if they were separate processes.

- Threads sometimes called light-weight processes and they do not require much memory overhead; they are cheaper than processes.

Learn more about [Multithreaded Programming in Python](https://www.tutorialspoint.com/python/python_multithreading.htm).

## 1. An example of Multithreading

Consider the following source code:

```
from threading import Thread
import threading
import time


def cal_square(numbers):
	print("calculate square number")
	for n in numbers:
		time.sleep(0.2)
		print ('square:', n*n)


def cal_cube(numbers):
	print("calculate cube number \n")
	for n in numbers:
		time.sleep(0.2)
		print ('cube:', n*n*n)

arr = [2,3,7,9]

try:
	t = time.time()
	t1 = threading.Thread(target=cal_square, args=(arr,))
	t2 = threading.Thread(target=cal_cube, args=(arr,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	print ("done in ", time.time()- t)
except:
	print ("error")
```

Result:
```
calculate square number
calculate cube number 

square: 4
cube: 8
square: 9
cube: 27
square: 49
cube: 343
square: 81
cube: 729
done in  0.8020298480987549
```







