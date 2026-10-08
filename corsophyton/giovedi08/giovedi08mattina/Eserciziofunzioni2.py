#2

def fibonacci_fino_a_n():
    print("Ciao! Questo è un  Generatore Sequenza di Fibonacci ---")
    
    n = int(input("Inserisci il numero massimo N: "))               # 1. Chiediamo all'utente di inserire il numero limite N (convertendolo in intero)

    
    print(f"Sequenza di Fibonacci minore o uguale a (n):")
    
    a = 0               # 2. Inizializziamo i primi due numeri della sequenza

    b = 1
    
                # 3. Usiamo un ciclo for con un range grande  per calcolare i numeri
    for _ in range(100):
                 
        if a > n:           # Se il numero 'a' supera il limite N, ci fermiamo con il break
            break
            
                
        print(a, end=" ")            # Stampiamo il numero corrente sulla stessa riga
        
                 
        prossimo = a + b
        a = b           # Aggiorniamo i valori per il prossimo giro
        b = prossimo                                     # (il nuovo 'a' diventa 'b', e il nuovo 'b' diventa la somma di a + b)

        
    print()             # Andiamo a capo alla fine della stampa

fibonacci_fino_a_n()       # Chiamiamo la funzione per testarla
     