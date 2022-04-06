from vpython import*
import numpy as np

arrowL = 2
arrowT = .02
pntT = .04
bRadius = .04

Xarrow = arrow(axis=vector(1, 0, 0), color=color.red,
               length=arrowL, shaftwidth=arrowT)
Yarrow = arrow(axis=vector(0, 1, 0), color=color.green,
               length=arrowL, shaftwidth=arrowT)
Zarrow = arrow(axis=vector(0, 0, 1), color=color.blue,
               length=arrowL, shaftwidth=arrowT)
pntArrow = arrow(axis=vector(1, 0, 0), color=color.orange,
                 length=arrowL, shaftwidth=pntT)
myBall = sphere(make_trail=True, trail_color=color.cyan, radius=bRadius,
                color=color.white, pos=vector(arrowL, 0, 0))
while True:
    for myAngle in np.linspace(0, 2*np.pi, 1000):
        rate(100)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),
                               arrowL*np.sin(myAngle), 0)
        pntArrow.length = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle),
                            arrowL*np.sin(myAngle), 0)
    for myAngle in np.linspace(0, 2*np.pi, 1000):
        rate(100)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),
                               0, arrowL*np.sin(myAngle))
        pntArrow.length = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle),
                            0, arrowL*np.sin(myAngle))
    for myAngle in np.linspace(0, np.pi/2, 250):
        rate(100)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),
                               0, arrowL*np.sin(myAngle))
        pntArrow.length = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle),
                            0, arrowL*np.sin(myAngle))
    for myAngle in np.linspace(0, 2*np.pi, 1000):
        rate(100)
        pntArrow.axis = vector(0, arrowL*np.sin(myAngle),
                               arrowL*np.cos(myAngle))
        pntArrow.length = arrowL
        myBall.pos = vector(0, arrowL*np.sin(myAngle),
                            arrowL*np.cos(myAngle))
    for myAngle in np.linspace(np.pi/2, 0, 250):
        rate(100)
        pntArrow.axis = vector(arrowL*np.cos(myAngle),
                               0, arrowL*np.sin(myAngle))
        pntArrow.length = arrowL
        myBall.pos = vector(arrowL*np.cos(myAngle),
                            0, arrowL*np.sin(myAngle))
