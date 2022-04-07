from configparser import ConfigParser
file = 'C:/Users/Costy/Documents/LEARN/pyArduino/pyArd/lessons/lesson3-3.3.3-prereq-testing.ini'
config = ConfigParser()
config.read(file)

lista=list(config.sections())
print(lista)

for i in range(0,4,1):
    print(config[lista[i]]['dialTitle'])