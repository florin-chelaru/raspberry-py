import adafruit_bh1750
import time
import board
import digitalio
from adafruit_max7219 import bcddigits
from datetime import datetime
import datetime as dt

# light sensor:
# https://learn.adafruit.com/adafruit-bh1750-ambient-light-sensor/python-circuitpython
# pi -> sensor:
# 3V -> VIN
# GND -> GND
# SCL -> SCL
# SDA -> SDA
i2c = board.I2C()
sensor = adafruit_bh1750.BH1750(i2c)

# 8-digit display wiring:
# pi -> display:
# 5V -> VCC
# GND -> GND
# MOSI -> DIN
# SCLK -> CLK
# CE0 -> CS
spi = board.SPI()
cs = digitalio.DigitalInOut(board.D4)
leds = bcddigits.BCDDigits(spi, cs, nDigits=8)
leds.brightness(0)
leds.clear_all()
leds.brightness(3)

while True:
    print("%.2f Lux" % sensor.lux)
    leds.clear_all()
    str = "%.2f" % sensor.lux
    leds.show_str(0, str)
    leds.set_digit(len(str) - 1, 13)  # show L
    leds.show()
    time.sleep(0.01)
