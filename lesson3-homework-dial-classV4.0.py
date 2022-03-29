#it works with arduino code PW-Lesson3-2-homeworkV2.ino
from vpython import*
import numpy as np
import time
import serial
ardSer=serial.Serial('COM5',baudrate=115200,timeout=1)         #resets the arduino
time.sleep(3)                                                       #waits 3 seconds, enough time for the arduino to boot

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
arrowL=radDisperse-majorTickL

def getValues():
    ardSer.write(b'g')
    
    arduinoData=ardSer.readline().decode('ascii').split(',')
    arduinoData[len(arduinoData)-1]=arduinoData[len(arduinoData)-1].strip()
    for i in range(0,len(arduinoData),1):
        arduinoData[i]=float(arduinoData[i])
    return arduinoData

def mapValue(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def constrainValue(cVal, lowB, uppB):
    return max(lowB, min(uppB,cVal))

class MultiDial:
    def __init__(self,dialTitle,minVal,maxVal, unitOfMeasure, noOfMTick,noOfmTick,coloR,coloG,coloB, posX,posY,posZ):
        #make all values accesible
        self.dialTitle = dialTitle
        self.minVal = minVal
        self.maxVal = maxVal
        self.unitOfMeasure = unitOfMeasure
        self.noOfMTick = noOfMTick
        self.noOfmTick = noOfmTick
        self.colorR=coloR
        self.colorG= coloG
        self.colorB=coloB
        
        self.posX= posX
        self.posY= posY
        self.posZ= posZ
        self.incomingValue=0
        self.bgBox=box(pos=vector(self.posX,(bgHeight/2)+self.posY,(-bgThick/2)+self.posZ), size=vector(bgLength,bgHeight,bgThick))
        
        for theta in np.linspace(0,np.pi,self.noOfMTick):
            majorTick=box(axis=vector(radDisperse*np.cos(theta), radDisperse*np.sin(theta), 0), color=vector(self.colorR,self.colorG,self.colorB), length=majorTickL,
                    width=majorTickW, height=majorTickT, pos=vector((radDisperse-majorTickL/2-majorTickT/2)*np.cos(theta)+self.posX, (radDisperse-majorTickL/2-majorTickT/2)*np.sin(theta)+majorTickT/2+self.posY, majorTickW/2+self.posZ))
            if theta!=np.pi:
                for i in range(1, self.noOfmTick, 1):
                    temp_theta = theta+np.pi/(self.noOfmTick*(self.noOfMTick-1))*i
                    minorTick = box(axis=vector(radDisperse*np.cos(temp_theta), radDisperse*np.sin(temp_theta), 0), color=color.black, length=minorTickL,
                        width=minorTickW, height=minorTickT, pos=vector((radDisperse-minorTickL/2-minorTickT/2)*np.cos(temp_theta)+self.posX, (radDisperse-minorTickL/2-minorTickT/2)*np.sin(temp_theta)+self.posY, minorTickW/2+self.posZ))
        arrowHub = cylinder(axis=vector(0,0,1), color=majorTick.color, radius=.5, length=1, pos=vector(self.posX,majorTickW/2+self.posY,self.posZ))
        self.indicaTOR= arrow(axis=vector(-1, 0, 0), color=majorTick.color,
                   shaftwidth=majorTickT, length=arrowL, pos=vector(self.posX, self.posY, .5+self.posZ))
        self.valueLabel=label(text=str(self.incomingValue), color=majorTick.color,height=24, border=4, pos=vector(
        self.posX, -4+self.posY, self.posZ))#to find out

        title=text(text=self.dialTitle,align='center',color=majorTick.color,height=2,pos=vector(self.posX,bgHeight+1+self.posY,self.posZ),depth=0.5)
    
        Angle = np.pi
        AngleInc = -np.pi/(self.noOfMTick-1)
        #Angle = Angle+AngleInc
        numH = .75
        for i in np.linspace(self.minVal,self.maxVal,self.noOfMTick):
            clockNum = text(align='center', text=str(int(i)), color=majorTick.color, pos=vector(
            arrowL*0.85*np.cos(Angle)+self.posX, arrowL*0.85*np.sin(Angle)-numH/2+self.posY, self.posZ), height=numH, depth=.1)
            Angle = Angle+AngleInc

#BEGIN----PRE-RUN SETUP----INPUT DATA----
    #OFFSET CALCULATION--BEGIN
NoOfDials= int(input('Please input number of dials: '))                     #Insert number of dials you want to show
spawnOffset=[]                                                              #Use a list to catch the X offset postion of the dials
if  NoOfDials>1:                                                            #If there are more than 1 dial
    distDials=int(input('Please input the distance bewteen each dial. Enter '+str(bgLength)+'+desired gap between dials: '))   #Input the spacing between each of the dials. Each dial is 20 in length
    for i in range(0,NoOfDials,1):                                          #Calculate for  each dial the distDials
        if NoOfDials % 2 == 1:                                              #If there is an odd number of dials (e.g. 5 dials: the 3rd on will be at x=0 teh 2nd and 4th wil be at -distDials and +OFFSET, the 1st and 5th will be at -2*distDials and 2*distDials)
            spawnOffset.append(-1*distDials*(int(NoOfDials/2)-i))           #calculate the offset this way and fill the list
        if NoOfDials % 2 == 0:                                              #If there is and even number of dials (e.g. there are 4 dials, dial 2 and 3 will be at -distDials/2 and distDials/2,while the 1st and 4th will be at -distDials-distDials/2 and distDials+distDials/2)
            spawnOffset.append(-1*(distDials *
                               (int(NoOfDials/2)-(i+1))+int(distDials/2)))  #calculate this way
print(NoOfDials)                                                            #debug
if  NoOfDials>1:  
    print(distDials)
print(spawnOffset)
    #OFFSET CALCULATION----END
    #DIALS PARAMETERS----BEGIN
dialsList=[]
print('--------------------------------Insert Dial parameters--------------------------------')
for i in range(0, NoOfDials, 1):                                #insert dial parameters one by one
    filler = ''                                                 #prompt index
    if i == 0:
        filler = '1st'
    if i == 1:
        filler = '2nd'
    if i == 2:
        filler = '3rd'
    if i > 2:
        filler = str(i+1)+'th'
    dialTitle_temp = input(filler+' dial title: ')
    
    print('Enter input characteristics')
    inputMin=float(input(filler+' dial MIN input value: '))
    inputMax=float(input(filler+' dial MAX input value: '))
    unit_Temp=input(filler+' dial unit of measurement is: ')
    
    print('Define the gradations')
    noOfMTick_temp=int(input(filler+' dial number of MAJOR Ticks: '))
    noOfmTick_temp=int(input(filler+' dial number of MINOR Ticks: '))
    coloR_temp=float(input(filler+' dial MAJOR color - RED: '))
    coloG_temp=float(input(filler+' dial MAJOR color - GREEN: '))
    coloB_temp=float(input(filler+' dial MAJOR color - BLUE: '))
    
    answer=input('Do you want to spawn the dial/dials in default position/positions? Answer YES or NO.')
    
    if answer == 'YES':
        if  NoOfDials>1:
            posX_temp=spawnOffset[i]
        else:
            posX_temp=0
        posY_temp=0
        posZ_temp=0
    elif answer == 'NO': 
        posX_temp = float(input(filler+' dial posX: '))
        posY_temp = float(input(filler+' dial posY: '))
        posZ_temp = float(input(filler+' dial posZ: '))
    else: 
        print('Please enter YES or NO next time. Default YES was chosen. DO NOT ENTER Y,N or yes,no or y,n. Only YES,NO')
        if  NoOfDials>1:
            posX_temp=spawnOffset[i]
        else:
            posX_temp=0
        posY_temp=0
        posZ_temp=0

    temp_object = MultiDial(dialTitle_temp,inputMin,inputMax,unit_Temp,noOfMTick_temp,noOfmTick_temp,coloR_temp,coloG_temp,coloB_temp,posX_temp,posY_temp,posZ_temp)
    dialsList.append(temp_object)
   

#END----PRE-RUN SETUP----INPUT DATA------

while True:
    rate(5000)
    #GET ARDUINO GATA VIA SERIAL
    sensorData=getValues()
    #UPDATE arrows and lables for all dials
    for i in range(0, NoOfDials, 1):
        constrainedValue=constrainValue(float(sensorData[i]),dialsList[i].minVal,dialsList[i].maxVal)
        angleRad=mapValue(constrainedValue,dialsList[i].minVal,dialsList[i].maxVal,1.000,0.000)
        dialsList[i].indicaTOR.axis=vector(arrowL*np.cos(angleRad*np.pi),arrowL*np.sin(angleRad*np.pi),0)
        dialsList[i].valueLabel.text=str(constrainedValue)+' '+dialsList[i].unitOfMeasure
        if (float(sensorData[i])>=dialsList[i].minVal) and (float(sensorData[i])<=dialsList[i].maxVal):
            dialsList[i].bgBox.color=color.white
        else:
            dialsList[i].bgBox.color=color.red
            print(dialsList[i].dialTitle,'is out of bounds.')
