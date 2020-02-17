import random

def Answer():
    lst = ['R', 'B', 'G', 'Y', 'P', 'W']

    ranNum1=random.choice(lst)
    ranNum2=random.choice(lst)
    ranNum3=random.choice(lst)
    ranNum4=random.choice(lst)

    answer=ranNum1,ranNum2,ranNum3,ranNum4  #door getallen in list.
    return answer

def feedbackBlack(guessTuple,correctAns):
    white = 0
    black = 0
    if guessTuple[0] == correctAns[0]:
        black += 1
    else:
        black += 0

    if guessTuple[1] == correctAns[1]:
        black += 1
    else:
        black += 0

    if guessTuple[2] == correctAns[2]:
        black += 1
    else:
        black += 0

    if guessTuple[3] == correctAns[3]:
        black += 1
    else:
        black += 0


    return black
def feedbackWhite(guessTuple,correctAns):
    white=0
    black=feedbackBlack(guessTuple,correctAns)
    for i in correctAns:

        if i == guessTuple[0] or i == guessTuple[1] or i == guessTuple[2] or i == guessTuple[3]:
            white += 1
        else:
            white += 0
    white = white - black
    return white

def playerGuessVScomputer():
    correctAns = Answer()
    print(correctAns)
    rounds = 1

    while True:
        guess = input("Enter the letters of your 4 colours((R)ed, (B)lue, (G)reen, (Y)ellow, (P)ink, (W)hite): ")
        guess=guess.upper()
        if len(guess)==4:
            guessTuple=(guess[0],guess[1],guess[2],guess[3])




            if  rounds<10:
                black=feedbackBlack(guessTuple,correctAns)
                white=feedbackWhite(guessTuple,correctAns)


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

playerGuessVScomputer()


def computerGuessVSplayer():
    print("Enter the code you want the computer to guess on the next line.")
    answer= input("Choose 4 colours for your code((R)ed, (B)lue, (G)reen, (Y)ellow, (P)ink, (W)hite): ")
    answer =answer.upper()
    correctAns= (answer[0],answer[1],answer[2],answer[3])
    print(correctAns)

    return
computerGuessVSplayer()

def mastermind():

    while True:
        print("Game options:\n 1. You guess the code of the computer.\n 2. The computer guesses your code.\n 3. Quit Game",)
        gameChoice=int(input("Enter choice 1 or 2 or 3: "))
        if gameChoice==1:
            playerGuessVScomputer()
        elif gameChoice==2:
            computerGuessVSplayer()
        else:
            exit()
#mastermind()

def gokken(): # bron: https://www.programiz.com/python-programming/examples/random-number
    lst=[1,2,3,4,5,6]
    gok=int(input("Voor een getal tussen 1 en 6 in: "))
    randomNummer= random.choice(lst)
    while True:
        if gok == randomNummer:
            print("Je hebt goed gegokt.")
            return True
        else:
            print('je hebt het niet goed')
            gok = int(input("Voer volgende gok in tussen 1 en 10: "))