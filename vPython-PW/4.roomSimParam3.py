from vpython import *
from time import *


class ParamBall:
    def __init__(self, mRadius, colorR, colorG, colorB, posX, posY, posZ, speedX, speedY, speedZ):
        self.mRadius = mRadius
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.speedX = speedX
        self.speedY = speedY
        self.speedZ = speedZ


print('Define your room. Dimensions include wall thickness.')
roomWidth = int(input('Room width: '))
roomDepth = int(input('Room depth: '))
roomHeigth = int(input('Room height: '))
wallThick = float(input('Wall thickness: '))

print('A room with the dimenssions of '+str(roomWidth)+'x'+str(roomHeigth)+'x' +
      str(roomDepth)+' and a wall thickness of '+str(wallThick)+' will be created.')
floor = box(pos=vector(0, -roomHeigth/2+wallThick/2, 0), color=color.white,
            size=vector(roomWidth, wallThick, roomDepth))

ceiling = box(pos=vector(0, roomHeigth/2-wallThick/2, 0), color=color.white,
              size=vector(roomWidth, wallThick, roomDepth))

backWall = box(pos=vector(0, 0, -roomDepth/2+wallThick/2), color=color.white,
               size=vector(roomWidth-2*wallThick, roomHeigth-2*wallThick, wallThick))

leftWall = box(pos=vector(-roomWidth/2+wallThick/2, 0, 0), color=color.white,
               size=vector(wallThick, roomHeigth-2*wallThick, roomDepth))

rightWall = box(pos=vector(roomWidth/2-wallThick/2, 0, 0), color=color.white,
                size=vector(wallThick, roomHeigth-2*wallThick, roomDepth))

noBalls = int(input('Please input number of balls: '))
print('Number of balls: ', noBalls)
ballParamList = []
ballSpawnList = []
"""
utmostLeft=[]
utmostRight=[]
utmostUp=[]
utmostDown=[]
utmostBack=[]
utmostFront=[]
"""

print('Insert ball parameters--------------------------------')
for i in range(0, noBalls, 1):
    filler = ''
    if i == 0:
        filler = '1st'
    if i == 1:
        filler = '2nd'
    if i == 2:
        filler = '3rd'
    if i > 2:
        filler = str(i+1)+'th'
    bRadius = float(input(filler+' ball RADIUS: '))
    bRcolor = int(input(filler+' ball COLOR R value: '))
    bGcolor = int(input(filler+' ball COLOR G value: '))
    bBcolor = int(input(filler+' ball COLOR B value: '))
    bStartPosX = float(input(filler+' ball START X position value: '))
    bStartPosY = float(input(filler+' ball START Y position value: '))
    bStartPosZ = float(input(filler+' ball START Z position value: '))
    bSpeedX = float(input(filler+' ball speed on X: '))
    bSpeedY = float(input(filler+' ball speed on Y: '))
    bSpeedZ = float(input(filler+' ball speed on z: '))
    temp_object = ParamBall(bRadius, bRcolor, bGcolor, bBcolor,
                            bStartPosX, bStartPosY, bStartPosZ, bSpeedX, bSpeedY, bSpeedZ)
    ballParamList.append(temp_object)
    temp_ball = sphere(color=vector(bRcolor, bGcolor, bBcolor),
                       radius=bRadius, pos=vector(bStartPosX, bStartPosY, bStartPosZ))
    ballSpawnList.append(temp_ball)


while True:
    rate(40)

    for i in range(0, noBalls, 1):
        ballParamList[i].posX = ballParamList[i].posX+ballParamList[i].speedX
        ballParamList[i].posY = ballParamList[i].posY+ballParamList[i].speedY
        ballParamList[i].posZ = ballParamList[i].posZ+ballParamList[i].speedZ

        ballSpawnList[i].pos = vector(
            ballParamList[i].posX, ballParamList[i].posY, ballParamList[i].posZ)

        utmostLeft = -(roomWidth-2*wallThick)/2+ballParamList[i].mRadius
        utmostRight = (roomWidth-2*wallThick)/2-ballParamList[i].mRadius
        utmostUp = (roomHeigth-2*wallThick)/2-ballParamList[i].mRadius
        utmostDown = -(roomHeigth-2*wallThick)/2+ballParamList[i].mRadius
        utmostBack = -(roomDepth-2*wallThick)/2+ballParamList[i].mRadius
        utmostFront = (roomDepth-2*wallThick)/2-ballParamList[i].mRadius

        if (ballParamList[i].posX >= utmostRight) or (ballParamList[i].posX <= utmostLeft):
            ballParamList[i].speedX = ballParamList[i].speedX*(-1)
        if (ballParamList[i].posY >= utmostUp) or (ballParamList[i].posY <= utmostDown):
            ballParamList[i].speedY = ballParamList[i].speedY*(-1)
        if (ballParamList[i].posZ >= utmostFront) or (ballParamList[i].posZ <= utmostBack):
            ballParamList[i].speedZ = ballParamList[i].speedZ*(-1)
        # print(ballParamList[i].posX,
        #      ballParamList[i].posY, ballParamList[i].posZ)
