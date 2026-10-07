#5
numeri = []

numeri.append(int(input("Inserisci il primo numero: ")))
numeri.append(int(input("Inserisci il secondo numero: ")))
numeri.append(int(input("Inserisci il terzo numero: ")))
numeri.append(int(input("Inserisci il quarto numero: ")))
numeri.append(int(input("Inserisci il quinto numero: ")))

for numero in numeri:
    print(numero ** 2)