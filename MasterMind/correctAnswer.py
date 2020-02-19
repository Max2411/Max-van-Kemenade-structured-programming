def answerInput():
    print("Enter the code you want the computer to guess on the next line.")
    answer = input("Choose 4 colours for your code((R)ed, (B)lue, (G)reen, (Y)ellow, (P)ink, (W)hite): ")
    answer = answer.upper()

    if len(answer) != 4:
        print("Not the right lengt")
        return answerInput()
    else:
        answerTuple = (answer[0], answer[1], answer[2], answer[3])
    print(answerTuple)



    return answerTuple
answerInput()

def compair(guess,correctAns,tries):
    if guess == correctAns:
        print("-----------")
        print(guess)
        print("GG, it took {}".format(tries))
        print("----------")
        return True
    else:
        return False