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
    
# Note Board Pin lables are per chip numbers - 2, 3, 4, 5
# Which correspond to GPIO numbers - 0, 1, 2, 3
