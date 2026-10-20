import numpy as np

# Impostiamo la riproducibilità dei numeri casuali
np.random.seed(42)

# Nome del file di testo per il salvataggio dei dati
NOME_FILE = "risultati_numpy.txt"

# ==========================================
# 1. CREAZIONE DELL'ARRAY CON linspace
# ==========================================
# np.linspace(start, stop, num) genera 50 valori equidistanti tra 0 e 10 (inclusi)
array_linspace = np.linspace(0, 10, 50)


# ==========================================
# 2. CREAZIONE DELL'ARRAY CASUALE
# ==========================================
# np.random.random(size) genera 50 numeri casuali compresi tra 0.0 e 1.0
array_casuali = np.random.random(50)


# ==========================================
# 3. SOMMA ELEMENTO PER ELEMENTO
# ==========================================
# Somma vettoriale: somma ciascun elemento di array_linspace con il corrispondente di array_casuali
array_somma = array_linspace + array_casuali


# ==========================================
# 4 & 5. CALCOLO DELLE SOMME (TOTALE E FILTRATA)
# ==========================================
# Calcola la somma di tutti gli elementi del nuovo array
somma_totale = array_somma.sum()

# Maschera booleana per selezionare solo gli elementi maggiori di 5 e calcolarne la somma
elementi_maggiori_5 = array_somma[array_somma > 5]
somma_maggiori_5 = elementi_maggiori_5.sum()


# ==========================================
# 6. STAMPA A SCHERMO DEI RISULTATI
# ==========================================
print("--- 1. ARRAY LINSPACE (50 elementi tra 0 e 10) ---")
print(array_linspace)
print("-" * 50)

print("\n--- 2. ARRAY CASUALE (50 elementi tra 0 e 1) ---")
print(array_casuali)
print("-" * 50)

print("\n--- 3. NUOVO ARRAY (Somma elemento per elemento) ---")
print(array_somma)
print("-" * 50)

print("\n--- 4 & 5. RISULTATI DELLE SOMME ---")
print(f"Somma totale degli elementi del nuovo array: {somma_totale:.4f}")
print(f"Somma degli elementi maggiori di 5: {somma_maggiori_5:.4f}")
print("-" * 50)


# ==========================================
# 7. SALVATAGGIO DEI DATI SU FILE TXT
# ==========================================
# Apriamo il file in modalità 'w' (write) usando la gestione dei contesti 'with'
try:
    with open(NOME_FILE, 'w', encoding='utf-8') as file:
        file.write("=== RISULTATI ESERCIZIO NUMPY ===\n\n")
        
        file.write("--- 1. ARRAY LINSPACE ---\n")
        # Ciclo per scrivere elemento per elemento
        for val in array_linspace:
            file.write(f"{val:.4f}\n")
        file.write("\n")
        
        file.write("--- 2. ARRAY CASUALI ---\n")
        for val in array_casuali:
            file.write(f"{val:.4f}\n")
        file.write("\n")
        
        file.write("--- 3. ARRAY SOMMA ---\n")
        for val in array_somma:
            file.write(f"{val:.4f}\n")
        file.write("\n")
        
        file.write("--- STATISTICHE ---\n")
        file.write(f"Somma totale: {somma_totale:.4f}\n")
        file.write(f"Somma elementi > 5: {somma_maggiori_5:.4f}\n")

    print(f"\nTutti i dati sono stati salvati con successo nel file: '{NOME_FILE}'")

except Exception as e:
    print(f"Errore durante il salvataggio sul file: {e}")