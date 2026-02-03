print("Welcome to the Python Pizza Delivery System")
size = input("What size of the pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni in your pizza? Y or N: ")
cheese = input("Do you want extra cheese in your pizza? Y or N: ")

totalBill = 0

if size == "S":
    totalBill = 15;
elif size == "M":
    totalBill = 20;
elif size == "L":
    totalBill = 25;
else:
    print("Program End!")

if totalBill != 0:
    if pepperoni == "Y":
        if size == "S":
            totalBill = totalBill + 2;
        else:
            totalBill = totalBill + 3;
    elif pepperoni != "Y" and pepperoni != "N":
        print("No Pepperoni Ordered!")

    if cheese == "Y":
        totalBill = totalBill + 1;
    elif cheese != "Y" and cheese != "N":
        print("No Cheese Ordered!")

print("Total Bill: $" + str(totalBill))
