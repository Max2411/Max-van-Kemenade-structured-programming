import random
def Answer():
    lst = ['R', 'B', 'G', 'Y', 'P', 'W']

    ranNum1=random.choice(lst)
    ranNum2=random.choice(lst)
    ranNum3=random.choice(lst)
    ranNum4=random.choice(lst)

    answer=ranNum1,ranNum2,ranNum3,ranNum4  #Makes a tuple of an random code from the 6 given colours.
    return answer


def Answeraabb():
    lst = ['R', 'B', 'G', 'Y', 'P', 'W']
    ranNum1 = ""
    ranNum2 = ""
    while ranNum1 == ranNum2:
        ranNum1 = random.choice(lst)
        ranNum2 = random.choice(lst)


    answer = ranNum1, ranNum1, ranNum2, ranNum2     # makes a tuple from the list af random colours with an combination of aabb.
                                                    # so the random answer alway exits out of 2 times 2 colours.
    return answer

def Answeraabc():
    lst = ['R', 'B', 'G', 'Y', 'P', 'W']
    ranNum1 = ""
    ranNum2 = ""
    ranNum3 = ""
    while ranNum1 == ranNum2 or ranNum1== ranNum3 or ranNum2==ranNum3:
        ranNum1 = random.choice(lst)
        ranNum2 = random.choice(lst)
        ranNum3 = random.choice(lst)


    answer = ranNum1, ranNum1, ranNum2, ranNum3     # makes a tuple from the list af random colours with an combination of aabb.
                                                    # so the random answer alway exits out of 2 times 2 colours.
    return answer