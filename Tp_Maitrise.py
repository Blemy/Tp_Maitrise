# Pour mettre tous les caracter en minicule
caractere=input("Entre la phrase : ").lower()
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

carac="Ayiti kapab avanse"
for i in enumerate(carac):
    print(i)