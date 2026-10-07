#esercizio3
parole = ["ciao" , "Buongiorno" , " Buonanotte"]
numeri = [1, 2, 3]

scelta = input("Scegli quale elemento della lista vuoi usare? (parole/numeri)")

if scelta == "parole":
    print ( "hai scelto la lista delle parole")
    print (parole)
    
    operazione = input("Scegli se aggiungere o rimuovere una parola")
    if scelta == "aggiungere":
        scelta_parola = input ("scrivi una parola da aggiungere")
        parole.append(scelta_parola)
        
    elif scelta == "rimuovere":
        scelta_parola = input("scrivi la parola da rimuovere")
        parole.remove(scelta_parola)
        
    else:
        print("La parola non è presente nella lista")
        
elif scelta== "numero":
    print("hai scelto la lista dei numeri")
    print (numeri)
    
    scelta = input ("Scegli se aggiungere o rimuovere un numero")
    
    if scelta == "aggiungere":
        print ("hai aggiunto un numero")
        scelta = int(input ("scrivi un numero da aggiungere"))

        numeri.append=(scelta)
        
    elif scelta== "rimuovere":
        scelta== int(input("scrivi un numero da rimuovere"))
        numeri.remove(scelta)
        
    else:
        print("Operazione non valida.")
        
else:
    print("scelta non valida")