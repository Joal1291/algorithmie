import openfile

filename = "day4.txt"
exerciceFile = openfile.readFile(filename)

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
        newArray.append(numbers)
    return newArray

#######################################################################
#                               Part 1                                #
#######################################################################

def main(array):
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

# main(exerciceFile)

#######################################################################
#                               Part 2                                #
#######################################################################

def main(array):
    arrayToInterprete = transformArray(array)
    result = 0
    count = 0
    for line in arrayToInterprete:
        playNbr = line[0].strip().split(' ')
        winNbr = line[1].strip().split(' ')
        resBuffer = 0
        for nbr in playNbr:
            if nbr=="":
                continue
            if nbr in winNbr:
                resBuffer +=1
        for i in range(1, resBuffer+1):
            arrayToInterprete[count+i].append("a")
        count+=1
    for line in arrayToInterprete:
        result += line.count('a')
        print(line.count('a'))

    print("count: ", count)
    print("Result :", result)

main(exerciceFile)