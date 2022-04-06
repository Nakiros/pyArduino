from vpython import*
import numpy as np


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


thermoLength = 8
thermoPosX = -thermoLength/2
tMax = 50
tMin = -20
mercColor = vector(255, 0, 0)
glassCyl = cylinder(radius=.65, length=thermoLength+0.1, color=color.white,
                    opacity=.3, up=vector(-1, 0, 0), pos=vector(0, thermoPosX, 0))
glassBulb = sphere(radius=1.25, color=color.white,
                   opacity=.3, pos=vector(0, thermoPosX, 0))
mercCyl = cylinder(radius=.45, length=thermoLength,
                   color=mercColor, up=vector(-1, 0, 0), pos=vector(0, thermoPosX, 0))
mercBulb = sphere(radius=1, color=mercColor, pos=vector(0, thermoPosX, 0))
"""box(size=vector(.05, .05, .25), color=color.white,
    pos=vector(-glassCyl.radius+.05/2, thermoPosX+1, 0))"""

for tick in np.linspace(1, thermoLength, 35):
    box(size=vector(.05, .05, .25), color=color.white,
        pos=vector(-glassCyl.radius+.05/2, thermoPosX+tick, 0))

while True:
    temp_input = float(input('Please input temperature: '))
    mercCyl.length = map(temp_input, -20, 50, 1, 8)
    if temp_input < -20:
        mercCyl.up = vector(1, 0, 0)
    if temp_input > -20:
        mercCyl.up = vector(-1, 0, 0)

    print(mercCyl.length)
    if temp_input >= 28:
        mercBulb.color = color.red
        mercCyl.color = color.red
    if (temp_input < 28) and (temp_input >= 20):
        mercBulb.color = color.green
        mercCyl.color = color.green
    if (temp_input < 20) and (temp_input >= 10):
        mercBulb.color = vector(0, 191, 255)
        mercCyl.color = vector(0, 191, 255)
    if (temp_input < 10) and (temp_input >= 0):
        mercBulb.color = color.blue
        mercCyl.color = color.blue
    if temp_input < 0:
        mercBulb.color = vector(100, 10, 100)
        mercCyl.color = vector(100, 10, 100)
