from gpiozero import RGBLED
from time import sleep
import Adafruit_DHT

# Configure
DHT_PIN = 4
RGBLED_RED = 27
RGBLED_GREEN = 17
RGBLED_BLUE = 22

 
DHT_SENSOR = Adafruit_DHT.DHT11
led = RGBLED(red = RGBLED_RED, green = RGBLED_GREEN, blue = RGBLED_BLUE)

led.color = (1, 0, 0)
sleep(0.5)
led.color = (0, 1, 0)
sleep(0.5)
led.color = (0, 0, 1)
sleep(0.5)

# led.color = (0, 1, 0)  # full green
# sleep(1.5)
# led.color = (1, 0, 1)  # magenta
# sleep(1.5)
# led.color = (1, 1, 0)  # yellow
# sleep(1.5)
# led.color = (0, 1, 1)  # cyan
# sleep(1.5)
# led.color = (1, 1, 1)  # white
# sleep(1.5)


 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        faren = (temperature * (9/5)) + 32;
        print("Temp={0:0.1f}F ({1:0.1f}C) Humidity={2:0.1f}%".format(faren, temperature, humidity))
        if faren >= 76:
            led.color = (0, 1, 0)
    else:
        print("Sensor failure. Check wiring.");
    sleep(3);