from configparser import ConfigParser
file = 'C:/Users/Costy/Documents/LEARN/pyArduino/pyArd/lessons/config.ini'
config = ConfigParser()
config.read(file)

print(config.sections())