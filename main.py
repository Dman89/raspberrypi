from gpiozero import *
water_sensor = GPIODevice(23)

print(water_sensor.value)