from possibilities import possibilities
from RandAns import Answeraabb
from correctAnswer import answerInput
def algoritme3():
    possibilitie=possibilities()
    guess=Answeraabb()
    correctAns = answerInput()
    print(guess)
    while True:
        tries += 1
        newLst = []
        if compair(guess, correctAns, tries) == True:
            break
        else:
            black, white = feedback(guess, correctAns)  # gives feedback for the guess compaired to the answer
            print(black, " black")
            print(white, "white")

            for item in possibilitie:
                blackP, whiteP = feedback(item,guess)  # deletes al items with the same feedback compaired to the guess of the computerer

                if black != blackP or white != whiteP:
                    newLst.append(item)  # First item removed the item but that made the item from possiblite jump up
                    # so it skipped some items.
        for item in newLst:  # this for loop is to prevent that

            delItem = item
            if delItem in possibilitie:
                possibilitie.remove(delItem)
            for i in possibilitie:
                for j in possibilitie:

                    if