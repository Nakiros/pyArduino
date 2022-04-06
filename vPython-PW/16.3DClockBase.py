from vpython import*
import numpy as np
clockR = 2
clockT = clockR/10
majorTickL = clockR/7
majorTickT = 2*np.pi*clockR/400
majorTickW = clockT*1.2

minorTickL = clockR/12
minorTickT = 2*np.pi*clockR/750
minorTickW = clockT

for theta in np.linspace(0, 2*np.pi, 12, endpoint=False):
    majorTick = box(axis=vector(clockR*np.cos(theta), clockR*np.sin(theta), 0), color=color.black, length=majorTickL,
                    width=majorTickW, height=majorTickT, pos=vector((clockR-majorTickL/2)*np.cos(theta), (clockR-majorTickL/2)*np.sin(theta), majorTickW-clockT))
    for i in range(1, 5, 1):
        temp_theta = theta+2*np.pi/60*i
        minorTick = box(axis=vector(clockR*np.cos(temp_theta), clockR*np.sin(temp_theta), 0), color=color.black, length=minorTickL,
                        width=minorTickW, height=minorTickT, pos=vector((clockR-minorTickL/2)*np.cos(temp_theta), (clockR-minorTickL/2)*np.sin(temp_theta), majorTickW-clockT))


clockFace = cylinder(axis=vector(0, 0, 1),
                     color=vector(0, 1, .8), length=clockT, radius=clockR, pos=vector(0, 0, -clockT/2))
while True:
    pass
