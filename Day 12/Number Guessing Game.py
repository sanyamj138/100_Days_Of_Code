import random

def playGame():
    print("Choosing a Number Between 1 and 100")
    guessCom = random.randint(1,100)
    difficult = input("Choose a Difficulty Level: Easy, Medium, Hard: ")
    if difficult == "Easy" or difficult == "easy" or difficult == "EASY":
        ran = 10
    elif difficult == "Medium" or difficult == "medium" or difficult == "MEDIUM":
        ran = 7
    elif difficult == "Hard" or difficult == "hard" or difficult == "HARD":
        ran = 5
    else:
        ran = 0

    i = ran

    while i > 0:
        guess = int(input("Guess a Number: "))
        if guess == guessCom:
            print("Correct!")
            i = 0
        elif guess < guessCom:
            print("You Have " + str(i) + " Attempts Left!")
            print("Too Low!")
            i -= 1
        elif guess > guessCom:
            print("You Have " + str(i) + " Attempts Left!")
            print("Too High!")
            i -= 1

print("Welcome to Number Guessing Game")
yesNo = input("Do You Want to Play Guessing Game? (Y/N): ")
if yesNo == "y" or yesNo == "Y":
    playGame()