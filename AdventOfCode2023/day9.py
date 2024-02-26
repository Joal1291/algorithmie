import re
import openfile

exercice = openfile.readFile("day9.txt")
exerciceTest = openfile.readFile("day9test.txt")

arrayBuffer = []

def getResult(array):
    value = 0
    for lines in array:
        value = lines[-1:][0] + value
    return value

def allNextLine(line):
    buffer = []
    for i in range (1, len(line)):
        buffer.append(int(line[i]) - int(line[i-1]))
    arrayBuffer.insert(0,  buffer)
    if sum(buffer) != 0:
        allNextLine(buffer)
    elif max(buffer) !=0 or min(buffer) != 0:
        allNextLine(buffer)

def main(array):
    result = 0
    for lines in array:
        line = map(int, lines.split())
        result_line = list(line)
        arrayBuffer.append(result_line)
        allNextLine(result_line)
        result += getResult(arrayBuffer)

        arrayBuffer.clear()
    print("Result: ", result)

main(exercice) 