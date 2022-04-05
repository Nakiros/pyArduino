from vpython import*
import serial
import numpy as np
import time
ardSer = serial.Serial('COM5', baudrate=115200, timeout=1)
time.sleep(3)

def getValues():
    ardSer.write(b'g')
    
    arduinoData=ardSer.readline().decode('ascii').split(',')
    arduinoData[len(arduinoData)-1]=arduinoData[len(arduinoData)-1].strip()
    #print(len(arduinoData))
    #print(arduinoData)
    #arduinoData.pop()
    #print(arduinoData)
    #print(len(arduinoData))
    #print(type(arduinoData))
    #print('arduinoData[0]: ')
    #print(arduinoData[0])
    #print(type(arduinoData[0]))
    for i in range(0,len(arduinoData),1):
        arduinoData[i]=float(arduinoData[i])
    return arduinoData
while True:
    rate(2)
    testData=getValues()
    print(testData)
    #print(floatN)