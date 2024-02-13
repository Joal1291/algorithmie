import re
from collections import Counter # vas me permettre de compter les iteration d'un caractere dans une chaine de caractere
import openfile

from collections import Counter

exercice = openfile.readFile("day7.txt")
exerciceTest = openfile.readFile("day7test.txt")

### 250898830 ###
#######################################################################
#                                Part 1                               #
#######################################################################

####################################
# Type du plus fort au plus faible #
####################################
# 5 carte du même type
# 4 caret du même type
# full house
# 3 cartes du même type
# 2 paire
# 1 paire
# carte forte

# si deux main sont de même niveau comparer les carte de la premiere vers la 5.
# La main qui l'emporte et celle avec la carte la plus forte
# si par exemple la carte n°1 est de même type il faut donc comparer la deuxieme etc...
# plus la main est forte plus le rank est élevé

## LET'S GO.

# tableau des carte
five = []
four = []
fullhouse = []
three = []
twoandtwo = []
two = []
high = []

# valeur
topcard ={"2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}

def compareMain(main, mainInArray):
    count = 0
    for i in mainInArray:
        char = topcard[i]
        mainchar = topcard[main[count]]
        if char == mainchar :
            count += 1
            continue
        elif mainchar < char:
            return False
        elif mainchar > char:
            return True

def storage(main, line, arrayToStoreIn):

    if len(arrayToStoreIn) == 0: 
        arrayToStoreIn.insert(0, line)
        return
    
    else:
        for lines in arrayToStoreIn:
            mainInArray = lines[0]
            index = arrayToStoreIn.index(lines)
            check = compareMain(main, mainInArray)
            if check and index == len(arrayToStoreIn)-1:
                arrayToStoreIn.append(line)
                return
            elif check:
                continue
            else: 
                arrayToStoreIn.insert(index, line)
                return
                       
def calcul():
    res = 0
    count = 1
    for line in high: res +=int(line[1])*count; count +=1
    for line in two:res +=int(line[1])*count; count +=1
    for line in twoandtwo: res +=int(line[1])*count; count +=1
    for line in three: res +=int(line[1])*count; count +=1
    for line in fullhouse: res +=int(line[1])*count; count +=1
    for line in four: res +=int(line[1])*count; count +=1
    for line in five: res +=int(line[1])*count; count +=1
    return res

def findmain(array):
    for lines in array:
        line = lines.split()
        main = line[0]
        counter = Counter(main)
        # Counter permet dans ce cas de compter le nombre d'itération de chaque caractere de la main
        paire = counter.most_common(2)
        # most_common est un methode qui permet de récuperer les paire de clef valeur d'un résultat de Counter()
        # le chiffre préciser a l'intérieur des parenthése precise le nombre de paire clef valeur que l'on veut obtenir
        valeur1 = paire[0][1]
        if valeur1 == 5:
            storage(main, line, five)
            continue
        valeur2 = paire[1][1]
        if valeur1 == 4:storage(main, line, four)
        elif valeur1 == 3 and valeur2 == 2:storage(main, line, fullhouse)
        elif valeur1 == 3:storage(main, line, three)
        elif valeur1 == 2 and valeur2 == 2:storage(main, line, twoandtwo)
        elif valeur1 == 2:storage(main, line, two)
        else: storage(main, line, high)
    print("Resultat:",calcul())

findmain(exercice)
# print((1*765)+(2*220)+(3*28)+(4*483)+(5*684))