import time
import serial
arduinoData=serial.Serial('com4',115200)
time.sleep(1)
while True:
    while(arduinoData.inWaiting()==0):
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8') #show without b' CR  and NL
    dataPacket=dataPacket.strip('\r\n')
    print(dataPacket)