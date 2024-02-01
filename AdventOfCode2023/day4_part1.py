import openfile
import cProfile
filename = "day4.txt"
exerciceFile = openfile.readFile(filename)

#############################################################################
# import re
# def part2(puzzle_input):
#     regex = r':(.*)\|(.*)'
#     cards = [1] * len(puzzle_input)
#     for i, line in enumerate(puzzle_input):
#         win_nums, actual_nums = re.findall(regex, line)[0]
#         overlap = set(win_nums.split()) & set(actual_nums.split())
#         for j in range(len(overlap)):
#             cards[i+j+1] += cards[i]
#     print(sum(cards))
# part2(exerciceFile)
#############################################################################

arrayTest = [
"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]
 
#                             ,---')
#                            (  -_-(
#                            ) .__/ )
#                          _/ _/_( /        _.---._
#                         (__/ _ _) ,-._   /  o    \
#                           //)__(\/,-` |_| O  o o O|
#                       _\\///==o=\'      |O o  o O |
#                        `-' \    /        \O o   o/
#                             )___\         `'-.-\\
#                            / ,\ \       ____)_(____
#                           / /  \ \     '--..---,,--'
#                          /()    >()        \\_//   
#                         |\_\   |\_\       /,-.\
#######################################################################
#                                                                     #
#   88                                                                #
#   88              ,d      ,d                                        #
#   88              88      88                                        #
#   88  ,adPPYba, MM88MMM MM88MMM ,adPPYba, 8b,dPPYba, 8b       d8    #
#   88 a8"     "8a  88      88   a8P_____88 88P'   "Y8 `8b     d8'    #
#   88 8b       d8  88      88   8PP""""""" 88          `8b   d8'     #
#   88 "8a,   ,a8"  88,     88,  "8b,   ,aa 88           `8b,d8'      #
#   88  `"YbbdP"'   "Y888   "Y888 `"Ybbd8"' 88             Y88'       #
#                                                          d8'        #
#                                                          d8'        #
#######################################################################

def transformArray(array):
    newArray = []
    for line in array:
        cards = line.split(':')
        numbers = cards[1].split('|')
        newArray.append([numbers[0], numbers[1], 1])
    return newArray

newarray = transformArray(exerciceFile)
#######################################################################
#                               Part 1                                #
#######################################################################

def main1(array):
    arrayToInterprete = transformArray(array)
    first = True
    result = 0
    for line in arrayToInterprete:
        playNbr = line[0].strip().split(' ')
        winNbr = line[1].strip().split(' ')
        resBuffer = 0
        for nbr in playNbr:
            if nbr=="":
                continue
            if nbr in winNbr and first:
                resBuffer += 1
                first = False
            else:
                if nbr in winNbr:
                    resBuffer *=2
        first = True
        result += resBuffer
    print("Result :", result)

#######################################################################
#                               Part 2                                #
#######################################################################

def main2(array):
    count = 0
    for playline, winLine, iterations in array:
        playLineSet = set(playline.split())
        winLineSet = set(winLine.split())
        resBuffer = 0
        for i in range(1, iterations+1):
            for nbr in playLineSet:
                if nbr in winLineSet:
                    resBuffer += 1
                    array[count +resBuffer][2] += 1
            resBuffer = 0
        count += 1
    finalResult = 0
    for line in array:
        finalResult += line[2]
    print("Result: ", finalResult)
main2(newarray)