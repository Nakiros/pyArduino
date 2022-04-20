import serial.tools.list_ports

def get_ports():
    ports = serial.tools.list_ports.comports()
    return ports

def findArduino(portsFound,Ard_Name):
    commPort='None'
    numConnection = len(portsFound)
    
    for i in range(0,numConnection):
        port = portsFound[i]
        strPort=str(port)
        
        if Ard_Name in strPort:
            splitPort=strPort.split(' ')
            commPort = (splitPort[0])

    return commPort

def autoConArd(ArdName):
    foundPorts = get_ports()
    connectPort = findArduino(foundPorts,ArdName)
    return connectPort
    #autofind arduino port-----END