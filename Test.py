#lst = ['R', 'B', 'G', 'Y', 'P', 'B']
#mogelijkheden=[]
#for i in lst:
#    for j in lst:
#        for k in lst:
#            for l in lst:
from itertools import permutations

#bron: https://www.geeksforgeeks.org/permutation-and-combination-in-python/
#bron: https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
# Get all permutations of [1, 2, 3]
perm = permutations(['R','R','R','R', 'B','B','B','B', 'G','G','G','G', 'Y','Y','Y','Y', 'P','P','P','P', 'W','W','W','W'],4)
mogelijkheid=[]
mogelijkheden=[]
# Print the obtained permutations
item=0
item2=0
for i in list(perm):
    mogelijkheid.append(i)
    item+=1
print(item)
for j in mogelijkheid:
    if j not in mogelijkheden:
        mogelijkheden.append(j)
    item+=1
    item2+=1
    print(item)
    print(item2)
print(mogelijkheden)
print(len(mogelijkheden))
\



for item in correctAns:
    if item in guess:
        white += 1
for j in guess:
    for i in correctAns:
        if j == i:
            black += 1





   while True:
        guessInput = input("Enter the letters of your 4 colours((R)ed, (B)lue, (G)reen, (Y)ellow, (P)ink, (W)hite): ")
        guess=guessInput.upper()
        guessTuple=(guess[0],guess[1],guess[2],guess[3])
        print(guessTuple)
        white = 0
        black = 0
        if len(guess)==4 and rounds<10:
            if guessTuple[0]==correctAns[0]:
                black+=1
            elif guessTuple[0] in correctAns:
                white+=1
            else:
                white+=0

            if guessTuple[1]==correctAns[1]:
                black+=1
            elif guessTuple[1] in correctAns:
                white+=1
            else:
                white+=0

            if guessTuple[2]==correctAns[2]:
                black+=1
            elif guessTuple[2] in correctAns:
                white+=1
            else:
                white+=0

            if guessTuple[3]==correctAns[3]:
                black+=1
            elif guessTuple[3] in correctAns:
                white+=1
            else:
                white+=0
            rounds+=1

            if black==4:
                print("You have won")
            else:
                print("Your guess {}.\n {} white pins, {} black pins.".format(guessInput,white,black)) #  i.p.v. twee zwart en 0 wit

        elif rounds==10:
            print("GAME OVER!")
            break