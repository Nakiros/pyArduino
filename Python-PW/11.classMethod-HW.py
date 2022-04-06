class Student:
    def __init__(self, fName, sName):
        self.firstName = fName
        self.secondName = sName

    def inputGrades(self):
        self.grades = []
        self.noGrd = int(
            input('Please input the number of grades you wish to insert: '))
        for i in range(0, self.noGrd, 1):
            filler = ''
            if i == 0:
                filler = '1st'
            if i == 1:
                filler = '2nd'
            if i == 2:
                filler = '3rd'
            if i > 2:
                filler = str(i+1)+'th'
            grd = float(input('Please input your '+filler+' grade: '))
            self.grades.append(grd)
        return self.grades

    def printGrades(self):
        for i in range(0, self.noGrd, 1):
            print(self.grades[i])

    def averageGrades(self):
        tot = 0
        for i in range(0, self.noGrd, 1):
            tot += self.grades[i]
        return round(tot/self.noGrd, 1)

    def HighLow(self):
        self.highG = 0
        self.lowG = 100
        for i in range(0, self.noGrd, 1):
            if self.grades[i] < self.lowG:
                self.lowG = self.grades[i]
            if self.grades[i] > self.highG:
                self.highG = self.grades[i]
        return self.highG, self.lowG


studentNo = int(input('Please enter the number of students: '))
print('Number of students is:', studentNo)
studentList = []
print('Student First and Last name input')

for i in range(0, studentNo, 1):
    filler = ''
    if i == 0:
        filler = '1st'
    if i == 1:
        filler = '2nd'
    if i == 2:
        filler = '3rd'
    if i > 2:
        filler = str(i+1)+'th'
    first = input(filler+" student's First name: ")
    second = input(filler+" student's Last name: ")
    temp_object = Student(first, second)
    studentList.append(temp_object)

print('Input grades')
for i in range(0, studentNo, 1):
    print('Insert grades for',
          studentList[i].firstName, studentList[i].secondName)
    studentList[i].inputGrades()

print('Print grades')
for i in range(0, studentNo, 1):
    print('Print grades for',
          studentList[i].firstName, studentList[i].secondName)
    studentList[i].printGrades()

print('Calculate and print averages')
for i in range(0, studentNo, 1):
    print('Print average grade for',
          studentList[i].firstName, studentList[i].secondName)
    print(studentList[i].averageGrades())

print('Print highest grade and lowest grade')
for i in range(0, studentNo, 1):
    highG, lowG = studentList[i].HighLow()
    print('Print Highest and Lowest grade for',
          studentList[i].firstName, studentList[i].secondName, 'are', highG, 'and', lowG)
