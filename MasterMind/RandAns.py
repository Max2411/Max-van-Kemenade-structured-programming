import random
def Answer():
    lst = ['R', 'B', 'G', 'Y', 'P', 'W']

    ranNum1=random.choice(lst)
    ranNum2=random.choice(lst)
    ranNum3=random.choice(lst)
    ranNum4=random.choice(lst)

    answer=ranNum1,ranNum2,ranNum3,ranNum4  #door getallen in list.
    return answer
def Answeraabb():
    lst = ['R', 'B', 'G', 'Y', 'P', 'W']

    ranNum1 = random.choice(lst)
    ranNum2 = random.choice(lst)


    answer = ranNum1, ranNum1, ranNum2, ranNum2  # door getallen in list.
    return answer