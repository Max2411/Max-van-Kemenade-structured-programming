import random
from RandAns import Answeraabb
from possibilities import possibilities
from Feedback import feedback
from RandAns import Answer


def computerGuessVSplayer():# gem is 4.584 with 1000 tries
    "Deletes everything that doesnt get the same feedback. then picks a random number from the list"
    possibilitie=possibilities()
    guess= Answeraabb()
    print("Enter the code you want the computer to guess on the next line.")
    answer= input("Choose 4 colours for your code((R)ed, (B)lue, (G)reen, (Y)ellow, (P)ink, (W)hite): ")# the code the computer must guess
    answer =answer.upper()
    correctAns= (answer[0],answer[1],answer[2],answer[3])
    print(correctAns)
    print(guess)

    tries=0
    while True:
        tries += 1
        newLst=[]
        if guess == correctAns:
            print("-----------")
            print(guess)
            print("GG, it took {}".format(tries))
            print("----------")
            break
        else:
            black, white = feedback(guess, correctAns)#gives feedback for the guess compaired to the answer
            print(black, " black")
            print(white, "white")

            for item in possibilitie:

                blackP,whiteP=feedback(item,guess) # deletes al items with the same feedback compaired to the guess of the computerer

                if black!=blackP or white!=whiteP:
                    newLst.append(item) # First item removed the item but that made the item from possiblite jump up
                                        # so it skipped some items.
        for item in newLst:       # this for loop is to prevent that

            delItem=item
            if delItem in possibilitie:

                possibilitie.remove(delItem)


        print(possibilitie)

        print(len(possibilitie))
        print(guess)
        guess = random.choice(possibilitie)# new guess out of leftover possibilities. Restarts the loop

    return tries

def test2():
    "First change correctAns from input to Answer"
    count=0
    tries=0
    for i in range(1000):
        Try=computerGuessVSplayer()
        tries+=Try
        count+=1
    gem = tries/count
    print(gem)

