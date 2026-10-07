#6

numeri = []

numeri.append(int(input("Inserisci il primo numero: ")))

numeri.append(int(input("Inserisci il secondo numero: ")))

numeri.append(int(input("Inserisci il terzo numero: ")))

numeri.append(int(input("Inserisci il quarto numero: ")))

numeri.append(int(input("Inserisci il quinto numero: ")))


if len(numeri) == 0:

    print("Lista vuota")

else:

    massimo = numeri[0]

    for numero in numeri:

        if numero > massimo:
            massimo = numero


    contatore = 0

    while contatore < len(numeri):
        contatore = contatore + 1


    print("Il numero massimo trovato è:", massimo)
    print("Il numero di elementi presenti nella lista è:", contatore)