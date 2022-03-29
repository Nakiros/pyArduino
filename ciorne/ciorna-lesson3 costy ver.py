for theta in np.linspace(0,np.pi,7):
    majorTick=box(axis=vector(radDisperse*np.cos(theta), radDisperse*np.sin(theta), 0), color=color.blue, length=majorTickL,
                    width=majorTickW, height=majorTickT, pos=vector((radDisperse-majorTickL/2-majorTickT/2)*np.cos(theta), (radDisperse-majorTickL/2-majorTickT/2)*np.sin(theta)+majorTickT/2, majorTickW/2))
    if theta!=np.pi:
        for i in range(1, 10, 1):
            temp_theta = theta+np.pi/60*i
            minorTick = box(axis=vector(radDisperse*np.cos(temp_theta), radDisperse*np.sin(temp_theta), 0), color=color.black, length=minorTickL,
                        width=minorTickW, height=minorTickT, pos=vector((radDisperse-minorTickL/2-minorTickT/2)*np.cos(temp_theta), (radDisperse-minorTickL/2-minorTickT/2)*np.sin(temp_theta), minorTickW/2))
arrowHub = cylinder(axis=vector(0,0,1), color=color.blue, radius=.5, length=1, pos=vector(0,majorTickW/2,0))
indicaTOR= arrow(axis=vector(-1, 0, 0), color=color.blue,
                   shaftwidth=majorTickT, length=arrowL, pos=vector(0, 0, .5))
incomingValue=0;
valueLabel=label(text=str(incomingValue), color=color.blue,height=24, border=4, pos=vector(
        0, -4, 0))#to find out
max_flag=0

    valueLabel.text=str(incomingValue)
    print(incomingValue, end='  ')
    if max_flag==0:
        incomingValue+=1
    if max_flag==1:
        incomingValue-=1
    if incomingValue==1500:
        max_flag=1
    if incomingValue==-500:
        max_flag=0
    print(incomingValue, end='  ')
    if (incomingValue<0) or (incomingValue>1023):
        bgBox.color=color.red
    elif (incomingValue>=0) and (incomingValue<=1023):
        bgBox.color=color.white
    mappedVal=mapValue(incomingValue,0,1023,1.000,0.000)
    mappedVal=round(mappedVal,3)
    print(mappedVal, end='  ')
    constrainedMappedVal=constrainValue(mappedVal,0.000,1.000)
    constrainedMappedVal=round(constrainedMappedVal,3)
    print(constrainedMappedVal)
    indicaTOR.axis=vector(arrowL*np.cos(constrainedMappedVal*np.pi),arrowL*np.sin(constrainedMappedVal*np.pi),0)