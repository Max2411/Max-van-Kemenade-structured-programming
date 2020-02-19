from Feedback import feedback
from possibilities import possibilities

def delFirstStrat():# the simple strat
    '''
    Checks the first item of all possibilities. If the first item is not the answer. Delete all the items with the same feedback
    compaired to the first item. Then repeat until it gets the answer.
    '''
    possibilitie=possibilities()

    possibilitie.sort()
    guess= possibilitie[0]
    print("Enter the code you want the computer to guess on the next line.")
    answer= input("Choose 4 colours for your code((R)ed, (B)lue, (G)reen, (Y)ellow, (P)ink, (W)hite): ")
    answer =answer.upper()
    correctAns= (answer[0],answer[1],answer[2],answer[3])
    print(correctAns)
    print(guess)

    tries=0
    while True:
        tries += 1
        if guess == correctAns:
            print("-----------")
            print(guess)
            print("GG, it took {}".format(tries))
            print("----------")
            break
        else:
            black, white = feedback(guess, correctAns)
            print(black, " black")
            print(white, "white")
            for item in possibilitie:

                blackP,whiteP=feedback(item,guess)
                if black!=blackP or white!=whiteP:
                    possibilitie.remove(item)


        print(possibilitie)

        print(len(possibilitie))
        print(guess)
        if guess==correctAns:
            print("gg")
            break
        guess = possibilitie[0]

    return
delFirstStrat()

