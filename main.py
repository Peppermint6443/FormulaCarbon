from machine import Pin
import time

led = Pin(15, Pin.OUT)  # GPIO15 is the user LED on XIAO ESP32-C6
led2 = Pin(20, Pin.OUT)  # GPIO20 is the user LED on XIAO ESP32-C6

while True:
    led.on()
    led2.off()
    time.sleep(1)
    led.off()
    led2.on()
    time.sleep(1)


# from machine import Pin
# import time

# led = Pin(20, Pin.OUT)

# while True:
#     led.value(1)
#     print("LED ON")
#     time.sleep(0.5)
#     led.value(0)
#     print("LED OFF")
#     time.sleep(0.5)