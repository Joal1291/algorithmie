# import openfile2
# import sys
import math


# filename = "telephone.txt"
# exerciceFile = openfile2.readFile(filename)

# telephone = {
#     0: [],
#     1: [],
#     2: [],
#     3: [],
#     4: [],
#     5: [],
#     6: [],
#     7: [],
#     8: [],
#     9: []
# }
# res = 0
# def check(check, new):
#     mini = min(len(check), len(new))
#     for i in range(mini):
#         if check[i] != new[i]:
#             return len(new) - i
#     res = len(new)-len(check)
#     if res < 0: return 0
#     else: return res    

# for newtel in exerciceFile:
#     clef = int(newtel[0])
#     res1 = 20
#     if not telephone[clef]:
#         telephone[clef].insert(0,newtel)
#         res += len(newtel)
#         continue
#     else: 
#         for tel in sorted(telephone[clef]):
#             res2 = check(tel, newtel)
#             if res2 < res1:
#                 res1 = res2
#         telephone[clef].insert(0,newtel)
#         res += res1
# print(res)

import math
a,b,c=[float(input())for _ in range(3)]
print(int(a/(1-(math.log10(b)-math.log10(c)))))