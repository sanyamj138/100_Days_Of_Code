print("Welcome to the Calculator!")

def addition(num1, num2):
    return num1 + num2

def difference(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

# def calc(num1, num2):
#     addition(num1, num2)
#     difference(num1, num2)
#     multiply(num1, num2)
#     division(num1, num2)

num1 = int(input("Enter the 1st Number: "))
num2 = int(input("Enter the 2nd Number: "))
oper = input("Enter the Operation (+, -, *, /): ")
nextOper = True

if oper == "+":
    res = addition(num1, num2)
elif oper == "-":
    res = difference(num1, num2)
elif oper == "*":
    res = multiply(num1, num2)
elif oper == "/":
    res = division(num1, num2)

print("The Result is: ", res)

while nextOper:

    ques = input("Do you want to Calculate Another Number? (Y/N): ")
    if ques == "n" or ques == "N":
        nextOper = False
    else:
        num3 = int(input("Enter the Next Number: "))

        operNext = input("Enter the Operation (+, -, *, /): ")

        if operNext == "+":
            res = addition(res, num3)
        elif operNext == "-":
            res = difference(res, num3)
        elif operNext == "*":
            res = multiply(res, num3)
        elif operNext == "/":
            res = division(res, num3)

        print("The Result is: ", res)

