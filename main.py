import adafruit_rgbled
import time

RED_LED = 17
GREEN_LED = 27
BLUE_LED = 22

# Create a RGB LED object
led = adafruit_rgbled.RGBLED(RED_LED, BLUE_LED, GREEN_LED)
led.color = (255, 0, 0)
time.sleep(3);
led.color = (0, 255, 0)
time.sleep(3);
led.color = (0, 0, 255)