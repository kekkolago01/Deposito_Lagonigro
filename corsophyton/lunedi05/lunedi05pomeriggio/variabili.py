
"""
# qui proveremo le variabili e i tipi di variabili

nome_variabile = "nome"



saluto ="Ciao"

nome="Fragola89"

print (saluto + " " + " sono " + nome + ", 89 sono le misure nuove" )

s ="kekkolago"
print (s[0]) #output k
print (s[4]) #output o


#stringhe

s = "ciao, mondo!"
print (len(s)) #12
print (s.upper ()) # CIAO, MONDO!
print (s.lower()) #ciao, mondo!
print (s.split()) #['ciao,', 'mondo!']
print (s.replace('mondo' , 'universo')) #ciao, universo!



#booleani

x=5
y=10

print(x == y) #false
print (x != y) #true
print(x < y) #true
print (x <= y) #true
print (x > y) #false
print (x >= y) #false



#booleani con orepatori logici

x = 5
y= 10
z = 7

print (x < y and y > z ) #true
print (x<y or z>y)  #true
print (not(x<y)) #false

"""
#Andare a crea una variabile che prende in input ogni tipo di "tipo" basilare e stamparli tutti in unico print, dopodichè far inserire all'utente due numeri e comprovare gli operatori, logici e di confronto.

bool = bool(input("inserisci un bool"))
numint = int(input("inserisci un int"))
numfloat = float(input("inserisci un float"))
char = input("inserisci un char")
string = input("inserisci un parola")

print (bool, " ", numfloat, " ", numint, " ", string, " ", char)


numint1 = int(input("inserisci un int"))
numint2 = int(input("inserisci un int"))

print(numint1 < numint2 and numint1 > numint2 )
print(numint1 < numint2 or  numint1 > numint2 )
print(not(numint1 < numint2 and numint1 > numint2 ))