def feedbackBlack(guess, correctAns):
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
    white=0
    j=0
    guess=list(guess)
    correctAns=list(correctAns)
    for i in guess:
        if i in correctAns:
            white+=1
            correctAns.remove(i)
    return white

def feedback(guess, correctAns):
    "De feedback funcites zijn verbeterd met behulp van jelle"
    black=feedbackBlack(guess, correctAns)
    white= feedbackWhite(guess, correctAns)
    white=white-black
    return black,white