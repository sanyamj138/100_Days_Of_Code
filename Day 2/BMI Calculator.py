print("Welcome to BMI Calculator!")
weight = float(input("What's the weight of a person?\n"))
height = float(input("What's the height of a person?\n"))

bmi = weight / (height ** 2)

print("Your BMI is: " + str(round(bmi, 2)))