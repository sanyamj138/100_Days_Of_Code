import random

def mutate_list(list):
    list_temp = []
    newItem = 0
    for item in list:
        newItem = item * 2
        newItem += random.randint(1,3)
        list_temp.append(newItem)
    print(list_temp)

print("Welcome to the Mutate List!!")
num = int(input("Enter the Length of the List: "))
list = []
for i in range(0, num):
    numNew = int(input("Add the Number: "))
    list.append(numNew)

mutate_list(list)