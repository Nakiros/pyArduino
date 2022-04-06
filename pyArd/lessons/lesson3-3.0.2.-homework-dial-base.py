from vpython import*
import numpy as np


def mapValue(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrainValue(cVal, lowB, uppB):
    return max(lowB, min(uppB,cVal))

bgLength=20
bgHeight=10
radDisperse=bgLength/2
bgThick=.5
majorTickW=.1
majorTickL=1
majorTickT=.2

minorTickW=majorTickW/2
minorTickT=majorTickT/2
minorTickL=majorTickL/2
bgBox=box(pos=vector(0,bgHeight/2,-bgThick/2), size=vector(bgLength,bgHeight,bgThick))
arrowL=radDisperse-majorTickL
#mySphere=sphere(pos=vector(0,0,0.5), size=vector(1,1,1))
#myDisc=cylinder(pos=vector(0,0,0), radius=bgLength/2, length=1, color=color.red, axis=vector(0,0,1))
for theta in np.linspace(0,np.pi,7):
    majorTick=box(axis=vector(radDisperse*np.cos(theta), radDisperse*np.sin(theta), 0), color=color.blue, length=majorTickL,
                    width=majorTickW, height=majorTickT, pos=vector((radDisperse-majorTickL/2-majorTickT/2)*np.cos(theta), (radDisperse-majorTickL/2-majorTickT/2)*np.sin(theta)+majorTickT/2, majorTickW/2))
    if theta!=np.pi:
        for i in range(1, 10, 1):
            temp_theta = theta+np.pi/60*i
            minorTick = box(axis=vector(radDisperse*np.cos(temp_theta), radDisperse*np.sin(temp_theta), 0), color=color.black, length=minorTickL,
                        width=minorTickW, height=minorTickT, pos=vector((radDisperse-minorTickL/2-minorTickT/2)*np.cos(temp_theta), (radDisperse-minorTickL/2-minorTickT/2)*np.sin(temp_theta), minorTickW/2))
arrowHub = cylinder(axis=vector(0,0,1), color=color.blue, radius=.5, length=1, pos=vector(0,majorTickW/2,0))
indicaTOR= arrow(axis=vector(-1, 0, 0), color=color.blue,
                   shaftwidth=majorTickT, length=arrowL, pos=vector(0, 0, .5))
incomingValue=0;
valueLabel=label(text=str(incomingValue), color=color.blue,height=24, border=4, pos=vector(
        0, -4, 0))#to find out
#titleText=input('Please input dial name: ')
titleText='Test'
title=text(text=titleText,align='center',color=color.blue,height=2,pos=vector(0,bgHeight+1,0),depth=0.5)
#for i in range(1,7,1):
    
max_flag=0
Angle = np.pi
AngleInc = -np.pi/6
#Angle = Angle+AngleInc
numH = .75
for i in np.linspace(0,1023,7):
    clockNum = text(align='center', text=str(int(i)), color=color.blue, pos=vector(
        arrowL*0.85*np.cos(Angle), arrowL*0.85*np.sin(Angle)-numH/2, 0), height=numH, depth=.1)
    Angle = Angle+AngleInc
while True:
    rate(100)
    valueLabel.text=str(incomingValue)
    print(incomingValue, end='  ')
    if max_flag==0:
        incomingValue+=1
    if max_flag==1:
        incomingValue-=1
    if incomingValue==1500:
        max_flag=1
    if incomingValue==-500:
        max_flag=0
    print(incomingValue, end='  ')
    if (incomingValue<0) or (incomingValue>1023):
        bgBox.color=color.red
    elif (incomingValue>=0) and (incomingValue<=1023):
        bgBox.color=color.white
    mappedVal=mapValue(incomingValue,0,1023,1.000,0.000)
    mappedVal=round(mappedVal,3)
    print(mappedVal, end='  ')
    constrainedMappedVal=constrainValue(mappedVal,0.000,1.000)
    constrainedMappedVal=round(constrainedMappedVal,3)
    print(constrainedMappedVal)
    indicaTOR.axis=vector(arrowL*np.cos(constrainedMappedVal*np.pi),arrowL*np.sin(constrainedMappedVal*np.pi),0)