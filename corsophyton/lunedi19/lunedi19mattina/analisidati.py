import numpy as np

# ==========================================
# 1. CREAZIONE DELL'ARRAY
# ==========================================
# np.arange crea un array con numeri interi da 10 incluso fino a 49 escluso. 
# Per includere il 49, impostiamo il limite superiore a 50.
array_interi = np.arange(10, 50)

# ==========================================
# 2. VERIFICA DEL TIPO DI DATO (dtype) INIZIALE
# ==========================================
print("--- TIPO DI DATO INIZIALE ---")
print(f"Array: {array_interi}")
# L'attributo .dtype restituisce il tipo di dato degli elementi contenuti nell'array
print(f"Tipo di dato (dtype): {array_interi.dtype}")


# ==========================================
# 3. CONVERSIONE DEL TIPO DI DATO IN float64
# ==========================================
# Il metodo .astype() permette di convertire l'array in un nuovo tipo di dato (in questo caso float64)
array_float = array_interi.astype(np.float64)

print("\n--- TIPO DI DATO DOPO LA CONVERSIONE ---")
print(f"Array convertito: {array_float}")
print(f"Nuovo tipo di dato (dtype): {array_float.dtype}")


# ==========================================
# 4. VERIFICA DELLA FORMA (shape) DELL'ARRAY
# ==========================================
print("\n--- FORMA DELL'ARRAY ---")
# L'attributo .shape restituisce una tupla che indica la dimensione dell'array lungo ciascuna asse
print(f"Forma (shape) dell'array: {array_float.shape}")