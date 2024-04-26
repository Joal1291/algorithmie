import openfile

file = "fichier1.txt"

exercice = openfile.readFile(file)

dico = {}
for i in exercice: 
    runner, country, time = i.split(',')
    if dico.get(country)==None:
        dico[country] = int(time)
    else:
        dico[country] += int(time)

sorteddico = sorted(dico.items(), key=lambda x: x[1])
print(sorteddico[0])
