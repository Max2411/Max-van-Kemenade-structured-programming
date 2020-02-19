from mastermind import playerGuessVScomputer
from mastermind import computerGuessVSplayer
from algoritme2_0 import delFirstStrat


def mastermind():
    while True:
        print("Game options:"
              "\n 1. You guess the code of the computer."
              "\n 2. The computer guesses your code."
              "\n 3. The computer guesses using the strat that deletes the first item"
              "\n 4. Quit Game",)
        gameChoice=int(input("Enter choice 1 or 2 or 3 or 4: "))
        if gameChoice==1:
            playerGuessVScomputer()
        elif gameChoice==2:
            computerGuessVSplayer()
        elif gameChoice==3:
            delFirstStrat()
        else:
            exit()
mastermind()