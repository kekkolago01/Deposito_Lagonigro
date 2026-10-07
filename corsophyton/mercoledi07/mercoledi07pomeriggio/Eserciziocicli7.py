#7


while True:
    print("\n--- MENU ESERCIZI ---")
    print("1. Ciclo while (somma di numeri)")
    print("2. Ciclo for (lettere di una parola)")
    print("3. Ciclo range (sequenza con step)")
    print("0. Esci")
    
    scelta = input("Scegli un esercizio (0-3): ")
    
    if scelta == '1':    #ES1
        print("\n--- Esercizio 1: Ciclo while ---")
        somma = 0
        numero = int(input("Inserisci un numero intero (0 per terminare): "))
        while numero != 0:
            somma += numero
            numero = int(input("Inserisci un numero intero (0 per terminare): "))
        print(f"La somma totale dei numeri inseriti è: {somma}")
        
    elif scelta == '2':   #ES2
        print("\n--- Esercizio 2: Ciclo for ---")
        parola = input("Inserisci una parola: ")
        for lettera in parola:
            print(lettera)
            
    elif scelta == '3':  #ES3
        print("\n--- Esercizio 3: Ciclo range ---")
        N = int(input("Inserisci il valore massimo (N): "))
        step = int(input("Inserisci il passo (step): "))
        for i in range(0, N + 1, step):
            print(i)
            
    elif scelta == '0':
        print("Uscita dal programma. Arrivederci!")
        break
        
    else:
        print("Scelta non valida. Riprova inserendo un numero da 0 a 3.")