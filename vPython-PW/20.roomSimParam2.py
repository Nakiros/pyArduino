from vpython import *
from time import *

mRadius1 = .5
mRadius2 = .7
mRadius3 = .8

wallThick = .1
roomWidth = 12
roomDepth = 20
roomHeigth = 5
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

marble1 = sphere(color=color.red, radius=mRadius1)
marble2 = sphere(color=color.green, radius=mRadius2)
marble3 = sphere(color=color.blue, radius=mRadius3)

deltaX1 = .1
deltaY1 = .1
deltaZ1 = .1

deltaX2 = .1
deltaY2 = .1
deltaZ2 = .1

deltaX3 = .1
deltaY3 = .1
deltaZ3 = .1

xPosm1 = 0
yPosm1 = 1
zPosm1 = 1

xPosm2 = -1
yPosm2 = -1
zPosm2 = 0

xPosm3 = -1
yPosm3 = 0
zPosm3 = 1
# ifFlag = 1 #to make the movement sequential not simultaneous on zyx

while True:
    rate(40)

    if runRadioRed.checked == True:
        xPosm1 = xPosm1+deltaX1
        yPosm1 = yPosm1+deltaY1
        zPosm1 = zPosm1+deltaZ1

        marble1.pos = vector(xPosm1, yPosm1, zPosm1)
        utmostLeft1 = -(roomWidth-2*wallThick)/2+mRadius1
        utmostRight1 = (roomWidth-2*wallThick)/2-mRadius1
        utmostUp1 = (roomHeigth-2*wallThick)/2-mRadius1
        utmostDown1 = -(roomHeigth-2*wallThick)/2+mRadius1
        utmostBack1 = -(roomDepth-2*wallThick)/2+mRadius1
        utmostFront1 = (roomDepth-2*wallThick)/2-mRadius1

        if (xPosm1 >= utmostRight1) or (xPosm1 <= utmostLeft1):
            deltaX1 = deltaX1*(-1)
        if (yPosm1 >= utmostUp1) or (yPosm1 <= utmostDown1):
            deltaY1 = deltaY1*(-1)
        if (zPosm1 >= utmostFront1) or (zPosm1 <= utmostBack1):
            deltaZ1 = deltaZ1*(-1)

    xPosm2 = xPosm2+deltaX2
    yPosm2 = yPosm2+deltaY2
    zPosm2 = zPosm2+deltaZ2

    marble2.pos = vector(xPosm2, yPosm2, zPosm2)
    utmostLeft2 = -(roomWidth-2*wallThick)/2+mRadius2
    utmostRight2 = (roomWidth-2*wallThick)/2-mRadius2
    utmostUp2 = (roomHeigth-2*wallThick)/2-mRadius2
    utmostDown2 = -(roomHeigth-2*wallThick)/2+mRadius2
    utmostBack2 = -(roomDepth-2*wallThick)/2+mRadius2
    utmostFront2 = (roomDepth-2*wallThick)/2-mRadius2

    if (xPosm2 >= utmostRight2) or (xPosm2 <= utmostLeft2):
        deltaX2 = deltaX2*(-1)
    if (yPosm2 >= utmostUp2) or (yPosm2 <= utmostDown2):
        deltaY2 = deltaY2*(-1)
    if (zPosm2 >= utmostFront2) or (zPosm2 <= utmostBack2):
        deltaZ2 = deltaZ2*(-1)

    xPosm3 = xPosm3+deltaX3
    yPosm3 = yPosm3+deltaY3
    zPosm3 = zPosm3+deltaZ3

    marble3.pos = vector(xPosm3, yPosm3, zPosm3)
    utmostLeft3 = -(roomWidth-2*wallThick)/2+mRadius3
    utmostRight3 = (roomWidth-2*wallThick)/2-mRadius3
    utmostUp3 = (roomHeigth-2*wallThick)/2-mRadius3
    utmostDown3 = -(roomHeigth-2*wallThick)/2+mRadius3
    utmostBack3 = -(roomDepth-2*wallThick)/2+mRadius3
    utmostFront3 = (roomDepth-2*wallThick)/2-mRadius3

    if (xPosm3 >= utmostRight3) or (xPosm3 <= utmostLeft3):
        deltaX3 = deltaX3*(-1)
    if (yPosm3 >= utmostUp3) or (yPosm3 <= utmostDown3):
        deltaY3 = deltaY3*(-1)
    if (zPosm3 >= utmostFront3) or (zPosm3 <= utmostBack3):
        deltaZ3 = deltaZ3*(-1)
    #print(xPos, '    ', yPos, '    ', zPos)
