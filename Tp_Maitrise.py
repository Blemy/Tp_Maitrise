# Pour mettre tous les caracter en minicule
caractere="Pour mettre tous les caracter en minicule".lower()
print("Le phrase en miniscule est\n",caractere)

# Pour split et mettre dans une liste
print('\nLa phrase dans une liste')
list=caractere.split(" ")
print(list)

#Tous les premieres lettres en majuscule
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
print("\nFraz la se : ", carac)
print("Afiche endeks premye karaktè 'M' ki nan yon chenn a se")
test=carac[0].lower()
for i, char in enumerate(carac):
        if(char==test):
            print(i)
            break

#Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil)
caract="Afiche total tout endeks karaktè ki nan yon chenn"
test=caract[0].lower()
som=0
for i, char2 in enumerate(caract):
        if(char2==test):
            som+=i
print("\nLa somme du premier caractere est : ",som)

#Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil)
print("\nlis ki gen endeks tout karaktè a se : ")
list=[]
for i, char2 in enumerate(carac):
        if(char2=='a'):
            list+=[i]
print(list)

#Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen
print("\n La chaine de caractere sans espace est : ")
somme=0
car_split=carac.replace(" ","")
for i, chr in enumerate(car_split) :
    somme+=i
print(f"{car_split}{somme}\n")

#Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
list_element=[]
for i in range(0,101): 
    if(i%2==0):
        list_element+=[i]
print("La liste des elements divisible que par 2 sont\n",list_element)

#Ou gen yon lis antye, konvèti l an yon lis chenn.

#Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.
list_conv=[]
dictionnaire={"name": "Lub", "age": 14, "assets": "laptop", "nom": "Alice", "laj": 30, "ville": "Paris"}
for valeur in dictionnaire.values():
    list_conv.append(valeur)
print("\nLa nouvelle liste devient : \n",list_conv)





#Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
tape=input("\nTape yon vale : ")
if(str(tape[0])=='{' or str(tape[0])=='}' or str(tape[-1]=='{' or str(tape[-1])=='}')):
    print("Oui li gen akolad ladanl")
else:
    print("Pas gen akolad")

#Pakouri yon diksyonè, epi afiche tout kle yo
print("\nLes cles sont : ")
for cle in dictionnaire.keys():
    print(cle)

#Pakouri yon diksyonè, epi afiche tout kle yo
print("\nLes valeurs sont :")
for vale in dictionnaire.values():
    print(vale)

#Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
print("\nLe copy du dictionnaire est :\n")
dict_nouv=dictionnaire.copy()
print(dict_nouv)

#Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo
print("Le nouveau dectionnaire avec des _ est : ")
for cle, valeur in dictionnaire.items():
    if isinstance(valeur, str):
        dictionnaire[cle]="_"+valeur+"_"
print(dictionnaire)

#Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman. 
print("\nLe nouveau dectionnaire entier est : ")
dictionnaire_nouv={}
for cle, valeur in dictionnaire.items():
    if isinstance(valeur, int):
        dictionnaire_nouv[cle]=valeur
print(dictionnaire_nouv)