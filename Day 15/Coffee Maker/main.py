import coffee_data

def report(ini_milk, ini_water, ini_coffee):
    print("MILK: " + str(ini_milk))
    print("WATER: " + str(ini_water))
    print("COFFEE: " + str(ini_coffee))

def start_machine(ini_milk, ini_water, ini_coffee, total_bill):
    coffee_type = input("WHICH COFFEE TYPE WOULD YOU LIKE OR WOULD YOU LIKE TO GENERATE REPORT? (ESPRESSO, CAPPUCCINO, LATTE, REPORT): ")
    water = 0
    coffee = 0
    milk = 0
    price = 0

    if coffee_type.lower() == "espresso":
        water = coffee_data.Menu["espresso"]["Ingredients"]['Water']
        coffee = coffee_data.Menu["espresso"]["Ingredients"]['Coffee']
        price = coffee_data.Menu["espresso"]['Price']


    elif coffee_type.lower() == "cappuccino":
        milk = coffee_data.Menu["cappuccino"]["Ingredients"]['Milk']
        water = coffee_data.Menu["cappuccino"]["Ingredients"]['Water']
        coffee = coffee_data.Menu["cappuccino"]["Ingredients"]['Coffee']
        price = coffee_data.Menu["cappuccino"]['Price']

    elif coffee_type.lower() == "latte":
        milk = coffee_data.Menu["latte"]["Ingredients"]['Milk']
        water = coffee_data.Menu["latte"]["Ingredients"]['Water']
        coffee = coffee_data.Menu["latte"]["Ingredients"]['Coffee']
        price = coffee_data.Menu["latte"]['Price']

    elif coffee_type.lower() == "report":
        report(ini_milk, ini_water, ini_coffee)

    ini_water = ini_water - water
    ini_milk = ini_milk - milk
    ini_coffee = ini_coffee - coffee

    if (ini_milk < 0 or ini_water < 0 or ini_coffee < 0):
        if(ini_water < 0):
            print("WATER TOO LOW: " + water)
        elif(ini_milk < 0):
            print("MILK TOO LOW: " + milk)
        elif(ini_coffee < 0):
            print("COFFEE TOO LOW: " + coffee)
        return total_bill

    total_bill = total_bill + price

    order_again = input("WOULD YOU LIKE TO ORDER MORE OR PRINT REPORT (Y/N): ")
    if order_again.lower() == "y":
        return start_machine(ini_milk, ini_water, ini_coffee, total_bill)

    return total_bill

def refund(amt_received, total_bill):
    if(amt_received == total_bill):
        return 0
    elif(amt_received > total_bill):
        return amt_received - total_bill
    else:
        print("NOT SUFFICIENT AMOUNT!")
        return 0

start = input("DO YOU WANT COFFEE ? TYPE YES OR NO (Y/N): ")
if start == "Y" or start == "y":
    ini_coffee = 200
    ini_water = 1500
    ini_milk = 500
    total_bill = 0

    bill = start_machine(ini_milk, ini_water, ini_coffee, total_bill)

    print("COFFEE BILL: " + str(bill))
    amt_received = int(input("ENTER THE TOTAL AMOUNT RECEIVED: "))
    refund = refund(amt_received, bill)
    if refund == 0:
        print("THANK YOU! VISIT AGAIN!")
    else:
        print("HERE IS YOU CHANGE: " + str(refund))
