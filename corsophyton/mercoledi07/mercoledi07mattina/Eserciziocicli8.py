
n = int(input("Inserisci un numero intero positivo n: ")) # 1. Utilizzare un ciclo while per garantire che l'utente inserisca un numero intero positivo n
while n <= 0:
    print("Il numero inserito non è positivo. Riprova.")
    n = int(input("Inserisci un numero intero positivo n: "))


somma_pari = 0    # 2. Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n
for i in range(1, n + 1):
    if i % 2 == 0:
        somma_pari += i


print(f"Numeri dispari da 1 a {n}:")   # 3. Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()  # Per andare a capo


if n < 2:  # 4. Utilizzare una struttura if per determinare se n è un numero primo
    is_primo = False
else:
    is_primo = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_primo = False
            break


print("\n--- RISULTATI ---")   # 5. Stampare tutto
print(f"Numero inserito (n): {n}")
print(f"La somma dei numeri pari da 1 a {n} è: {somma_pari}")

if is_primo:
    print(f"Il numero {n} è un numero primo.")
else:
    print(f"Il numero {n} non è un numero primo.")