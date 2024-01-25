path = "C:/Users/jordy/Documents/Code/algorithmie/AdventOfCode2023/"

def readFile(filename: str):
    fichier = open(path+filename, 'r')
    words = []
    for line in fichier:
        words.extend(line.strip().split())
    # print(words)
    return words
