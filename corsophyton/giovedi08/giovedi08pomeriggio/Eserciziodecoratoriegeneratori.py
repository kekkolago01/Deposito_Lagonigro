import random

# 5. Funzione per determinare se un numero è primo
# Restituisce True se il numero è primo, altrimenti False
def è_primo(numero):
    # I numeri minori o uguali a 1 non sono primi
    if numero <= 1:
        return False
    
    # Controlliamo se ha divisori tra 2 e numero - 1 usando un ciclo for e range
    for i in range(2, numero):
        if numero % i == 0:
            return False # Trovato un divisore, non è primo
            
    return True # Se il ciclo finisce senza trovare divisori, è primo


# 1. Chiede all'utente un numero intero positivo n (continua finché non è valido)
def chiedi_n():
    while True:
        n = int(input("Inserisci un numero intero positivo n: "))
        if n > 0:
            return n
        print("Il numero deve essere maggiore di zero. Riprova.")


# 2. Genera una lista di numeri interi casuali tra 1 e n, di lunghezza n
def genera_lista(n):
    lista = []
    for _ in range(n):
        numero_casuale = random.randint(1, n)
        lista.append(numero_casuale)
    return lista


# 3. Calcola e stampa la somma dei numeri pari nella lista usando un ciclo for
def somma_pari(lista):
    somma = 0
    for num in lista:
        if num % 2 == 0: # Se il numero è pari
            somma += num
    print(f"Somma dei numeri pari: {somma}")


# 4. Stampa tutti i numeri dispari nella lista usando un ciclo for
def stampa_dispari(lista):
    print("Numeri dispari nella lista:")
    for num in lista:
        if num % 2 != 0: # Se il numero è dispari
            print(num, end=" ")
    print()


# 6. Stampa tutti i numeri primi presenti nella lista usando un ciclo for e la funzione è_primo
def stampa_primi_nella_lista(lista):
    print("Numeri primi presenti nella lista:")
    for num in lista:
        if è_primo(num):
            print(num, end=" ")
    print()


# 7. Verifica se la somma totale di tutti i numeri nella lista è un numero primo
def verifica_somma_totale(lista):
    somma_totale = sum(lista)
    print(f"Somma totale di tutti i numeri nella lista: {somma_totale}")
    
    if è_primo(somma_totale):
        print("Il risultato: La somma totale è un numero primo!")
    else:
        print("Il risultato: La somma totale NON è un numero primo.")


# 8. Menu principale per gestire tutte le funzioni
def menu():
    print("--- MENU ESERCITAZIONE ---")
    n = chiedi_n()
    
    # Generiamo la lista basata su n
    mia_lista = genera_lista(n)
    print(f"\nLista generata: {mia_lista}\n")
    
    # Richiamiamo le funzioni in sequenza come richiesto dai punti 3, 4, 6 e 7
    somma_pari(mia_lista)
    print("-" * 30)
    stampa_dispari(mia_lista)
    print("-" * 30)
    stampa_primi_nella_lista(mia_lista)
    print("-" * 30)
    verifica_somma_totale(mia_lista)

# Avviamo il programma chiamando il menu
menu()