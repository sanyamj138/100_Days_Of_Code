# First Step -> Create a Word List
# Second Step -> Select a Random Word
# Third Step -> Now ask user for a letter
# Fourth Step -> If the letter in the word enter its position

import random

wordList = ['camel', 'goat', 'horse', 'cat', 'dog']


def hangman(word):
    randomWord = random.choice(wordList)

    for i in range(0, 5):
        letterAsk = input("Guess a letter: ")
        for j in range(len(randomWord)):
            if (letterAsk == randomWord[j]):
