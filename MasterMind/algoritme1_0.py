from RandAns import Answer
from correctAnswer import answerInput
from correctAnswer import compair

def randomWithoutRepeatGuess():# gem 650. Totaal niet efficient.
    """
    Does a random guess, then saves this guess in a list. If the random function gets the same guess again.
    it wil try again until there is a unique guess. This caps the guess limit to 1296.
    """
    correctAns = answerInput()

    lst=[]
    tries=0
    while True:
        guess = Answer()
        if guess not in lst:
            lst.append(guess)
            tries += 1
            if compair(guess, correctAns, tries) == True:
                break

    return tries

def test():
    "First change correctAns from input to Answer"
    count=0
    tries=0
    for i in range(1000):
        Try=randomWithoutRepeatGuess()
        tries+=Try
        count+=1
    gem = tries/count
    print(gem)
