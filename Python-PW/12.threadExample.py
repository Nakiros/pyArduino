"""
from time import *
while True:
    print('My box is open: ')
    sleep(5)
    print('My box is closed: ')
    sleep(5)
    print('My LED is ON: ')
    sleep(1)
    print('My LED is OFF: ')
    sleep(1)
"""

from time import *
from threading import Thread


def myBox(delayT):
    while True:
        print('................................My box is OPEN')
        sleep(delayT)
        print('................................My box is CLOSED')
        sleep(delayT)


def myLED(delayT):
    while True:
        print('My LED is ON')
        sleep(delayT)
        print('My LED is OFF')
        sleep(delayT)


delayBox = 5
delayLED = 1

boxThread = Thread(target=myBox, args=(delayBox,))
LEDThread = Thread(target=myLED, args=(delayLED,))
boxThread.daemon = True
LEDThread.daemon = True
boxThread.start()
LEDThread.start()
j = 0
while True:
    print(j)
    j += 1
    sleep(.1)
