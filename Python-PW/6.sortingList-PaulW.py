numGrades = int(input('How many grades do you have? '))
grades = []
highest_grade = 0
lowest_grade = 10
for i in range(0, numGrades, 1):
    grade = int(input('Please enter grade number '+str(i+1)+' :'))
    grades.append(grade)
averageGrade = 0.0
for i in range(0, numGrades, 1):
    averageGrade = averageGrade+grades[i]
averageGrade = averageGrade/numGrades
print('Your average grade is '+str(averageGrade)+' from the following grades:')
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
    print('Your '+filler+' grade: '+str(grades[i]))
    if (highest_grade < grades[i]):
        highest_grade = grades[i]
    if (lowest_grade >= grades[i]):
        lowest_grade = grades[i]
print('Your highest grade is: '+str(highest_grade) +
      ' and your lowest grade is: '+str(lowest_grade))
ordered_grades = []
for i in range(0, numGrades, 1):
    ordered_grades.append(grades[i])

for i in range(0, numGrades-1, 1):
    for i in range(0, numGrades-1, 1):
        if ordered_grades[i] < ordered_grades[i+1]:
            swp = ordered_grades[i]
            ordered_grades[i] = ordered_grades[i+1]
            ordered_grades[i+1] = swp
print('Your sorted grades list is: ')
for i in range(0, numGrades, 1):
    print(ordered_grades[i])
