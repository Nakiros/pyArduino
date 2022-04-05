import pickle
names = []
grades = []
numStudents = int(input('Please enter your number of students: '))
for j in range(0, numStudents, 1):
    name = input('Please enter student name: ')
    names.append(name)
    prompt = 'Please enter '+name+"'s grade: "
    grade = float(input(prompt))
    grades.append(grade)
with open('studentData.pkl', 'wb') as dataW:
    pickle.dump(numStudents, dataW)
    pickle.dump(names, dataW)
    pickle.dump(grades, dataW)
with open('studentData.pkl', 'rb') as dataR:
    a = pickle.load(dataR)
    b = pickle.load(dataR)
    c = pickle.load(dataR)
print(a)
print(b)
print(c)
