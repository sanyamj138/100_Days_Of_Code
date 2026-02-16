import random

def gamestart():
    print("Welcome to the Black Jack Game!!!")

    playerCards = []
    for i in range(0, 2):
        playerCards.append(playerDeck())

    computerCards = []
    computerCards.append(computerDeck())

    playAhead = True
    totalPlayer = 0
    totalComputer = 0

    while playAhead:
        print('Your Cards: ', end ='')
        print(playerCards)
        print('Computer Cards: ', end='')
        print(computerCards)
        ans = input("Do you want to Pick Another Card? (Y/N): ")
        if ans == "Y" or ans == "y":
            playerCards.append(playerDeck())

        else:
            playAhead = False
            computerCards.append(computerDeck())
            print('Your Cards: ', end ='')
            print(playerCards)
            print('Computer Cards: ', end ='')
            print(computerCards)


    for i in range(len(playerCards)):
        totalPlayer = totalPlayer + playerCards[i]
    for i in range(len(computerCards)):
        totalComputer = totalComputer + computerCards[i]

    if totalPlayer > 21 and totalComputer > 21:
        ans1 = totalPlayer - 21
        ans2 = totalComputer - 21
        if ans1 > ans2:
            print("You Won!!!")
        elif ans1 < ans2:
            print("You Lost!!!")
        else:
            print("Tie!!!")

    elif totalPlayer <= 21 and totalComputer > 21:
        print("You Won!!!")

    elif totalPlayer > 21 and totalComputer <= 21:
        print("You Lost!!!")

    elif totalPlayer <= 21 and totalComputer <= 21:
        ans1 = 21 - totalPlayer
        ans2 = 21 - totalComputer
        if ans1 < ans2:
            print("You Won!!!")
        elif ans1 > ans2:
            print("You Lost!!!")
        else:
            print("Tie!!!")

    else:
        print("Tie!!!")

def playerDeck():
    return random.randint(1, 11)

def computerDeck():
    return random.randint(1, 11)


answer = input("Would you Like to Black Jack? (Y/N): ")
if answer == "Y" or answer == "y":
    gamestart()