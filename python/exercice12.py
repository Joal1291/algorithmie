# nbr equal child age and display the category of the child

def category(nbr1):
    result = "The kid category is:"
    if(nbr1 >= 6 and nbr1 <= 7):
        print(f"{result} poussin.")
    elif(nbr1 >= 8 and nbr1 <= 9):
        print(f"{result} pupille.")
    elif(nbr1 >= 10 and nbr1 <= 11):
        print(f"{result} minime.")
    elif(nbr1 >= 12):
        print(f"{result} cadet.")
category(9)