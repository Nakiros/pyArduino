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
runRED = 0
runGREEN = 0
runBLUE = 0

myspeedRed = 1
myspeedGreen = 1
myspeedBlue = 1

scene.append_to_caption('\n')


def callColorRed(x):
    marble1.color = vector(0.5, 0, 0)


def callColorGreen(x):
    marble2.color = vector(0, 0.5, 0)


def callColorBlue(x):
    marble3.color = vector(0, 0, 0.5)


button(bind=callColorRed, text='Other red',
       color=color.black, background=vector(0.5, 0, 0))
button(bind=callColorGreen, text='Other green',
       color=color.black, background=vector(0, 0.5, 0))
button(bind=callColorBlue, text='Other blue',
       color=color.black, background=vector(0, 0, 0.5))
scene.append_to_caption('\n')


def callColorfirstRed(x):
    marble1.color = color.red


def callColorfirstGreen(x):
    marble2.color = color.green


def callColorfirstBlue(x):
    marble3.color = color.blue


button(bind=callColorfirstRed, text='First red',
       color=color.black, background=color.red)
button(bind=callColorfirstGreen, text='First green',
       color=color.black, background=color.green)
button(bind=callColorfirstBlue, text='First blue',
       color=color.black, background=color.blue)
scene.append_to_caption('\n\n')

wtext(text='RED Ball opacity')
scene.append_to_caption('\n')


def ballOpacityRed(x):
    op = x.value
    marble1.opacity = op


slider(bind=ballOpacityRed, vertical=False, min=0,
       max=1, value=1)

scene.append_to_caption('\n\n')

wtext(text='GREEN Ball opacity')
scene.append_to_caption('\n')


def ballOpacityGreen(x):
    op = x.value
    marble2.opacity = op


slider(bind=ballOpacityGreen, vertical=False, min=0,
       max=1, value=1)

scene.append_to_caption('\n\n')

wtext(text='BLUE Ball opacity')
scene.append_to_caption('\n')


def ballOpacityBlue(x):
    op = x.value
    marble3.opacity = op


slider(bind=ballOpacityBlue, vertical=False, min=0,
       max=1, value=1, text='BLUE Ball opacity')

scene.append_to_caption('\n\n')


def speedRed(x):
    global myspeedRed
    if x.selected == '1':
        myspeedRed = 1
    if x.selected == '2':
        myspeedRed = 2
    if x.selected == '3':
        myspeedRed = 3
    if x.selected == '4':
        myspeedRed = 4
    if x.selected == '5':
        myspeedRed = 5


wtext(text='Red ball speed')
menu(bind=speedRed, choices=['1', '2', '3', '4', '5'])
scene.append_to_caption('    ')


def speedGreen(x):
    global myspeedGreen
    if x.selected == '1':
        myspeedGreen = 1
    if x.selected == '2':
        myspeedGreen = 2
    if x.selected == '3':
        myspeedGreen = 3
    if x.selected == '4':
        myspeedGreen = 4
    if x.selected == '5':
        myspeedGreen = 5


wtext(text='Green ball speed')
menu(bind=speedGreen, choices=['1', '2', '3', '4', '5'])
scene.append_to_caption('    ')


def speedBlue(x):
    global myspeedBlue
    if x.selected == '1':
        myspeedBlue = 1
    if x.selected == '2':
        myspeedBlue = 2
    if x.selected == '3':
        myspeedBlue = 3
    if x.selected == '4':
        myspeedBlue = 4
    if x.selected == '5':
        myspeedBlue = 5


wtext(text='Blue ball speed')
menu(bind=speedBlue, choices=['1', '2', '3', '4', '5'])
scene.append_to_caption('\n\n')


def runRadioRed(x):
    print(x.checked)
    global runRED
    if x.checked == True:
        runRED = 1
    if x.checked == False:
        runRED = 0


radio(bind=runRadioRed, text='Run RED')


def runRadioGreen(x):
    print(x.checked)
    global runGREEN
    if x.checked == True:
        runGREEN = 1
    if x.checked == False:
        runGREEN = 0


radio(bind=runRadioGreen, text='Run GREEN')


def runRadioBlue(x):
    print(x.checked)
    global runBLUE
    if x.checked == True:
        runBLUE = 1
    if x.checked == False:
        runBLUE = 0


radio(bind=runRadioBlue, text='Run BLUE')

scene.append_to_caption('\n\n')


def bigBallRED(x):
    global mRadius1
    if x.checked == True:
        mRadius1 = mRadius1*1.2
        marble1.radius = mRadius1
    if x.checked == False:
        mRadius1 = mRadius1/1.2
        marble1.radius = mRadius1


checkbox(bind=bigBallRED, text='Big Ball RED')


def bigBallGREEN(x):
    global mRadius2
    if x.checked == True:
        mRadius2 = mRadius2*1.2
        marble2.radius = mRadius2
    if x.checked == False:
        mRadius2 = mRadius2/1.2
        marble2.radius = mRadius2


checkbox(bind=bigBallGREEN, text='Big Ball GREEN')


def bigBallBLUE(x):
    global mRadius3
    if x.checked == True:
        mRadius3 = mRadius3*1.2
        marble3.radius = mRadius3
    if x.checked == False:
        mRadius3 = mRadius3/1.2
        marble3.radius = mRadius3


checkbox(bind=bigBallBLUE, text='Big Ball BLUE')

while True:
    rate(40)

    xPosm1 = xPosm1+deltaX1*runRED*myspeedRed
    yPosm1 = yPosm1+deltaY1*runRED*myspeedRed
    zPosm1 = zPosm1+deltaZ1*runRED*myspeedRed

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

    xPosm2 = xPosm2+deltaX2*runGREEN*myspeedGreen
    yPosm2 = yPosm2+deltaY2*runGREEN*myspeedGreen
    zPosm2 = zPosm2+deltaZ2*runGREEN*myspeedGreen

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

    xPosm3 = xPosm3+deltaX3*runBLUE*myspeedBlue
    yPosm3 = yPosm3+deltaY3*runBLUE*myspeedBlue
    zPosm3 = zPosm3+deltaZ3*runBLUE*myspeedBlue

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
