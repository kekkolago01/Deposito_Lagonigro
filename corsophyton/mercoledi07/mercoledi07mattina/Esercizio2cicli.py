#2

# 1

numero = int(input("Inserisci un numero: "))

numeri_primi = []

for numero_controllato in range(numero, 100):

    divisori = 0

    for i in range(1, numero_controllato + 1):

        if numero_controllato % i == 0:
            divisori = divisori + 1

    if divisori == 2:

        numeri_primi.append(numero_controllato)

        print("Il numero è primo:", numero_controllato)

    else:

        print("Il numero non è primo:", numero_controllato)

    if len(numeri_primi) == 5:
        break

print("I primi 5 numeri primi sono:", numeri_primi)