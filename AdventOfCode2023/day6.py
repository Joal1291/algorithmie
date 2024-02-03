import openfile
import re

exercice = openfile.readFile("day6.txt")
exerciceTest = openfile.readFile("day6test.txt")

def getInfo(array):
    array1 = []
    array2 = []
    for lines in array:
        line = lines.split(':')
        name = line[0]
        numbers = line[1].strip().split()
        if name == "Time":
            for i in numbers:
                array1.append(int(i))
        else:
            for i in numbers:
                array2.append(int(i))
    return array1, array2  

###################################################################
#                          Part 1 and 2                           #
###################################################################

def main1(array):
    temps, distances = getInfo(array)
    resultat = 1

    for temp, distance in zip(temps, distances):
        courseRemporter = 0
        for vitesse in range(1, temp+1):
            distanceParcouru = (temp-vitesse)*vitesse
            if distanceParcouru > distance:
                courseRemporter += 1
        resultat *= courseRemporter
    
    print("Resultat: ", resultat)

main1(exercice)