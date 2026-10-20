import numpy as np

# Per garantire la riproducibilità dei numeri casuali ad ogni esecuzione
np.random.seed(42)

# ==========================================
# 1. CREAZIONE DELLA MATRICE 2D (6x6)
# ==========================================
# np.random.randint(low, high, size) genera interi casuali.
# 'high=101' serve per includere il 100 (il limite superiore è escluso).
matrice_originale = np.random.randint(1, 101, size=(6, 6))

print("--- 1. MATRICE ORIGINALE (6x6) ---")
print(matrice_originale)
print("-" * 40)


# ==========================================
# 2. ESTRAZIONE DELLA SOTTO-MATRICE CENTRALE (4x4)
# ==========================================
# Per estrarre una sottomatrice 4x4 dal centro di una 6x6, 
# prendiamo le righe e le colonne dall'indice 1 fino al 5 (escluso, cioè indici 1, 2, 3, 4).
sotto_matrice = matrice_originale[1:5, 1:5]

print("--- 2. SOTTO-MATRICE CENTRALE (4x4) ---")
print(sotto_matrice)
print("-" * 40)


# ==========================================
# 3. INVERSIONE DELLE RIGHE DELLA SOTTO-MATRICE
# ==========================================
# Lo slicing con passo -1 invertito sulle righe (::-1) capovolge l'ordine delle righe.
matrice_invertita = sotto_matrice[::-1, :]

print("--- 3. MATRICE CON RIGHE INVERTITE ---")
print(matrice_invertita)
print("-" * 40)


# ==========================================
# 4. ESTRAZIONE DELLA DIAGONALE PRINCIPALE
# ==========================================
# np.diagonal() estrae la diagonale principale dalla matrice invertita creando un array 1D.
diagonale_principale = np.diagonal(matrice_invertita)

print("--- 4. DIAGONALE PRINCIPALE ---")
print(diagonale_principale)
print("-" * 40)


# ==========================================
# 5. SOSTITUZIONE CONDIZIONALE (Multipli di 3 -> -1)
# ==========================================
# Creiamo una copia della matrice invertita per non modificare direttamente il passaggio precedente se vogliamo stamparle entrambe
matrice_modificata = matrice_invertita.copy()

# Sostituiamo con -1 tutti gli elementi che diviso per 3 danno resto 0 (multipli di 3)
matrice_modificata[matrice_modificata % 3 == 0] = -1

print("--- 5. MATRICE INVERTITA MODIFICATA (Multipli di 3 sostituiti con -1) ---")
print(matrice_modificata)
print("-" * 40)