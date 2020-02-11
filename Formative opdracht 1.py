#'Ik heb sommige delen samen gedaan met Jelle.'
#Opdracht 1
import random
def pyramide():
    'bron; https://realpython.com/python-range/, stukje: Decrementing With range()'
    groote = int(input('voor groote van de pyramide in: '))
    print('Dit is de groote van uw pyramide: ',groote)

    for i in range(groote):
        print('*'*(i+1))
    for i in range(groote-1, 0,-1):
        print('*'*(i))

    return groote

#pyramide()
#Opdracht 2
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
#Opdracht 3
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
#binairVerschil([0,0,1,0,1,1,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1])
grootsteVerschil()
#count([0,9,8,2,2,6,7,8,9,1,3,4,5,2,3,4,5,6,7,8,9,0])
#momentVerschil()

#Opdracht 4
# Bron1: https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python
# Bron2: https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/
def reverseString():
    word= input("Typ the word you want to reverse: ")
    lenght=len(word)
    reveserdWord=word[lenght::-1]
    print(reveserdWord)

def reverseString2():
    word= input("Typ the word you want to reverse: ")
    rWord=""
    reverseInLst=[]
    i=len(word)

    while i>0:
        reverseInLst+=word[i-1]
        i=i-1

    for letter in reverseInLst:
        rWord+=letter
    print("Your word Reversed is: {}".format(rWord))



#reverseString2()



#reverseString()
#Opdracht 5
def sorteren():
    lst= [0,7,8,2,2,6,7,8,7,1,3,4,5,2,3,4,5,6,7,8,9,0]
    i = 0
    while i != len(lst)-1:
        if lst[i]>lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            i = 0
        else:
            i +=1
    print(lst)

sorteren()
#Opdracht 6
def gemiddelde():
    cijferlst = [0,9,8,2,2,6,7,8,9,1,3,4,5,2,3,4,5,6,7,8,9,0]
    som= sum(cijferlst)

    aantal = len(cijferlst)
    print("het gemiddelde van de cijferlijst = {}".format(som/aantal))


#gemiddelde()
def gemiddeldeMultipleLists():
    lst1=[0,9,8,2,2,6,7,8,9,1,3,4,5,2,3,4,5,6,7,8,9,0]
    lst2=[4,8,6,7,2,16,7,7,3,7,1,7,6,4,2,3,1,4,9,2,8,3]
    CombinedLst= lst1+lst2
    som=sum(CombinedLst)
    aantal=len(CombinedLst)
    print("The average number from all the numbers of the list = {}".format(som/aantal))
#gemiddeldeMultipleLists()

#Opdracht 7
def gokken(): # bron: https://www.programiz.com/python-programming/examples/random-number
    lst=[1,2,3,4,5,6,7,8,9,10]
    gok=int(input("Voor een getal tussen 1 en 10 in: "))
    randomNummer= random.choice(lst)
    while True:
        if gok == randomNummer:
            print("Je hebt goed gegokt.")
            return True
        else:
            print('je hebt het niet goed')
            gok = int(input("Voer volgende gok in tussen 1 en 10: "))
#gokken()

#Opdracht 8
def compressie(): 
    file= open('tekst.txt','r')
    tekst=file.readlines()
    list=[]
    compres = ""
    for rule in tekst:
        for letter in rule:
            list.append(letter)
    file.close()
    while '\n' in list:
        list.remove('\n')
    while' ' in list:
        list.remove(' ')
    for item in list:
        compres+=item
    file= open("compression.txt","w")
    file.write(compres)
    file.close()






compressie()
#Opdracht 9

#Opdracht 10
"""
def Fibonaci():
    '''
    De rij van Fibonacci is genoemd naar Leonardo van Pisa, bijgenaamd Fibonacci, die de rij noemt
    in zijn boek Liber abaci uit 1202. De rij begint met 0 en 1 en vervolgens is elk
    volgende element van de rij steeds de som van de twee voorgaande elementen. Bij de rij gebruiken we
    de notatie fn voor het aangeven van het n-de element van de rij. f9 is
    bijvoorbeeld gelijk aan 34. De eerste elementen van de rij zijn dan als volgt:
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584
    Implementeer een functie die fn uitrekent gegeven integer n. De functie moet recursief zijn.
    '''
    fn= int(input("Voor het getal in."))
    lst= [0,1]
    i=0
    if i==i:
        newItem=lst[i]+lst[i+1]
        lst.append(newItem)
        i+=1
    print("Op plek {} is het getal {}".format(fn,lst[i]))
Fibonaci()
"""
#Opdracht 11
#Opdracht 12
def fizzbuzz():
    for i in range(1,100):
        if i%3==0 and i%5==0:
            print('fizzbuzz')
        elif i%3==0:
            print('fizz')
        elif i%5==0:
            print('buzz')
        else:
            print(i)
#fizzbuzz()