def pyramide():
    groote = int(input('voor groote van de pyramide in: '))

    print('*'*groote)





    return groote

#pyramide()
def verschilLengte():
    zin1 = input('Typ hier zin 1: ')
    zin2 = input('Typ hier zin 2: ')

    if len(zin1)>len(zin2):
        verschil= len(zin1)-len(zin2)
        print("Het verschil in lengte is: ",verschil)
    else:
        verschil= len(zin2)-len(zin1)
        print("Het verschil in lengte is: ",verschil)
    return
#verschilLengte()

def momentVerschil():
    zin1 = input('Typ hier zin 1: ')
    zin2 = input('Typ hier zin 2: ')
    i = 0
    lst1=[]
    lst2=[]
    for letter in zin1:
        lst1.append(letter)
    for letter2 in zin2:
        lst2.append(letter2)

    while lst1[0]==lst2[0]:
        i += 1
        lst1.pop(0)
        lst2.pop(0)
        if len(lst1)==0 or len(lst2)==0:
            break
    print(i+1)
    return

def count():
    lst=[0,9,8,2,2,6,7,8,9,1,3,4,5,2,3,4,5,6,7,8,9,0]
    getal=int(input('Voor getal in dat u zoekt in de lijst: '))
    aantalGetal= lst.count(getal)
    print('Het getal {} komt {} keer voor in de lijst.'.format(getal,aantalGetal))
    return

count()
#momentVerschil()
