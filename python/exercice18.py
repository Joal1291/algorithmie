# prendr deux tableaux les réunir et le trier 

array1 = [1,8,65,854,2,96,74,25,1002,85,374,194,276]
array2 = [65,842,34,75,1284,94,1974,379,465,987]

def sorttwoarray(value1, value2):
    array3 = [*array1, *array2]
    array3.sort()
    print(array3)

sorttwoarray(array1, array2)