print("Welcome to the Leap Year!")

def is_leap_year(year):
    if((year%4 == 0 and year%100 != 0) or (year%400 == 0)):
        return True
    else:
        return False

yearIn = int(input("Enter the Year you want to check for: "))
print(is_leap_year(yearIn))