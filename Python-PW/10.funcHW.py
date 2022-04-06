
def inputGrades(nm):
    grades = []
    for i in range(0, nm, 1):
        grd = float(input('Please in put your grade: '))
        grades.append(grd)
    return grades


def printGrades(nm, x):
    for i in range(0, nm, 1):
        print(x[i])


def averageGrades(nm, x):
    tot = 0
    for i in range(0, nm, 1):
        tot += x[i]
    return round(tot/nm, 1)


def HighLow(nm, x):
    highG = 0
    lowG = 100
    for i in range(0, nm, 1):
        if x[i] < lowG:
            lowG = x[i]
        if x[i] > highG:
            highG = x[i]
    return highG, lowG


numGrades = int(input('How many grades: '))
myGrades = inputGrades(numGrades)
print('Your grades are: ')
printGrades(numGrades, myGrades)

aver = averageGrades(numGrades, myGrades)
print('Your average is:', aver)

highG, lowG = HighLow(numGrades, myGrades)
print('Your high grade is:', highG)
print('Your low grade is:', lowG)
