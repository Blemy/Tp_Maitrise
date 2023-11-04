# Pour mettre tous les caracter en minicule
caractere="Pour mettre tous les caracter en minicule".lower()
print("Le phrase en miniscule est ",str(caractere))

# Pour split et mettre dans une liste
print('\n La phrase dans une liste')
list=caractere.split(" ")
print(list)

# Tous les premieres lettres en majuscule
print('\nTous les premieres lettres en majuscule')
lettr=caractere.title()
print(lettr)

# 1er lettre chaque mot
print('\nTous les premieres lettres chaque mot')
inv=caractere.split()
premier=[mot[0] for mot in inv]
print(''.join(premier))

#Remplace tous les caracteres a par @
print('\nRemplace tous les caracteres a par @')
rempl=caractere.replace("a","@")
print("La phrase devient : ",rempl)

#Mete yon chenn karaktè devan dèyè, answit mete l an majiskil.
print("\nMete yon chenn karaktè devan dèyè, answit mete l an majiskil.")
inv=caractere.upper()
print(inv[::-1])

#Afiche endeks premye karaktè "a" ki nan yon chenn
carac="Mete yon chenn karaktè devan dèyè, answit mete l an majiskil"
test=carac[0].lower()
for i, char in enumerate(carac):
        if(char==test):
            print(i)
            break

#Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil)
caract="Mete m"
test=caract[0].lower()
som=0
for i, char2 in enumerate(caract):
        if(char2==test):
            som+=i
print("La somme des caracteres est : ",som)

#Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil)
list=[]
for i, char2 in enumerate(carac):
        if(char2=='a'):
            list+=[i]
print(list)

#Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen
somme=0
car_split=carac.replace(" ","")
for i, chr in enumerate(car_split) :
    somme+=i
print(f"{car_split}{somme}")





