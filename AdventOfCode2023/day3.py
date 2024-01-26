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
notSymb = ".123456789"

#Matrice
# check = [[0 for row in range(height)]for col in range(width)]

######################################################################
#                     Function pour la partie 1                      #
######################################################################
def calculateSumOfNumber(array):
    result = 0
    for i in array:
        result += int(i)
    return result

def numberValidation(lineindex, nbrindex, array):
    row = lineindex
    col = nbrindex
    height = len(array)
    width = len(array[0])
    #Digonale haut gauche
    if str(array[(row-1)%height][(col-1%width)]) not in notSymb:
        return True
    #Haut
    if str(array[(row-1)%height][col]) not in notSymb:
        return True
    #Diagonal haut droite
    if str(array[(row-1)%height][(col+1%width)]) not in notSymb:
        return True
    #Droite
    if str(array[row][(col-1%width)]) not in notSymb:
        return True
    #Diagonal bas droite
    if str(array[(row+1)%height][(col+1%width)]) not in notSymb:
        return True
    #Bas
    if str(array[(row+1)%height][col]) not in notSymb:
        return True
    #Diagonal bas gauche
    if str(array[(row+1)%height][(col-1%width)]) not in notSymb:
        return True
    #Gauche
    if str(array[row][(col-1%width)]) not in notSymb:
        return True
    return False

def thereIsSymb(lineindex, nbrindex, array):
    row = lineindex
    col = nbrindex
    width = len(array[0])
    if str(array[row][(col+1)%width]) not in notSymb:
        return True
    return False

def thereIsDot(lineindex, nbrindex, array):
    row = lineindex
    col = nbrindex
    width = len(array[0])
    if str(array[row][(col+1)%width]) == ".":
        return True
    return False

def main(array):
    arrayOfNumber = []
    validation = False
    number = ""

    for row in range(len(array)):
        print("\n-------- row: ", row)
        for col in range(len(array[0])):
            print("column: ", col)
            char = array[row][col]
            if char.isdigit():
                number += char
                if numberValidation(row, col, array):
                    validation = True
                if thereIsDot(row, col, array):
                    if validation == True:
                        arrayOfNumber.append(number)
                        number = ""
                        validation = False
                    else:
                        number = ""
                if thereIsSymb(row, col, array):
                    arrayOfNumber.append(number)
                    number = ""
                    validation = False
    print('Result:', calculateSumOfNumber(arrayOfNumber))

main(exerciceFile) 