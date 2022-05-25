import time
import random
import board
import digitalio
from adafruit_max7219 import bcddigits
from datetime import datetime
import datetime as dt

spi = board.SPI()
cs = digitalio.DigitalInOut(board.D4)

leds = bcddigits.BCDDigits(spi, cs, nDigits=8)

leds.brightness(0)
leds.clear_all()
leds.brightness(3)

# Show time
# while True:
#     now = datetime.now()
#     current_time = now.strftime("%H.%M.%S.%f")
#     # print(current_time)
#     leds.show_str(0, current_time)
#     leds.show()
#     time.sleep(0.01)

# Countdown

helper_date = dt.date(1, 1, 1)
t = dt.time(0, 1, 0)  # 10 minutes
time_str = t.strftime("%H.%M.%S.%f")
print(time_str)
leds.show_str(0, time_str)
leds.show()

zero = dt.time(0, 0, 0)

now = datetime.now()

while t > zero:
    last = now
    now = datetime.now()
    d = now - last

    t = (datetime.combine(helper_date, t) - d).time()
    time_str = t.strftime("%H.%M.%S.%f")
    # print(time_str)
    leds.show_str(0, time_str)
    leds.show()
    time.sleep(0.01)
