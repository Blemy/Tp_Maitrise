import random, string

# 1-Pour mettre tous les caracter en minicule
caractere="Pour mettre tous les caracter en minicule".lower()
print("Le phrase en miniscule est\n",caractere)

#2-Pour split et mettre dans une liste
print('\nLa phrase dans une liste')
listQ=caractere.split(" ")
print(listQ)

#3-Tous les premieres lettres en majuscule
print('\nTous les premieres lettres en majuscule')
lettr=caractere.title()
print(lettr)

#4-1er lettre chaque mot
print('\nTous les premieres lettres chaque mot')
inv=caractere.split()
premier=[mot[0] for mot in inv]
print(''.join(premier))

#5-Remplace tous les caracteres a par @
print('\nRemplace tous les caracteres a par @')
rempl=caractere.replace("a","@")
print("La phrase devient : ",rempl)

#6-Mete yon chenn karaktè devan dèyè, answit mete l an majiskil.
print("\nMete yon chenn karaktè devan dèyè, answit mete l an majiskil.")
inv=caractere.upper()
print(inv[::-1])

#7-Afiche endeks premye karaktè "a" ki nan yon chenn
carac="Mete yon chenn karaktè devan dèyè, answit mete l an majiskil"
print("\nFraz la se : ", carac)
print("Afiche endeks premye karaktè 'M' ki nan yon chenn a se")
test=carac[0].lower()
for i, char in enumerate(carac):
        if(char==test):
            print(i)
            break

#8-Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil)
caract="Afiche total tout endeks karaktè ki nan yon chenn"
test=caract[0].lower()
som=0
for i, char2 in enumerate(caract):
        if(char2==test):
            som+=i
print("\nLa somme du premier caractere est : ",som)

#9-Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil)
print("\nlis ki gen endeks tout karaktè a se : ")
listQ=[]
for i, char2 in enumerate(carac):
        if(char2=='a'):
            listQ+=[i]
print(listQ)

#10-Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen
print("\n La chaine de caractere sans espace est : ")
somme=0
car_split=carac.replace(" ","")
for i, chr in enumerate(car_split) :
    somme+=i
print(f"{car_split}{somme}\n")


print("BYENVINI NAN PATI DE A KI AP PALE DE LISTE")
#1-Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
list_element=[]
for i in range(0,101): 
    if(i%2==0):
        list_element+=[i]
print("La liste des elements divisible que par 2 sont\n",list_element)

#2-Ou gen yon lis antye, konvèti l an yon lis chenn.
list_entier=[1,2,3,4,5,6,7,8,9,0]
noub=[]
for i in list_entier:
    noub+=str(i)
print("\nLis konveti en chenn\n",noub)

#3.	Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
list_chenn=["chat", "chien", "oiseau", "fleur", "arbre"]
list_majus=[]
for chn in list_chenn :
    list_majus+=[chn.upper()]
print("\nListe convertit en majikil\n",list_majus)

#4.	Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
lis=[1,2,3,4,5,6,7,8,9,10,12,11]
nouvo_lis=[]
for lo, la in enumerate(lis):
    if (lo%3 ==0):
        nouvo_lis+=[la]
print("\nLis ki fet ak endeks divisib pa 3 selman\n",nouvo_lis)


#5.	Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl.
lost=[]
for i in range(0, len(lis), 3) :
    a = tuple(lis[i:i+3])
    lost.append(a)
print("\nLa liste groupee par 3 \n",lost)

lis_dou=[1,2,3,4,5,6,7,1,2,3,4,5,6,7,8,9,10,12,118,9,10,12,11,44]
lis_dou2=[1,2,3,4,5,6,7,1,2,3,4,5,6,7,8,9,10,12,118,9,10,12,11,55,65,69]
#6.	Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.
sans_doublon=list(set(lis_dou))
print("\nLis, ki pa gen okenn doublon\n",sans_doublon)

#7.	Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.
nouvo_lis = []
for eleman in lis_dou:
    if eleman in lis_dou2:
        nouvo_lis.append(eleman)
print("\nNouvo lis, ki genyen sèlman eleman komen ant 2 lis yo \n",nouvo_lis)
#8-Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.
nouvo_lis = []
for eleman in lis_dou:
    if eleman not in lis_dou2:
        nouvo_lis.append(eleman)

for eleman in lis_dou2:
    if eleman not in lis_dou:
        nouvo_lis.append(eleman)
print("\nEleman ki nan 1 an ki pa nan 2 a se : ",nouvo_lis)


#9-Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.
dictionnaire={"name": "Lub", "age": 14, "assets": "laptop", "nom": "Alice", "laj": 30, "ville": "Paris"}
list_cv=[]
for valeur in dictionnaire.values():
    list_cv.append(valeur)
print("\nLa nouvelle liste devient : \n",list_cv)

#10-Reyini 3 lis ansanm, san okenn doublon.
print("\n\nBYENVINI NAN PATI 3\n\n")

#Partie 3
#1-Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.
list_dict=[]
for kle, vale in dictionnaire.items():
    list_dict+=[vale]
print("\nLa liste des valeurs sont \n",list_dict)


#2-Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
tape=input("\nTape yon vale epi verifye lap si l gen akolad devan ak dèyè : ")
if(str(tape[0])=='{' or str(tape[0])=='}' or str(tape[-1]=='{' or str(tape[-1])=='}')):
    print("\nOui li gen akolad ladanl\n")
else:
    print("Pas gen akolad")

#3-Pakouri yon diksyonè, epi afiche tout kle yo
print("\nLes cles sont : ")
for cle in dictionnaire.keys():
    print(cle)
print("\n")
#4-Pakouri yon diksyonè, epi afiche tout vale yo
print("\nLes valeurs sont :")
for vale in dictionnaire.values():
    print(vale)
print("\n")

#5-Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
print("\nLe copy du dictionnaire est :\n")
dict_nouv=dictionnaire.copy()
print(dict_nouv)
print("\n")

#6-Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo
print("Le nouveau dectionnaire avec des _ est : ")
for cle, valeur in dictionnaire.items():
    if isinstance(valeur, str):
        dictionnaire[cle]="_"+valeur+"_"
print(dictionnaire)
print("\n")

#7-Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman. 
print("\nLe nouveau dectionnaire entier est : ")
dictionnaire_nouv={}
for cle, valeur in dictionnaire.items():
    if isinstance(valeur, int):
        dictionnaire_nouv[cle]=valeur
print(dictionnaire_nouv)
print("\n")

dictionnaire={"name": "Lub", "age": 14, "assets": "laptop", "nom": "Alice", "laj": 30, "ville": "Paris"}

#8-Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la
list_cle_vla=[]
print("Dictionnaire la sou fom tipl : ")
for cle1, valeur1 in dictionnaire.items():
    list_cle_vla.append((cle1, valeur1))
print(list_cle_vla)
print("\n")

#9-Pakouri yon lis tipl, pou w mete l sou fòm diksyonè.
nuv_dict={}
print("List la sou fòm diksyonè")
for cle3, valeur3 in list_cle_vla:
    nuv_dict[cle3] = valeur3
print(nuv_dict)
print("\n")
#10-Kole 2 diksyonè ansanm pou fè youn, kote si gen eleman ki gen menm kle ap konkatene valè, swivan kondisyon sa yo:


print("BYENVINI NAN PATI FONKSYON ANH\n")
#PATI FONCTION
#1-kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.

def finction_inverse(argument):
    arg=(argument[::-1])
    print("Inserse la se : ")
    print(arg)
argumen=input("Entrer la phrase epi program nan ap envese l pou ou : ")
finction_inverse(argumen)
print("\n")

#2-kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik.
def fonction_code(n):
    code=''
    for i in range(n):
        code+=(random.choice(string.ascii_letters)).title()
    print("Le code est : ", code)
nmbr_code=input("Konbyen karaktè alfabetik ou bezwen kob wa genyen : ")
fonction_code(int(nmbr_code))
print("\n")

#3-kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon
def fonction_code_sans_rep(m):
    code=''
    cod=''
    for i in range(m):
        code=(random.choice(string.ascii_letters)).upper()
        while code in cod:
           code=(random.choice(string.ascii_letters)).upper()
        cod+=code
    print("Kode san repetisyon se : ", cod) 
nmbr_code2=input("Konbyen karaktè alfabetik ou bezwen kob wa genyen : ")
fonction_code_sans_rep(int(nmbr_code2))
print("\n")


#4-kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.
def fonction_code_sans_rep_alfanim(b):
    code=''
    cod=''
    for i in range(b):
        code=(random.choice(string.ascii_letters + string.digits)).upper()
        while code in cod:
           code=(random.choice(string.ascii_letters + string.digits)).upper()
        cod+=code
    print("Kod alafanimerik, san repetisyon anh se : ", cod)
nmbr_code3=input("Konbyen karaktè alfabetik ou bezwen kob wa genyen : ")        
fonction_code_sans_rep_alfanim(int(nmbr_code3))
print("\n")
#5-Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"
def fonction_slug():
    slug=input("Antre chenn de karakte pou slug la : ").replace(" ","-")
    print("LE SLUG EST ",slug)
fonction_slug()
print("\n")

#6-Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def fonction_separe():
    chenn="Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil"
    che=""
    for i in chenn :
        che+=i+","
    print("Chak lèt ap ak yon vigil :")
    print(che)
fonction_separe()
print("\n")

#7-Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.
def fonction_kip(mot):
    end=[]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for let in mot:
        if let in alphabet :
            end.append(str(alphabet.index(let)))
    mo_krip="-".join(end)
    print("Mo kripte a se : ")
    print(mo_krip)
mot=input("Antre mo ou besoin kripte a : ").lower()
fonction_kip(mot)
print("\n")

#8-Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.
def fonction_decrip():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    mot_kry=input("Antre mo ou besoin dekripte a : ")
    mot_krypte=(str(mot_kry))
    mo_a=mot_krypte.split("-")
    decrip=""
    for i in mo_a:
        if i.isdigit():
            moo=alphabet[int(i)]
            decrip+=moo
    print("Mo dekripte a se : ")
    print(decrip)
fonction_decrip()
print("\n")
#9-Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li retounen tou 2 valè yo sou fòm Tuple.

#10-Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. Atansyon ak non konpoze ak tirè yo.
def fontion_initial(noo):
    init=noo[0]
    for car in range(len(noo)-1):
        if(noo[car]==" "):
            init+=noo[car+1]
    print("L'initial du nom est : ",init)
nom_s=input("Entrer nom anh epi lap baw initial li : ").replace("-"," ")
fontion_initial(str(nom_s))
