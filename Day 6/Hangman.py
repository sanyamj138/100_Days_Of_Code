# First Step -> Create a Word List
# Second Step -> Select a Random Word
# Third Step -> Now ask user for a letter
# Fourth Step -> If the letter in the word enter its position

import random

wordList = ['camel', 'goat', 'horse', 'cat', 'dog']


def hangman():
    randomWord = random.choice(wordList)
    listCollect = ''
    lives = 5

    while lives != 0:
        letterAsk = input("Guess a letter: ")
        check = False

        for j in range(0, len(randomWord)):
            if (letterAsk == randomWord[j]):
                listCollect = listCollect + letterAsk
                check = True
            else:
                listCollect = listCollect + '_'

        if check == True:
            print(listCollect)

        if check == False:
            print("You guessed " + letterAsk + " and it's not in the word. You Lost a Life!" )
            lives = lives - 1
            print(str(lives) + " Out of 5 Lives Left")


hangman()