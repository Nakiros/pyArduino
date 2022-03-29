import time
import serial
arduinoData=serial.Serial('com6',115200)
time.sleep(1)
while True:
    while(arduinoData.inWaiting()==0):
        pass
    dataPacket=arduinoData.readline()
    dataPacket=str(dataPacket,'utf-8') #show without b' CR  and NL
    dataPacket=dataPacket.strip('\r\n')
    splitPacket=dataPacket.split(',')
    print(splitPacket)
    print(len(splitPacket))
    x=float(splitPacket[0])
    y=float(splitPacket[1])
    z=float(splitPacket[2])
    print('X=',x, 'Y=',y, 'Z=',z)