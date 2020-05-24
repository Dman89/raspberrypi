from gpiozero import RGBLED
from time import sleep
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT11

# Configure
DHT_PIN = 4
RGBLED_RED = 17
RGBLED_GREEN = 27
RGBLED_BLUE = 22

 
led = RGBLED(red = RGBLED_RED, green = RGBLED_GREEN, blue = RGBLED_BLUE)

# led.color = (1, 0, 0)
# sleep(0.5)
# led.color = (0, 1, 0)
# sleep(0.5)
# led.color = (0, 0, 1)
# sleep(0.5)
# led.color = (0, 0, 0)


 
while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    print(temperature)
    if humidity is not None and temperature is not None:
        faren = (temperature * (9/5)) + 32;
        print("Temp={0:0.1f}F ({1:0.1f}C) Humidity={2:0.1f}%".format(faren, temperature, humidity))
        setColor(faren)
    else:
        print("Sensor failure. Check wiring.");
        setColor(76)
    sleep(3);


def setColor(faren):
    if faren == 76:
            led.color = (0, 1, 0)
    else if faren >= 76:
        led.color = (1, 0, 0)
    else if faren <= 76:
        led.color = (0, 0, 1)