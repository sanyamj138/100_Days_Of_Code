print("Welcome to the Grade Calculator!")

numStudents = int(input("Enter the Number of Students: "))
dict = {}

for i in range(numStudents):
    name = input('Enter Name of Student ' + str(i + 1) +' : ')
    number = int(input('Enter Number of Student ' + str(i+1) + ': '))
    dict[name] = number

gradeDict = {}
for i, j in dict.items():
    gradeDict[i] = ''

