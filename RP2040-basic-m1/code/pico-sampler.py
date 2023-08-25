import board
import digitalio
import time

lightA = digitalio.DigitalInOut(board.GP23)
lightB = digitalio.DigitalInOut(board.GP24)
lightO = digitalio.DigitalInOut(board.GP25)

lightA.direction = digitalio.Direction.OUTPUT
lightB.direction = digitalio.Direction.OUTPUT
lightO.direction = digitalio.Direction.OUTPUT

while True:
    lightA.value = True
    time.sleep(.5)
    lightB.value = True
    time.sleep(.5)
    lightO.value = True
    time.sleep(.5)
    lightA.value = False
    lightB.value = False
    lightO.value = False
    time.sleep(.5)
