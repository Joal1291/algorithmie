def higher(nbr):
    if(nbr >= 0 and  nbr <= 20):
        if(nbr > 10):
            print('Valid')
        else:
            print('Not valid')
    else: 
        print('The number have to be between 0 and 20')
higher(21)
