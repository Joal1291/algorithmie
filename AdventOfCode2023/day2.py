import openfile

filename = "day2.txt"
exerciceFile = openfile.readFile(filename)

arrayTest = [
"Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
"Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
"Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
"Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
"Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

def transformArrayToDict(array):
    arrayToDict = {}
    # pour une meilleur gestion des données je transforme le tableau en dictionnaire
    for line in array:
        game:str = line.split(':')
        find_nbr = game[0].split(' ')
        number:int = int(find_nbr[1])
        game_turn:str = game[1].strip().split(';')
        
        arrayToDict[number] = game_turn
    return arrayToDict

########################################################################
#                  Function écrite pour la partie 1                    #
########################################################################


def interpretLineSum(value):
    result:bool = True
    # valeur a ne pas depasser
    red:int = 12
    green:int = 13
    blue:int = 14
    # interprétation de chaque ligne en les découpant par manche
    for parts in value:
        part = parts.strip().split(',')
        # pour chaque manche je découpe le tirage de chaque couleu de cube et de leur nombre
        for i in part:
            obj = i.strip().split(' ')
            obj_number = int(obj[0])
            obj_color = obj[1]
            # ainsi j'interprete les résultat et je passe la variable result a false si une valeur passe au dessus des valeur données
            if obj_color == "red" and obj_number > red:
                result = False
            if obj_color == "green" and obj_number > green:
                result = False
            if obj_color == "blue" and obj_number > blue:
                result = False
    return result

def possibleGameCountSum(array):
    dictionnary = transformArrayToDict(array)
    result:int = 0
    # pour chaque ligne du dictionnaire je fais appel a une fonction qui permet l'interprétation des trois manche d'une game
    # et si la function d'interprétation renvoi true j'ajoute la valeur de la key au resultat final.
    for key, value in dictionnary.items():
        if interpretLineSum(value):
            result += int(key)

    print("Result :", result)

########################################################################
#                  Function modifer pour la partie 2                    #
########################################################################


def interpretLineProduct(value):
    # valeur des couleur qui sera changer pendant l'interprétation des cubes d'une manche
    redcac = 0
    greencac = 0
    bluecac = 0
    # interprétation de chaque ligne en les découpant par manche
    for parts in value:
        part = parts.strip().split(',')
        # pour chaque manche je découpe le tirage de chaque couleu de cube et de leur nombre
        for i in part:
            obj = i.strip().split(' ')
            obj_number = int(obj[0])
            obj_color = obj[1]
            # ainsi j'interprete les résultat et je passe la variable result a false si une valeur passe au dessus des valeur données
            if obj_color == "red" and obj_number > redcac:
                redcac = obj_number
            elif obj_color == "green" and obj_number > greencac:
                greencac = obj_number
            elif obj_color == "blue" and obj_number > bluecac:
                bluecac = obj_number
    
    return redcac*greencac*bluecac

def possibleGameCountProduct(array):
    dictionnary = transformArrayToDict(array)
    result:int = 0
    # pour chaque ligne du dictionnaire je fais appel a une fonction qui permet l'interprétation des trois manche d'une game
    # et si la function d'interprétation renvoi true j'ajoute la valeur de la key au resultat final.
    for key, value in dictionnary.items():
        if key:
            result += interpretLineProduct(value)

    print("Result :", result )

# possibleGameCountSum(exerciceFile)
possibleGameCountProduct(exerciceFile)