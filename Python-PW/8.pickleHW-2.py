import pickle
with open('studentData.pkl', 'rb') as dataR:
    numStudents = pickle.load(dataR)
    names = pickle.load(dataR)
    grades = pickle.load(dataR)
while(1 == 1):
    name = input('Which student do you want to check? ')
    for i in range(0, numStudents, 1):
        if names[i] == name:
            print(name, "'s grade is ", grades[i], '.')
