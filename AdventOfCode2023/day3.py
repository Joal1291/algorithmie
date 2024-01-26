import openfile

filename = "day3.txt"
exerciceFile = openfile.readFile(filename)

arrayTest = [
"467..114...............................................",
"...*...................................................",
"..35..633..............................................",
"......#................................................",
"617*...................................................",
".....+.58..............................................",
"..592..................................................",
"......755..............................................",
"...$.*.................................................",
".664.598...............................................",

]


     #  #               ################
      #   #           ###         #    ###
        #   #        ##           #      ##
          #   #     ###################################
            #   #   ##    ####               ###      ##
              #  #####   #    #             #   #     #
                    #####  ##  #############  #  ######
                         ####                ###
                         ##                  #
######################################################################
#                            Engine Game                             #
######################################################################

######################################################################
#                               Utils                                #
######################################################################

#Varriable
notSymb = ".1234567890"

######################################################################
#                     Function pour la partie 1                      #
######################################################################

## Fonction permettant de pouvoir valider un chiffre, a savoir si il y a un symbole au tour.
def numberValidation(lineindex, nbrindex, array):
    row = lineindex
    col = nbrindex
    height = len(array)
    width = len(array[row])
    #Digonale haut gauche
    if str(array[(row-1)%height][(col-1)%width]) not in notSymb:
        print(str(array[(row-1)%height][(col-1)%width]))
        print(array[row][col], "\n---------------------")
        return True
    #Haut
    if str(array[(row-1)%height][col]) not in notSymb:
        return True
    #Diagonal haut droite
    if str(array[(row-1)%height][(col+1)%width]) not in notSymb:
        return True
    #Diagonal bas droite
    if str(array[(row+1)%height][(col+1)%width]) not in notSymb:
        return True
    #Bas
    if str(array[(row+1)%height][col]) not in notSymb:
        return True
    #Diagonal bas gauche
    if str(array[(row+1)%height][(col-1)%width]) not in notSymb:
        return True
    #Gauche
    if str(array[row][(col-1)%width]) not in notSymb:
        return True
    return False

## Fonction qui permet de determiner si le caractere a la suite est un symbole.
## j'ai fait de fonction différente pour la verification de droite afin de gérer plus facilement les cas.
def thereIsSymb(lineindex, nbrindex, array):
    row = lineindex
    col = nbrindex
    width = len(array[0])
    if str(array[row][(col+1)%width]) not in notSymb:
        return True
    return False

## Function de vrification du caractere suivant a savoir si c'est un point ou non,
def thereIsDot(lineindex, nbrindex, array):
    row = lineindex
    col = nbrindex
    width = len(array[row])
    if col == width-1:
        return True
    elif str(array[row][(col+1)]) == ".":
        return True
    return False

## Permet de créer les nombre a réunir pour l'addition final.
def main(array):
    arrayOfNumber = []
    validation = False
    number = ""
    
    for row in range(0, len(array)):
        for col in range(0, len(array[row])):
            char = array[row][col]
            if char.isdigit():
                number += char
                if validation != True:
                    if numberValidation(row, col, array):
                        validation = True
                if thereIsSymb(row, col, array):
                    arrayOfNumber.append(number)
                    number = ""
                if thereIsDot(row, col, array):
                    if validation == True:
                        arrayOfNumber.append(number)
                        number = ""
                        validation = False
                    if validation == False:
                        number = ""
    print('Result:', sum(int(i) for i in arrayOfNumber))

# main(arrayTest) 
main(exerciceFile)
# print(exerciceFile)