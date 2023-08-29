print("Hello World!")
import board
import digitalio
import time

lightA = digitalio.DigitalInOut(board.GP0)

lightA.direction = digitalio.Direction.OUTPUT

while True:
    lightA.value = True
    time.sleep(.5)
    lightA.value = False
    time.sleep(.5)
