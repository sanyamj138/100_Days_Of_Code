print("Welcome to the Grade Calculator!")

def gradePattern(num):
    if (num <= 100 and num > 90):
        return 'Outstanding'
    elif (num <= 90 and num > 80):
        return 'Exceeds Expectations'
    elif (num <= 80 and num > 70):
        return 'Acceptable'
    elif (num <= 70):
        return 'Fail'
    else:
        return 'Incorrect Number Entered!'

numStudents = int(input("Enter the Number of Students: "))
dict = {}

for i in range(numStudents):
    name = input('Enter Name of Student ' + str(i + 1) +' : ')
    number = int(input('Enter Number of Student ' + str(i+1) + ': '))
    dict[name] = number

gradeDict = {}
for i, j in dict.items():
    gradeDict[i] = gradePattern(dict[i])

print(dict)
print(gradeDict)




