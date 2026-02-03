print("Welcome to the BMI Calculator!")
weight = float(input("What is your weight? "))
height = float(input("What is your height? "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Under Weight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal Weight")
else:
    print("Over Weight")