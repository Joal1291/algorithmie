import openfile

filename = "day3.txt"
exerciceFile = openfile.readFile(filename)

arrayTest = [
"467..114...",
"...*......",
"...35.633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598..",
]

     #  #               ################
      #   #           ###         #    ###
        #   #        ##           #      ##
          #   #     ###################################
            #   #   ##    ####               ###      ##
              #  #####   #    #             #   #     #
                    #####  ##  #############   # ######
                         ####                ###
                         ##                  #
######################################################################
#                          Engine Game Product                       #
######################################################################
height = len(exerciceFile)
width = len(exerciceFile[0])

def findNumber(row, col, array):
  index = 0
  number1 = ""
  number2 = ""
  for row1 in range(row-1, row+2):
      for col1 in range(col-1, col+2):
          if array[row1][col1].isdigit():
              char = array[row1][col1+index]
              if number1 == "":   
                while char.isdigit():
                  number1 = number1 + char
                  index += 1
                  if col1+index> width-1:break
                  char = array[row1][col1+index]
                index = 1
                char = array[row1][col1-index]
                while char.isdigit():
                  number1 = char + number1
                  index += 1
                  if col1-index <0:break
                  char = array[row1][col1-index]
                index = 0
                if array[row-1][col1] + array[row-1][col1+1] in number1:break
                if array[row+1][col1] + array[row+1][col1+1] in number1:break
              elif number2 == "":
                while char.isdigit():
                  number2 = number2 + char
                  index += 1
                  if col1+index> width-1:break
                  char = array[row1][col1+index]
                index = 1
                char = array[row1][col1-index]
                while char.isdigit():
                  number2 = char + number2
                  index += 1
                  if col1-index <0:break
                  char = array[row1][col1-index]
  if number1 == "" or number2 == "":
     return 0
  else:
    return int(number1)*int(number2)

def main(array):
    result = 0
    for row in range(0, len(array)):
        for col in range(0, width):
            char = array[row][col]
            if char == '*':
                result += findNumber(row, col, array)               
    print('Result :',result)
main(exerciceFile)