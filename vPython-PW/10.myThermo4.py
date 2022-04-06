from turtle import pos
from vpython import*
import numpy as np


class MyThermo:
    def __init__(self, thermoLength, posX, posY, posZ, tMax, tMin, mercRcolor, mercGcolor, mercBcolor, Temp):
        self.thermoLength = thermoLength
        self.Temp = Temp
        self.thermoPosX = -thermoLength/2
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.tMin = tMin
        self.tMax = tMax
        self.mapedTemp = (self.Temp - self.tMin) * \
            (self.thermoLength - 1) / (self.tMax - self.tMin) + 1
        self.mercRcolor = mercRcolor
        self.mercGcolor = mercGcolor
        self.mercBcolor = mercBcolor
        self.mercColor = vector(
            self.mercRcolor, self.mercGcolor, self.mercBcolor)
        self.glassCyl = cylinder(radius=.65, length=self.thermoLength+0.1, color=color.white,
                                 opacity=.3, up=vector(-1, 0, 0), pos=vector(self.posX, self.posY+self.thermoPosX, self.posZ))
        self.glassBulb = sphere(radius=1.25, color=color.white,
                                opacity=.3, pos=vector(self.posX, self.posY+self.thermoPosX, self.posZ))
        self.mercCyl = cylinder(radius=.45, length=self.mapedTemp,
                                color=self.mercColor, up=vector(-1, 0, 0), pos=vector(self.posX, self.posY+self.thermoPosX, self.posZ))
        self.mercBulb = sphere(radius=1, color=self.mercColor, pos=vector(
            self.posX, self.posY+self.thermoPosX, self.posZ))
        for tick in np.linspace(1, self.thermoLength, 35):
            box(size=vector(.05, .05, .25), color=color.white,
                pos=vector(-self.glassCyl.radius+.05/2+self.posX, self.thermoPosX+tick+self.posY, self.posZ))


def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


NoOfThermo = int(input('Please enter number of thermometers: '))
if NoOfThermo > 1:
    distThermo = int(input('Please input distance between the thermometers: '))
    spawnOffset = []
    for i in range(0, NoOfThermo, 1):
        if NoOfThermo % 2 == 1:
            spawnOffset.append(-1*distThermo*(int(NoOfThermo/2)-i))
        if NoOfThermo % 2 == 0:
            spawnOffset.append(-1*(distThermo *
                               (int(NoOfThermo/2)-(i+1))+int(distThermo/2)))
        # print(spawnOffset[i])
thermo = []
tempParse = []
print('Insert thermometer parameters--------------------------------')
for i in range(0, NoOfThermo, 1):
    filler = ''
    if i == 0:
        filler = '1st'
    if i == 1:
        filler = '2nd'
    if i == 2:
        filler = '3rd'
    if i > 2:
        filler = str(i+1)+'th'
    tLength = float(input(filler+' thermometer length: '))
    tTemp = float(input('Please input temperature: '))
    if NoOfThermo > 1:
        TposX = int(input(filler+' thermometer posX: '))+spawnOffset[i]
    else:
        TposX = int(input(filler+' thermometer posX: '))
    TposY = int(input(filler+' thermometer posY: '))
    TposZ = int(input(filler+' thermometer posZ: '))
    Ttmax = float(input(filler+' thermometer T MAX: '))
    Ttmin = float(input(filler+' thermometer T MIN: '))
    TmercRcolor = float(input(filler+' thermometer R color: '))
    TmercGcolor = float(input(filler+' thermometer G color: '))
    TmercBcolor = float(input(filler+' thermometer B color: '))
    temp_Parse = 0.0
    temp_object = MyThermo(tLength, TposX, TposY, TposZ, Ttmax,
                           Ttmin, TmercRcolor, TmercGcolor, TmercBcolor, tTemp)
    thermo.append(temp_object)
    tempParse.append(temp_Parse)


while True:
    rate(40)

    for i in range(0, NoOfThermo, 1):

        temp_input = float(
            input('Please input temperature for thermometer number '+str(i+1)+': '))
        if temp_input > thermo[i].tMax:
            print('Temperature out of MAX bound. Showing MAX.')
            temp_input = thermo[i].tMax
        if temp_input < thermo[i].tMin:
            print('Temperature out of MIN bound. Showing MIN.')
            temp_input = thermo[i].tMin
        tempParse[i] = temp_input
        lengthTemp = map(tempParse[i], thermo[i].tMin,
                         thermo[i].tMax, 1, thermo[i].thermoLength)
        #thermo[i].mercCyl.length = lengthTemp
        if lengthTemp != 0:
            if lengthTemp < thermo[i].tMin:  # redundant
                thermo[i].mercCyl.up = vector(1, 0, 0)  # redundant
            if lengthTemp > thermo[i].tMin:  # redundant
                thermo[i].mercCyl.up = vector(-1, 0, 0)  # redundant

                thermo[i].mercCyl.length = lengthTemp
        else:
            print('Length is zero -> NO CHANGE')
