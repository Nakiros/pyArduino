from vpython import*
import numpy as np
import time

clockR = 8
clockT = clockR/10
majorTickL = clockR/7
majorTickT = 2*np.pi*clockR/400
majorTickW = clockT*1.2

minorTickL = clockR/12
minorTickT = 2*np.pi*clockR/750
minorTickW = clockT

secondHandL = clockR-minorTickL
secondHandT = secondHandL/25
secondHandOffset = clockT/1.1

minuteHandL = secondHandL*.75
#minuteHandL = secondHandL
minuteHandT = secondHandT*1.5
minuteHandOffset = secondHandOffset+minuteHandT

hourHandL = secondHandL*.5
#hourHandL = secondHandL
hourHandT = minuteHandT*1.25
hourHandOffset = minuteHandOffset+hourHandT


"""hourAngle = np.pi/2
minuteAngle = np.pi/2
secondAngle = np.pi/2

secInc = .0022
minInc = secInc/60
hourInc = minInc/60"""


for theta in np.linspace(0, 2*np.pi, 12, endpoint=False):
    majorTick = box(axis=vector(clockR*np.cos(theta), clockR*np.sin(theta), 0), color=color.black, length=majorTickL,
                    width=majorTickW, height=majorTickT, pos=vector((clockR-majorTickL/2)*np.cos(theta), (clockR-majorTickL/2)*np.sin(theta), majorTickW-clockT))
    for i in range(1, 5, 1):
        temp_theta = theta+2*np.pi/60*i
        minorTick = box(axis=vector(clockR*np.cos(temp_theta), clockR*np.sin(temp_theta), 0), color=color.black, length=minorTickL,
                        width=minorTickW, height=minorTickT, pos=vector((clockR-minorTickL/2)*np.cos(temp_theta), (clockR-minorTickL/2)*np.sin(temp_theta), majorTickW-clockT))

clockFace = cylinder(axis=vector(0, 0, 1),
                     color=vector(0, 1, .8), length=clockT, radius=clockR, pos=vector(0, 0, -clockT/2))

secondHand = arrow(axis=vector(0, 1, 0), color=color.red,
                   shaftwidth=secondHandT, length=secondHandL, pos=vector(0, 0, secondHandOffset))
minuteHand = arrow(axis=vector(0, 1, 0), color=color.red,
                   shaftwidth=minuteHandT, length=minuteHandL, pos=vector(0, 0, minuteHandOffset))
hourHand = arrow(axis=vector(0, 1, 0), color=color.red,
                 shaftwidth=hourHandT, length=hourHandL, pos=vector(0, 0, hourHandOffset))
clockHub = cylinder(axis=vector(0, 0, 1), color=color.red, radius=hourHandT/1.75,
                    length=hourHandOffset, pos=vector(0, 0, clockT/2))
textH = clockR/4
myLabel = text(text='Timp Bucuresti', align='center',
               color=color.blue, height=textH, pos=vector(0, 1.1*clockR, -clockT/2), depth=clockT)
Angle = np.pi/2
AngleInc = -2*np.pi/12
Angle = Angle+AngleInc
numH = clockR/6
for i in range(1, 13, 1):
    clockNum = text(align='center', text=str(i), color=color.blue, pos=vector(
        clockR*0.75*np.cos(Angle), clockR*0.75*np.sin(Angle)-numH/2, 0), height=numH, depth=clockT)
    Angle = Angle+AngleInc
while True:
    rate(5000)

    hour = time.localtime(time.time())[3]
    if hour > 12:
        hour = hour-12
    minute = time.localtime(time.time())[4]
    second = time.localtime(time.time())[5]

    """hour = 1
    minute = 30
    second = 30"""
    hourAngle = -((hour+minute/60)/12)*2*np.pi+np.pi/2
    minuteAngle = -((minute+second/60)/60)*2*np.pi+np.pi/2
    secondAngle = -(second/60)*2*np.pi+np.pi/2
    print(str(hour)+':'+str(minute)+':'+str(second))

    hourHand.axis = vector(hourHandL*np.cos(hourAngle),
                           hourHandL*np.sin(hourAngle), 0)
    minuteHand.axis = vector(
        minuteHandL*np.cos(minuteAngle), minuteHandL*np.sin(minuteAngle), 0)
    secondHand.axis = vector(secondHandL*np.cos(secondAngle),
                             secondHandL*np.sin(secondAngle), 0)
