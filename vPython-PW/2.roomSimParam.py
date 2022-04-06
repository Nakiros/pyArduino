from turtle import right
from vpython import *
from time import *

"""
ball = sphere(color=color.red)
sleep(5)
ball.color = color.blue
sleep(5)
ball.color = color.green
"""

# myBox = box(color=color.yellow)

# myBox = box(color=color.magenta, length=12, width=1, height=.2)

# myTube = cylinder(color=color.orange, length=6, radius=1)

#myTube = cylinder(color=color.orange, length=6, width=.5, height=1)

floor = box(pos=vector(0, -4.95, 0), color=color.white,
            size=vector(10, .1, 10))


ceiling = box(pos=vector(0, 4.95, 0), color=color.white,
              size=vector(10, .1, 10))

backWall = box(pos=vector(0, 0, -4.95), color=color.white,
               size=vector(9.8, 9.8, .1))

leftWall = box(pos=vector(-4.95, 0, 0), color=color.white,
               size=vector(.1, 9.8, 9.8))

rightWall = box(pos=vector(4.95, 0, 0), color=color.white,
                size=vector(.1, 9.8, 9.8))

marble = sphere(color=color.red, radius=0.75)

deltaX = .1
xPos = 0

while True:
    rate(100)
    xPos = xPos+deltaX
    marble.pos = vector(xPos, 0, 0)
    if (xPos >= 4.2) or (xPos <= -4.2):
        deltaX = deltaX*(-1)
