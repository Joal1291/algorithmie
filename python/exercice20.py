chaine1 =  "Engage le jeu que je le gagne" 
chaine2 = 'radar'
chaine3 = 'je suis la'


def palindrome(value):
    count = 0
    chaine = value.lower()
    new = chaine.replace(' ', '')
    while count < len(new)//2:
        if(new[count] == new[-(count+1)]):
            count += 1
        else:
            print("Ce n'est pas un palindrome")
            return 
    print("C'est un palindrome")

palindrome(chaine1)

def palindromeOpti(value):
    new = value.lower().replace(' ', '')
    print(new)
    for i in range(len(new)//2):
        if new[i] != new[- (i+1)]:
            print("Ce n'est pas un palindrome")
            return
    print("C'est un palindrome")
    

palindromeOpti(chaine3)