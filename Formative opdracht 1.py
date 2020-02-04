'Ik heb sommige delen samen gedaan met Jelle.'

def pyramide():
    groote = int(input('voor groote van de pyramide in: '))
    print('Dit is de groote van uw pyramide: ',groote)
    for i in range(groote):
        print('*'*(i+1))
    for i in range(hoogte):
        print('*' * (item + 1))

    return groote

pyramide()
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

def count(lst):

    getal=int(input('Voor getal in dat u zoekt in de lijst: '))
    aantalGetal= lst.count(getal)
    print('Het getal {} komt {} keer voor in de lijst.'.format(getal,aantalGetal))
    return

def grootsteVerschil():
    lst = [0,3,6, 9, 8, 2, 2, 6, 7, 8, 9, 1, 3, 4, 5, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    lstverschil=[]
    print(lst)
    for item in lst:
        lstverschil.append(abs(lst[0]-lst[1]))
        lst.pop(0)

    verschil=max(lstverschil)
    print('Het maximale verschil tussen de lst: {}'.format(verschil))
    return

def count2(lst,getal):
    "deze count funtie is bijna hetzelfde alleen wordt wordt niet gevraagd om een getal en wordt het aantal niet weergeven."
    aantalGetal= lst.count(getal)
    return aantalGetal

def binairVerschil(lst):
    '''
     Schrijf een functie, die bepaalt of een gegeven lijst met alleen 1’en en 0’en aan de volgende eisen voldoet:
  - Het aantal enen is groter dan aan het aantal nullen
  - Er mogen niet meer dan 12 nullen zijn.
    '''
    nul = count2(lst,0)
    een = count2(lst,1)
    if een>nul and nul<12:
        print("Er zijn meer éénen dan nullen en er zijn niet meer dan 12 nullen")
    elif een>nul and  nul>=12:
        print("Er zijn meer éénen dan nullen, maar er zijn meer dan 12 nullen")
    else:
        print("Er zijn meer nullen dan éénen en er zijn meer dan 12 nullen")
    return
binairVerschil([0,0,1,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1])
#grootsteVerschil()
#count([0,9,8,2,2,6,7,8,9,1,3,4,5,2,3,4,5,6,7,8,9,0])
#momentVerschil()
