print("Welcome to the Calculator!")

def addition(num1, num2):
    return num1 + num2

def difference(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

dict = {
    '+': addition,
    '-': difference,
    '*': multiply,
    '/': division,
}

num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
oper = input("Enter the Operation (+, -, *, /): ")
answer = dict[oper](num1, num2)
print(answer)
nextOper = True

while nextOper:
    ques = input("Do you want to Calculate Another Number? (Y/N): ")
    if ques == "n" or ques == "N":
        nextOper = False
    else:
        num3 = int(input("Enter the Next Number: "))
        operNext = input("Enter the Operation (+, -, *, /): ")

        answer = dict[operNext](answer, num3)
        print(answer)
        nextOper = True


