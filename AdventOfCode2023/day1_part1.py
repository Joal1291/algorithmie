import openfile 


def sumNumberInAWord(array):
    # variable de récupération des tout les digits dans un mot
    concatDigit = ""
    # résultat de tout concat obtenue
    result_to_return = 0

    for word in array:
        for char in word:
            if char.isdigit():
                # ajout de chaque digit a la chaine de caractere
                concatDigit += char
        # prise en compte du premier et du dernier digit dans la chaine concat
        concatDigit = concatDigit[0] + concatDigit[-1:]
        # addition du nombre obtenu au resultat final
        result_to_return += int(concatDigit)
        # remise a zéro du concat
        concatDigit = ""
    
    print(result_to_return)

sumNumberInAWord(openfile.readFile())