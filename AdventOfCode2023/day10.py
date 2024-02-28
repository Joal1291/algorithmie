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
    
    if char_up in '|7F' and actualchar in '|JLS' and (line-1, index) not in moves:
        moves.append((line-1, index))
        return True, line-1, index
    elif char_right in '-7J' and actualchar in '-LFS' and (line, index+1) not in moves:
        moves.append((line, index+1))
        return True, line, index+1
    elif char_down in '|JL' and actualchar in '|7FS' and (line+1, index) not in moves:
        moves.append((line+1, index))
        return True, line+1, index
    elif char_left in '-LF' and actualchar in '-7JS' and (line, index-1) not in moves:
        moves.append((line, index-1))
        return True, line, index-1
    elif char_up == "S" or char_right == "S" or char_down == "S" or char_left == "S":
        return False, line, index

def countCharInBoucle(array):
    result = 0
    d = ""
    for count, a in enumerate(array):
        for count2, i in enumerate(a):
            if (count, count2) in moves:
                d+="-"
            else: d+= "O"
        print(d)
        d = ""
    return result

def main(array):
    animalLine, animalIndex = findAnimal(array)
    moves.append((animalLine, animalIndex))
    boolean = True
    line = animalLine
    index = animalIndex
    while boolean:
        boolean, line, index = addMove(array, line, index)
    print(f"Result of char in boucle = {countCharInBoucle(array)}")
    print("Result =",int(len(moves)/2))
    # print(moves)
    # print('---------------------------------------------------------')
    # print(movestest)

main(exercice)