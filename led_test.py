from machine import Pin
import time

led = Pin(20, Pin.OUT)

while True:
    led.value(1)
    print("LED ON")
    time.sleep(0.5)
    led.value(0)
    print("LED OFF")
    time.sleep(0.5)