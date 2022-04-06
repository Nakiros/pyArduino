"""
print('It is time to count')
j = 1
while(j <= 10):
    print(j)
    j += 1
print('While loop finished')
"""
"""
print('It is time to count')
j = 1.0
while(j <= 10):
    print(j)
    j += 0.1
    j = round(j, 2)
print('While loop finished')
"""
# homework - while loop to inpu grades
numGrades = int(input('Please input your number of grades :'))
grades = []
i = 1
j = 0
while(i <= numGrades):
    grade = int(input('Please enter grade number '+str(i)+' :'))
    grades.append(grade)
    i += 1
while (j < numGrades):
    print(grades[j])
    j += 1
