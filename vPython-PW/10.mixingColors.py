from vpython import *
mySphere = sphere(radius=1, color=vector(0, 0, 0))
Rchange = True
Gchange = False
Bchange = False
ValueR = 0
ValueG = 0
ValueB = 0
deltaR = .01
deltaG = .01
deltaB = .01
while True:
    rate(20)
    mySphere.color = vector(ValueR, ValueG, ValueB)
    if Rchange == True:
        ValueR = ValueR+deltaR
        if round(ValueR, 2) == 1.00 or round(ValueR, 2) == 0.00:
            Rchange = False
            Gchange = True
            deltaR = deltaR*(-1)
    if Gchange == True:
        ValueG = ValueG+deltaG
        if round(ValueG, 2) == 1.00 or round(ValueG, 2) == 0.00:
            Gchange = False
            Bchange = True
            deltaG = deltaG*(-1)
    if Bchange == True:
        ValueB = ValueB+deltaB
        if round(ValueB, 2) == 1.00 or round(ValueB, 2) == 0.00:
            Bchange = False
            Rchange = True
            deltaB = deltaB*(-1)
    print(ValueR, ' ', ValueG, ' ', ValueB)
