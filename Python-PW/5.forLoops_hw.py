# Costy
"""
no_of_Grades = int(input('Please specify the number of grades: '))
print(no_of_Grades)
myGrades = []
for grade_no in range(0, no_of_Grades, 1):
    grade = int(input('Please enter grade number '+str(grade_no+1)+':'))
    myGrades.append(grade)
for showGrade in myGrades:
    print(showGrade)
"""

# PaulW
numGrades = int(input('How many grades do you have? '))
grades = []
for i in range(0, numGrades, 1):
    grade = int(input('Please enter grade number '+str(i+1)+' :'))
    grades.append(grade)
for i in range(0, numGrades, 1):
    filler = 'zero'
    if (i == 0):
        filler = 'first'
    if (i == 1):
        filler = 'second'
    if (i == 2):
        filler = 'third'
    if (i > 2):
        filler = str(i+1)+'th'
    print('Your '+filler+' grade is: '+str(grades[i]))
