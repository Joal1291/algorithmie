import re
import openfile

exercice = openfile.readFile("day8.txt")
exerciceTest = openfile.readFile("day8test.txt")
###       22357       ###     10371555451871    ###
###################################################
#                     Part 1                      #
###################################################

def interpreteTheArray(array):
    array.pop(1)
    boolean = True
    move = ""
    searchValue = {}
    for lines in array:
        if boolean:
            move = lines
            boolean = False
        else:
            line = re.match(r"(\w+) = \((\w+), (\w+)\)", lines)
            clef = line.group(1)
            leftRight = [line.group(2), line.group(3)]
            searchValue[clef] = leftRight
    return move, searchValue

moves, searchvalue= interpreteTheArray(exercice)

def numberOfIterationToFindZZZ():
    result = 0
    true = True
    buffer = 'AAA'
    while true:
        if buffer == 'ZZZ': 
            print(f"Result: {result}")
            break
        for move in moves:
            if move == 'L':
                buffer = searchvalue[buffer][0]
            elif move == 'R':
                buffer = searchvalue[buffer][1]
            result += 1           
numberOfIterationToFindZZZ()