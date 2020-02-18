from mastermind import playerGuessVScomputer
from mastermind import computerGuessVSplayer


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
mastermind()