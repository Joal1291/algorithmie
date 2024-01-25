path = "C:/Users/jordy/Documents/Code/algorithmie/AdventOfCode2023/"
file = "day1_part1.txt"


def readFile():
    fichier = open(path+file, 'r')
    words = []
    for line in fichier:
        words.extend(line.strip().split())
    return words
readFile()
