from Feedback import feedback
from possibilities import possibilities
from RandAns import Answer

def delFirstStrat():# gem 5.789 with 1000 tries
    '''
    Checks the first item of all possibilities. If the first item is not the answer. Delete all the items with the same feedback
    compaired to the first item. Then repeat until it gets the answer.
    '''
    possibilitie=possibilities()

    possibilitie.sort()
    guess= possibilitie[0]#guesses the first item out the list.
    print("Enter the code you want the computer to guess on the next line.")
    answer= input("Choose 4 colours for your code((R)ed, (B)lue, (G)reen, (Y)ellow, (P)ink, (W)hite): ")
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
            black, white = feedback(guess, correctAns) #gives feedback compaired to the first item
            print(black, " black")
            print(white, "white")

            for item in possibilitie:

                blackP, whiteP = feedback(item,
                                          guess)  # deletes al items with the same feedback compaired to the guess of the computerer

                if black != blackP or white != whiteP:
                    newLst.append(item)
        for item in newLst:

            delItem = item
            if delItem in possibilitie:
                possibilitie.remove(delItem)


        print(possibilitie)

        print(len(possibilitie))
        print(guess)
        guess = possibilitie[0] # makes the first item of what is left the new guess. Restarts the loop

    return tries

def test():
    "First change correctAns from input to Answer"
    count=0
    tries=0
    for i in range(1000):
        Try=delFirstStrat()
        tries+=Try
        count+=1
    gem = tries/count
    print(gem)


