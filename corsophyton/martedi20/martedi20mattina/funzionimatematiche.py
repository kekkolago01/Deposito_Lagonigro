import numpy as np

# Per garantire la riproducibilità dei numeri casuali
np.random.seed(42)

# ==========================================
# 1. CREAZIONE DELL'ARRAY CON linspace
# ==========================================
# np.linspace(start, stop, num) crea un array di 'num' valori 
# equidistanti compresi tra 'start' e 'stop' (inclusi).
array_linspace = np.linspace(0, 1, 12)

print("--- 1. ARRAY ORIGINALE (linspace) ---")
print(array_linspace)
print("-" * 40)


# ==========================================
# 2. CAMBIO DI FORMA CON reshape (3x4)
# ==========================================
# Il metodo .reshape(righe, colonne) riorganizza i 12 elementi 
# in una nuova struttura a matrice bidimensionale (3 righe e 4 colonne).
matrice_linspace = array_linspace.reshape(3, 4)

print("--- 2. MATRICE TRASFORMATA (3x4) ---")
print(matrice_linspace)
print("-" * 40)


# ==========================================
# 3. GENERAZIONE DI UNA MATRICE CASUALE (3x4)
# ==========================================
# np.random.rand(righe, colonne) genera una matrice con numeri 
# casuali a virgola mobile compresi uniformemente tra 0 e 1.
matrice_casuale = np.random.rand(3, 4)

print("--- 3. MATRICE CASUALE (3x4) ---")
print(matrice_casuale)
print("-" * 40)


# ==========================================
# 4. CALCOLO E STAMPA DELLE SOMME
# ==========================================
# Il metodo .sum() calcola la somma algebrica di tutti gli elementi 
# presenti all'interno dell'array o della matrice.
somma_linspace = matrice_linspace.sum()
somma_casuale = matrice_casuale.sum()

print("--- 4. CALCOLO DELLE SOMME ---")
print(f"Somma degli elementi della matrice linspace: {somma_linspace:.4f}")
print(f"Somma degli elementi della matrice casuale: {somma_casuale:.4f}")
print("-" * 40)