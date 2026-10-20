import numpy as np

# Per garantire la riproducibilità dei numeri casuali
np.random.seed(42)

# ==========================================
# 1. CREAZIONE DELL'ARRAY COMBINATO
# ==========================================
# Creiamo la prima parte con np.arange da 0 a 50 (escluso) -> 50 elementi (da 0 a 49)
parte_arange = np.arange(0, 50)

# Creazione della seconda parte con 50 numeri interi casuali compresi tra 49 e 101 (101 escluso)
parte_casuali = np.random.randint(49, 101, size=50)

# Uniamo i due array in un unico array ndarray di 100 elementi
array_originale = np.concatenate([parte_arange, parte_casuali])

print("--- 1. ARRAY ORIGINALE INIZIALE ---")
print(array_originale)
print(f"Tipo di dato (dtype): {array_originale.dtype}")[cite: 2]
print(f"Forma (shape): {array_originale.shape}")[cite: 2]
print("-" * 50)


# ==========================================
# 2. MODIFICA DEL TIPO DI DATO (dtype) IN float64
# ==========================================
# Convertiamo l'array nel tipo float64 utilizzando il metodo .astype()
array_originale = array_originale.astype(np.float64)

print("--- 2. DOPO LA CONVERSIONE IN float64 ---")
print(f"Nuovo tipo di dato (dtype): {array_originale.dtype}")
print(f"Nuova forma (shape): {array_originale.shape}")
print("-" * 50)


# ==========================================
# 3. ESTRAZIONE TRAMITE SLICING
# ==========================================
# Estraiamo i primi 10 elementi
primi_10 = array_originale[:10]

# Estraiamo gli ultimi 7 elementi usando indici negativi
ultimi_7 = array_originale[-7:]

# Estraiamo gli elementi dall'indice 5 all'indice 20 escluso
da_5_a_20 = array_originale[5:20]

# Estraiamo ogni quarto elemento usando il passo pari a 4
ogni_quarto = array_originale[::4]


# ==========================================
# 4. MODIFICA TRAMITE SLICING (Indici da 10 a 15 escluso)
# ==========================================
# Assegniamo il valore 999 agli elementi compresi tra l'indice 10 e il 15 (escluso)
array_originale[10:15] = 999


# ==========================================
# 5. UTILIZZO DELLA FANCY INDEXING
# ==========================================
# Selezione degli elementi in posizioni specifiche
indici_specifici = [0, 3, 7, 12, 25, 33, 48]
elementi_specifici = array_originale[indici_specifici]

# Maschera booleana per selezionare tutti gli elementi pari
maschera_pari = (array_originale % 2 == 0)
elementi_pari = array_originale[maschera_pari]

# Selezione di tutti gli elementi maggiori della media dell'array
media_array = np.mean(array_originale)
elementi_maggiori_media = array_originale[array_originale > media_array]


# ==========================================
# 6. STAMPA FINALE DEI RISULTATI
# ==========================================
print("--- 6. ARRAY ORIGINALE DOPO LE MODIFICHE ---")
print(array_originale)
print("-" * 50)

print("--- SOTTO-ARRAY OTTENUTI TRAMITE SLICING ---")
print(f"Primi 10 elementi: {primi_10}")
print(f"Ultimi 7 elementi: {ultimi_7}")
print(f"Elementi dall'indice 5 al 20: {da_5_a_20}")
print(f"Ogni quarto elemento: {ogni_quarto}")
print("-" * 50)

print("--- SOTTO-ARRAY OTTENUTI TRAMITE FANCY INDEXING ---")
print(f"Elementi in posizioni {indici_specifici}: {elementi_specifici}")
print(f"Elementi pari (maschera booleana): {elementi_pari}")
print(f"Elementi maggiori della media ({media_array:.2f}): {elementi_maggiori_media}")
print("-" * 50)