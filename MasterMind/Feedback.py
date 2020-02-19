def feedbackBlack(guess, correctAns):
    """compairs every colour of the guess with the colour of the answer according to the place they are in.
    So the first is compaired with  first colour of the answer
    """
    black = 0
    j=0
    guess=list(guess)
    correctAns=list(correctAns)
    for i in guess:
        if i == correctAns[j]:
            black+=1
        j+=1
    return black

def feedbackWhite(guess, correctAns):
    """
    Compairs if an colour from your guess is in the answer. If the colour is in the answer, white will go up and the colour is
    removed from the list so an coulr can't be compaired 2 times.
    """
    white=0

    guess=list(guess)
    correctAns=list(correctAns)
    for i in guess:
        if i in correctAns:
            white+=1
            correctAns.remove(i)
    return white

def feedback(guess, correctAns): #De feedback funcites zijn verbeterd met behulp van jelle.
    """
    Gives the black and white pins from the previous functions. and subtracts the black pins from the white pins before return these,
    because the black pins werent subrtacted for the white pins.
    """
    black=feedbackBlack(guess, correctAns)
    white= feedbackWhite(guess, correctAns)
    white=white-black
    return black,white