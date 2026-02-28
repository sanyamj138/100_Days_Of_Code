import coffee_data

def start_machine(ini_milk, ini_water, ini_coffee, total_bill):
    coffee_type = input("WHICH COFFEE TYPE WOULD YOU LIKE ? (ESPRESSO, CAPPUCCINO, LATTE): ")
    water = 0
    coffee = 0
    milk = 0

    if coffee_type.lower() == "espresso":
        water = coffee_data.Menu["espresso"]["Ingredients"]['Water']
        coffee = coffee_data.Menu["espresso"]["Ingredients"]['Coffee']

    elif coffee_type.lower() == "cappuccino":
        milk = coffee_data.Menu["cappuccino"]["Ingredients"]['Milk']
        water = coffee_data.Menu["cappuccino"]["Ingredients"]['Water']
        coffee = coffee_data.Menu["cappuccino"]["Ingredients"]['Coffee']

    elif coffee_type.lower() == "latte":
        milk = coffee_data.Menu["latte"]["Ingredients"]['Milk']
        water = coffee_data.Menu["latte"]["Ingredients"]['Water']
        coffee = coffee_data.Menu["latte"]["Ingredients"]['Coffee']

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

    total_bill = total_bill + coffee_data.Menu[coffee_type]['Price']

    





start = input("DO YOU WANT COFFEE ? TYPE YES OR NO (Y/N): ")
if start == "Y" or start == "y":
    ini_coffee = 200
    ini_water = 1500
    ini_milk = 500
    total_bill = 0
    start_machine(ini_milk, ini_water, ini_coffee, total_bill)