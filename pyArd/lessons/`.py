import time
import serial
import lessons.lesson10_AutoConnect_module as AutoCon #import as module lesson10_AutoConnect_module.py from lessons folder

conPort=AutoCon.autoConArd('CH340')     #look under COM ports in device manager and see key search word that is part of the connected arduino board name

if conPort != 'None':
    ardSer = serial.Serial(conPort,baudrate = 115200, timeout=1) #resets the arduino
    print('Connected to ' + conPort)

else:
    print('Connection Issue!')

print('DONE')

time.sleep(3)

while True:
    cmd=input('Please enter your comand: ')
    cmd=cmd+'\r'
    ardSer.write(cmd.encode())