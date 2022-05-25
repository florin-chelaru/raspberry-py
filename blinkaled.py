import time
import board
import digitalio

print("hello blinky!")

led = digitalio.DigitalInOut(board.D21)
led.direction = digitalio.Direction.OUTPUT

led.value = True
time.sleep(2)
led.value = False
