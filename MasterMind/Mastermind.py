import random

def Answer():
#    lst = ['1', '2', '3', '4', '5', '6']
    lst = [1, 2, 3, 4, 5, 6]
    ranNum1=random.choice(lst)
    ranNum2=random.choice(lst)
    ranNum3=random.choice(lst)
    ranNum4=random.choice(lst)
#    answer=ranNum1+ranNum2+ranNum3+ranNum4     'door strings'
    answer=ranNum1,ranNum2,ranNum3,ranNum4  #door getallen in list.
    print(answer)

def mastermind():
    correctAns = Answer()
    while True:
        print("Game options:\n 1. You guess the code of the computer.\n 2. The computer guesses your code.\n 3. Quit Game",)
        gameChoice=int(input("Enter choice 1 or 2 or 3: "))
        if gameChoice==1:
            playerGuessVScomputer()
        elif gameChoice==2:
            computerGuessVSplayer()
        else:
            exit()


    guess=int(input("Enter your guess with numbber from 1 to 6: "))
    print(correctAns)
mastermind()

def playerGuessVScomputer():


def computerGuessVSplayer():


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