import random
gameList = ['Rock', 'Paper', 'Scissor']
i = 0
w = 0
l = 0
print("Welcome to the Rock Paper Scissor Game!")
while i < 3:
    rand = random.randint(0, 2)
    selectItem = input("What do you choose? Rock, Paper, or Scissor?\n")
    if(selectItem == "Rock" and rand == 1):
        print("You Lost! System Picked Paper")
        i = i + 1
        l = l + 1
    elif(selectItem == "Rock" and rand == 2):
        print("You Win! System Picked Scissor")
        i = i + 1
        w = w + 1
    elif(selectItem == "Paper" and rand == 0):
        print("You Win! System Picked Rock")
        i = i + 1
        w = w + 1
    elif(selectItem == "Paper" and rand == 2):
        print("You Lost! System Picked Scissor")
        i = i + 1
        l = l + 1
    elif(selectItem == "Scissor" and rand == 1):
        print("You Win! System Picked Paper")
        i = i + 1
        w = w + 1
    elif(selectItem == "Scissor" and rand == 0):
        print("You Lost! System Picked Rock")
        i = i + 1
        l = l + 1
    else:
        print("Tie!")

if l > w:
    print("You Lost! System Won")
else:
    print("You Win! System Lost")