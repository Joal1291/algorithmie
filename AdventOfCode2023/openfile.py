path = "C:/Users/jordy/Documents/Code/algorithmie/AdventOfCode2023/fichier/"

def readFile(filename: str):
    fichier = open(path+filename, 'r')
    words = []
    for line in fichier:
        words.extend(line.strip().split('\n'))
    # print(words)
    return words


# Règles du fichier en fonction des jours d'exercice.
