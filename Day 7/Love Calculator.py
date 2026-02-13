name1 = input("Give me your Name: ")
name2 = input("Give me your Lover's Name: ")
count1 = 0
count2 = 0

for i in range(len(name1)):
    if name1[i] == 't' or name1[i] == 'r' or name1[i] == 'u' or name1[i] == 'e' or name1[i] == 'T' or name1[i] == 'R' or name1[i] == 'U' or name1[i] == 'E':
        count1 += 1

for i in range(len(name2)):
    if name2[i] == 't' or name2[i] == 'r' or name2[i] == 'u' or name2[i] == 'e' or name2[i] == 'T' or name2[i] == 'R' or name2[i] == 'U' or name2[i] == 'E':
        count1 += 1

for i in range(len(name1)):
    if name1[i] == 'l' or name1[i] == 'o' or name1[i] == 'v' or name1[i] == 'e' or name1[i] == 'L' or name1[i] == 'O' or name1[i] == 'V' or name1[i] == 'E':
        count2 += 1

for i in range(len(name2)):
    if name2[i] == 'l' or name2[i] == 'o' or name2[i] == 'v' or name2[i] == 'e' or name2[i] == 'L' or name2[i] == 'O' or name2[i] == 'V' or name2[i] == 'E':
        count2 += 1

total = count1 * 10 + count2

print("Total Love Score: " + str(total))
