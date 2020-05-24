from time import sleep
from gpiozero import *
water_sensor = GPIODevice(23)

while True:
  print(water_sensor.value)
  print(is_active)
  sleep(1)