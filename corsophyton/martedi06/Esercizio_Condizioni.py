#esercizio 1
livello1= int(input("Inserisci un numero a piacere!"))
if livello1 > 0:
    print("Complimenti! il Numero è Positivo!")
    
    livello2= int(input("Inserisci una seconda età"))
    if livello2 == 17:
        print ("stai attento! non puoi andare a minorenni!")
        
        livello3= int(input("Inserisci una terza età"))
        if livello3 == 100:
            print("porca puttana con tutankamon ti sei messo?")
            

#esercizio2
scelta= int(input("Scegli un'operazione: aggiungi, modifica o elimina:"))
if scelta == "aggiungi":
    print("Ottimo!, ha scelto di aggiungere")
    
elif scelta == "modifica":
    print("Ottimo! hai scelto di modificare")
    
elif scelta == "elimina":
    print("Mi dispiace! hai scelto di eliminare")
else:
    "ERROR 404"

        

