import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lettersCap = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
specialChar = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '.']

print("Welcome to Password Generator!")
letter = int(input("Number of Letters you want in the Password: "))
letterCap = int(input("Number of Capital Letters you want in the Password: "))
number = int(input("Number of Numbers you want in the Password: "))
special = int(input("Number of Special Characters you want in the Password: "))

list1 = []

for i in range(letter):
    list1.append(random.Random(letters))

print()