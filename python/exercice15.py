# ecrire avec boucle while 1+2+3+...+N 

def calculate(nbr):
    result = 0
    count = 0
    while(count < nbr):
        result = result + (count + 1)
        count +=1
    print (f"the result is: {result}")

calculate(10)