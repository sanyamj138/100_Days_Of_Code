# First Step -> Create a Word List
# Second Step -> Select a Random Word
# Third Step -> Now ask user for a letter
# Fourth Step -> If the letter in the word enter its position

import random

wordList = ['camel', 'goat', 'horse', 'cat', 'dog']


def hangman():
    randomWord = random.choice(wordList)
    listCollect = ''

    for i in range(0, 1):
        letterAsk = input("Guess a letter: ")
        for j in range(0, len(randomWord)):
            if (letterAsk == randomWord[j]):
                listCollect = listCollect + letterAsk
            else:
                listCollect = listCollect + '_'


    print(listCollect)

hangman()