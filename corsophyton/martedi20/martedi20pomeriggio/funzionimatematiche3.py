import numpy as np

# ESERCIZIO 1: Somma, Media e Broadcasting base

# 1. Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
array_15 = np.random.randint(1, 101, size=15)
print("Array originale:", array_15)

# Esempio di broadcasting: sommiamo il numero 10 a tutti gli elementi dell'array in un unico passaggio

array_con_broadcasting = array_15 + 10
print("Array dopo il broadcasting (+10 a ogni elemento):", array_con_broadcasting)


somma_elementi = array_15.sum()         # 2. Calcolare e stampare la somma di tutti gli elementi dell'array
print("Somma degli elementi:", somma_elementi)


media_elementi = array_15.mean()            # 3. Calcolare e stampare la media di tutti gli elementi dell'array
print("Media degli elementi:", media_elementi)

print("-" * 50)


# ESERCIZIO 2: Manipolazione di Array Multidimensionali

# 1. Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25
matrice_5x5 = np.arange(1, 26).reshape(5, 5)
print("Matrice 5x5:")
print(matrice_5x5)

# 2. Estrarre e stampare la seconda colonna della matrice
seconda_colonna = matrice_5x5[:, 1]
print("Seconda colonna (indice 1):", seconda_colonna)

# 3. Estrarre e stampare la terza riga della matrice.
terza_riga = matrice_5x5[2, :]
print("Terza riga (indice 2):", terza_riga)

# 4. Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
somma_diagonale = np.diagonal(matrice_5x5).sum()
print("Somma della diagonale principale:", somma_diagonale)

print("-" * 50)


# ESERCIZIO 3: Operazioni con Fancy Indexing


# 1. Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
matrice_4x4 = np.random.randint(10, 51, size=(4, 4))
print("Matrice 4x4 originale:")
print(matrice_4x4)

# 2. Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).
righe = np.array([0, 1, 2, 3])
colonne = np.array([1, 3, 2, 0])
elementi_selezionati = matrice_4x4[righe, colonne]
print("Elementi selezionati (fancy indexing):", elementi_selezionati)

# 3. Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array.
righe_dispari = matrice_4x4[[1, 3], :]
print("Righe dispari:")
print(righe_dispari)

# 4. Modificare gli elementi selezionati nel primo punto aggiungendo 10 al loro valore.
matrice_4x4[righe, colonne] += 10
print("Matrice 4x4 dopo la modifica (aggiunta di 10 tramite broadcasting agli elementi scelti):")
print(matrice_4x4)