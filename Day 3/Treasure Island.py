print("Welcome to the Treasure Island!")
print("Your Mission is to Find the Treasure.")
opt1 = input("You are at the Cross Road. Where do you want to go Left or Right? L or R: ")
if opt1 == "L":
    opt2 = input("You've come to a Lake. Would you like to Swim or Wait? S or W: ")
    if opt2 == "W":
        print("Boat Picked You Up and Dropped you on an Island. There is a House which has 3 Doors that is Red, Yellow, and Blue")
        opt3 = input("Select any one Door. R, Y or B: ")
        if opt3 == "R":
            print("Burned by Fire!")
            print("Game Over!")
        elif opt3 == "Y":
            print("You Won!")
            print("Treasure is Yours!")
        elif opt3 == "B":
            print("Beaten to Death by Beasts!")
            print("Game Over!")
        else:
            print("Game Over!")
    else:
        print("Attacked by Trout!")
        print("Game Over!")
else:
    print("You Fall into a Hole!")
    print("Game Over!")