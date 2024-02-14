import re
from collections import Counter # vas me permettre de compter les iteration d'un caractere dans une chaine de caractere
import openfile

from collections import Counter

exercice = openfile.readFile("day7.txt")
exerciceTest = openfile.readFile("day7test.txt")

### 250898830 ### 252127335 ###
#######################################################################
#                               Part 2                                #
#######################################################################

# le "J" est maintenant un joker il peut etre utiliser pour créer une main plus forte
# exemple 'TJ55T' qui est une double paire  peut devenir 'TT55T' un full house sans en changer le caractere
# pour pallier a ce fort avantage on nous dit que maintenant la valeur de J est inférieur a toute les autre carte
# donc bien que celle ci ajoute un avantage lors du trie dans le tableau le J doit passer en dernier
# exemple 'TJT55' contre 'T5J5T'. 'T5J5T'sera considérer comme plus forte car le 5 est au dessus du J donc elle aura un rank plus elever.

#LET'S GO
# tableau des carte
five = []
four = []
fullhouse = []
three = []
twoandtwo = []
two = []
high = []
pasclasser = []

# valeur a comparer
topcard ={"2": 3, "3":4, "4":5, "5":6, "6":7, "7":8, "8":9, "9":10, "T":11, "J":2, "Q":12, "K":13, "A":14}


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
        jack = main.count('J')
        # Counter permet dans ce cas de compter le nombre d'itération de chaque caractere de la main
        paire = counter.most_common(2)
        # most_common est un methode qui permet de récuperer les paire de clef valeur d'un résultat de Counter()
        # le chiffre préciser a l'intérieur des parenthése precise le nombre de paire clef valeur que l'on veut obtenir
        clef1, valeur1 = paire[0][0], paire[0][1]
        if valeur1 == 5:
            storage(main, line, five)
            continue
        valeur2 = paire[1][1]

        valeur3 = valeur1 + jack

        if clef1 == 'J' and valeur1 == 2 and valeur2 == 1:
            storage(main, line, three)
            continue
        if clef1 == 'J':
            valeur3 = valeur2 + jack 
        
        if valeur3 == 5:
            storage(main, line, five)
            continue

        if valeur3  == 4:storage(main, line, four)
        elif valeur3 == 3 and valeur2 == 2:storage(main, line, fullhouse)
        elif valeur3 == 3: storage(main, line, three)
        elif valeur3 == 2 and valeur2 == 2:storage(main, line, twoandtwo)
        elif valeur3 == 2:storage(main, line, two)
        elif valeur3 == 1: storage(main, line, high)
        else:storage(main, line, pasclasser)
    print("Resultat:",calcul())

findmain(exercice)