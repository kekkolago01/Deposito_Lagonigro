import numpy as np

# Per fare in modo che i numeri casuali siano sempre gli stessi ad ogni esecuzione (facoltativo ma utile per il debug)
np.random.seed(42)

# ==========================================
# 1. CREAZIONE DELL'ARRAY 1D
# ==========================================
# np.random.randint(low, high, size) genera interi casuali. 
# 'high=51' serve per includere il numero 50 (il limite superiore è escluso).
array_originale = np.random.randint(10, 51, size=20)
print("--- 1. ARRAY ORIGINALE ---")
print(array_originale)
print("-" * 40)

# ==========================================
# 2. ESTRAZIONE DEI PRIMI 10 ELEMENTI
# ==========================================
# Lo slicing [:10] prende tutti gli elementi dall'inizio fino all'indice 10 (escluso)
primi_10 = array_originale[:10]
print("--- 2. Primi 10 elementi ---")
print(primi_10)
print("-" * 40)

# ==========================================
# 3. ESTRAZIONE DEGLI ULTIMI 5 ELEMENTI
# ==========================================
# L'indice negativo [-5:] parte a contare gli ultimi 5 elementi partendo dalla fine dell'array
ultimi_5 = array_originale[-5:]
print("--- 3. Ultimi 5 elementi ---")
print(ultimi_5)
print("-" * 40)

# ==========================================
# 4. ESTRAZIONE DALL'INDICE 5 AL 15 (ESCLUSO)
# ==========================================
# [5:15] prende gli elementi a partire dall'indice 5 fino al 14
elementi_mezzo = array_originale[5:15]
print("--- 4. Elementi dall'indice 5 al 15 (escluso) ---")
print(elementi_mezzo)
print("-" * 40)

# ==========================================
# 5. ESTRAZIONE DI OGNI TERZO ELEMENTO
# ==========================================
# Usiamo la sintassi [inizio:fine:passo]. Omettendo inizio e fine, 
# prendiamo tutto l'array con un passo di 3 (ogni 3 elementi ne seleziona uno).
ogni_terzo = array_originale[::3]
print("--- 5. Ogni terzo elemento ---")
print(ogni_terzo)
print("-" * 40)

# ==========================================
# 6. MODIFICA TRAMITE SLICING
# ==========================================
# Creiamo una copia dell'array originale per vedere la modifica senza perdere il riferimento iniziale
array_modificato = array_originale.copy()

# Assegniamo il valore 99 a tutti gli elementi compresi tra l'indice 5 e il 10 (escluso)
array_modificato[5:10] = 99

print("--- 6 & 7. Array dopo la modifica tramite slicing (indici 5-9 a 99) ---")
print("Array originale (inalterato):")
print(array_originale)
print("\nArray modificato:")
print(array_modificato)
print("-" * 40)