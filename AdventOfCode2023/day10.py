import re
import openfile

exercice = openfile.readFile("day10.txt")
exerciceTest = openfile.readFile("day10test.txt")

moves= []

def findAnimal(array):
    count = 0
    for lines in array:
        animal = re.findall(r'S', lines)
        if animal:
            return count, lines.index('S')
        count += 1

def addMove(array, line, index):
    actualchar = array[line][index]
    char_up = ""
    char_right = ""
    char_down = ""
    char_left = ""
    
    if line != 0: char_up = array[line-1][index]
    if index != len(array[0])-1:char_right = array[line][index+1]
    if line != len(array)-1:char_down = array[line+1][index]
    if index != 0:char_left = array[line][index-1]
    
    if char_up in '|7F' and actualchar in '|JLS' and (char_up, line-1, index) not in moves:
        moves.append((char_up, line-1, index))
        return char_up, line-1, index
    elif char_right in '-7J' and actualchar in '-LFS' and (char_right, line, index+1) not in moves:
        moves.append((char_right, line, index+1))
        return char_right, line, index+1
    elif char_down in '|JL' and actualchar in '|7FS' and (char_down, line+1, index) not in moves:
        moves.append((char_down, line+1, index))
        return char_down, line+1, index
    elif char_left in '-LF' and actualchar in '-7JS' and (char_left, line, index-1) not in moves:
        moves.append((char_left, line, index-1))
        return char_left, line, index-1
    elif char_up == "S" or char_right == "S" or char_down == "S" or char_left == "S":
        return "S", line, index
    else:
        print("Une putain d'erreur est survenue")
        return "S", 0, 0 

def main(array):
    count = 0
    animalLine, animalIndex = findAnimal(array)
    moves.append(("S", animalLine, animalIndex))
    char = ""
    line = animalLine
    index = animalIndex
    while char != "S":
        char, line, index = addMove(array, line, index)
        count += 1
    
    print("Result:",int(count/2))

main(exercice)