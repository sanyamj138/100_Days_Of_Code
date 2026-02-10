import random

wordList = ['camel', 'goat', 'horse', 'cat', 'dog']
randomWord = random.choice(wordList)
lives = 5
listCollect = []
for i in range(0,len(randomWord)):
    listCollect.append('_')

while lives != 0:
    finalList = ''
    letterAsk = input("Guess a letter: ")
    check = False
    for i in range(0,len(randomWord)):
        if (letterAsk == randomWord[i]):
            listCollect[i] = letterAsk
            check = True

    if check == False:
        lives -= 1
        print("You guessed " + letterAsk + " and it's not in the word. You Lost a Life!")
        print(str(lives) + " Out of 5 Lives Left")
    else:
        for i in range(0,len(randomWord)):
            finalList += listCollect[i]
        print(finalList)

print("Game Over!")