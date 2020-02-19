from mastermind import playerGuessVScomputer
from theSimpleStratWithRandom import computerGuessVSplayer
from algroritme2_0 import delFirstStrat
from algoritme1_0 import randomWithoutRepeatGuess
#from algoritme3_0


def mastermind():
    """
    The main menu to start the different types of games.
    """
    while True:
        print("Game options:"
              "\n 1. You guess the code of the computer."
              "\n 2. The computer guesses with a start guess of aabb."
              "\n 3. The computer guesses using the simple strat"
              "\n 4. The computer guesses random without repeat."
              "\n 5. Quit Game")
        gameChoice=int(input("Enter choice 1 or 2 or 3 or 4 or 5: "))
        if gameChoice==1:
            playerGuessVScomputer()
        elif gameChoice==2:
            computerGuessVSplayer()
        elif gameChoice==3:
            delFirstStrat()
        elif gameChoice==4:
            randomWithoutRepeatGuess()
        else:
            exit()
mastermind()