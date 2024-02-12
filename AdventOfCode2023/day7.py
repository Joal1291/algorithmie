import re
from collections import Counter # vas me permettre de compter les iteration d'un caractere dans une chaine de caractere
import openfile

from collections import Counter
from functools import cmp_to_key

exercice = openfile.readFile("day7.txt")
exerciceTest = openfile.readFile("day7test.txt")

### 250898830 ###
#######################################################################
#                                Part 1                               #
#######################################################################

####################################
# Type du plus fort au plus faible #
####################################
# 5 carte du même type
# 4 caret du même type
# full house
# 3 cartes du même type
# 2 paire
# 1 paire
# carte forte

# si deux main sont de même niveau comparer les carte de la premiere vers la 5.
# La main qui l'emporte et celle avec la carte la plus forte
# si par exemple la carte n°1 est de même type il faut donc comparer la deuxieme etc...
# plus la main est forte plus le rank est élevé

## LET'S GO.

def puissance(array):
    for lines in array:
        line = lines.split()
        main = Counter(line[0])
         
        print(line, main)


puissance(exerciceTest) 