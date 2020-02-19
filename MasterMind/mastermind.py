import random
from Feedback import feedback
from RandAns import Answer
from RandAns import Answeraabb
from possibilities import possibilities

def playerGuessVScomputer():
    correctAns = Answer()
    print(correctAns)
    rounds = 1

    while True:
        guess = input("Enter the letters of your 4 colours((R)ed, (B)lue, (G)reen, (Y)ellow, (P)ink, (W)hite): ")
        guess=guess.upper()
        if len(guess)==4:
            guessTuple=(guess[0],guess[1],guess[2],guess[3])

            if  rounds<11: #Van "<10" naar "<11" omdat je anders maar 9 ronden hebt
                black,white=feedback(guessTuple,correctAns)
                rounds += 1
                if black == 4:
                    print("You have won")
                    break
                else:
                    print("Your guess {}.\n {} white pins, {} black pins.".format(guessTuple, white, black))
                    print("------------------------------------")# maakt de console overzichtelijker.



            else:
                print("GAME OVER!")
                break

        else:
            print("The lenght of your guess is not 4.\n Guess again with code from 4 letters of the colour code you want to guess.")


def computerGuessVSplayer():# the simple strat
    possibilitie=possibilities()

    possibilitie.sort()
    guess= Answeraabb()
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
        guess = random.choice(possibilitie)

    return
computerGuessVSplayer()