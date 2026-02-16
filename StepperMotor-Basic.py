from machine import Pin
import time

in1 = Pin(5,Pin.OUT)
in2 = Pin(12,Pin.OUT)
in3 = Pin(25,Pin.OUT)
in4 = Pin(19,Pin.OUT)

while True:
    in1.value(1)
    in2.value(0)
    in3.value(0)
    in4.value(0)
    time.sleep(0.005)
    
    in1.value(0)
    in2.value(1)
    in3.value(0)
    in4.value(0)
    time.sleep(0.005)
    
    in1.value(0)
    in2.value(0)
    in3.value(1)
    in4.value(0)
    time.sleep(0.005)
    
    in1.value(0)
    in2.value(0)
    in3.value(0)
    in4.value(1)
    time.sleep(0.005)
