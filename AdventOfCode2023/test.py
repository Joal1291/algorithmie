## -------------------------calcul d'area!-------------------------##
# h = ('height')
# w = ('width')
# r = ('radius')
# s = ('value')
# if s=="triangle": print(f'{(w*h)/2:.2f}')
# elif s == 'rectangle': print(f'{w*h:.2f}')
# elif s == "circle": print(f'{3.14*(r**2):.2f}')

# # module date time
# import datetime
# year = int(input())

# try:
#     datetime.date(year, 2, 29)
#     print('true')
# except ValueError:
#     print('false')

##-----------------------changement de caractere-------------------##
    
# print(arm+ face + "".join(reversed(arm.translate(str.maketrans('</[{(>\]})','>\]})</[{(')))))

##---------------Check d'égalité dans deux tableau-----------------##
# p=input
# a=p().split()
# b=p().split()
# e=any(j==i for i in a for j in b)
# p(['Not overlap','Overlap'][e])

## sum de toute les majuscule dans une chaine de caractere
# s = "sdK"
# print(sum(ord(i) for i in s if i.isupper()))

##-------------------formule de calcul pour aditioner tout les nombre impaire puissance 2---------------------##
#print((n*(2*n-1)*(2*n+1))//3)

## formule pour calculer un bin negative to a decimal
# print(sum(int(r)*(-2)**p for p,r in enumerate(input()[::-1])))