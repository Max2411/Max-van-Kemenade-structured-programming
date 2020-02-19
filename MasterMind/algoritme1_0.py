
from RandAns import Answer


def randomWithoutRepeatGuess():
    """
    Does a random guess, then saves this guess in a list. If the random function gets the same guess again.
    it wil try again until there is a unique guess. This caps the guess limit to 1296.
    """
    print("Enter the code you want the computer to guess on the next line.")
    answer = input("Choose 4 colours for your code((R)ed, (B)lue, (G)reen, (Y)ellow, (P)ink, (W)hite): ")  # the code the computer must guess
    answer = answer.upper()
    correctAns = (answer[0], answer[1], answer[2], answer[3])
    print(correctAns)
    lst=[]
    tries=0
    while True:
        guess = Answer()
        if guess not in lst:
            lst.append(guess)
            tries += 1
            if guess == correctAns:
                print("-----------")
                print(guess)
                print("GG, it took {}".format(tries))
                print("----------")
                break
        else:
            print("This guess was already in list")


    return
algrotime1_0()