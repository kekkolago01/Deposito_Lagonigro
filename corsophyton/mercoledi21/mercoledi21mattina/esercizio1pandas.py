import pandas as pd
import numpy as np

# ==========================================
# 1. CREAZIONE DEI DATI E DEL DATAFRAME
# ==========================================
# Creiamo un dizionario con liste semplici di dati, inserendo qualche duplicato e qualche valore mancante (None)
dati = {
    'Nome': ['Anna', 'Mario', 'Luigi', 'Anna', 'Giulia', 'Marco', 'Sara'],
    'Età': [17, 25, 45, 17, 70, None, 30],
    'Città': ['Roma', 'Milano', 'Napoli', 'Roma', 'Torino', 'Firenze', 'Roma'],
    'Salario': [1200, 1500, 2500, 1200, 3000, 2200, None]
}

# Trasformiamo il dizionario in un DataFrame (la tabella di pandas)
df = pd.DataFrame(dati)

print("--- 1. IL NOSTRO DATAFRAME ---")
print(df)
print("\n" + "="*40 + "\n")


# ==========================================
# 2. VISUALIZZARE PRIME E ULTIME RIGHE
# ==========================================
# .head() mostra le prime righe (di default 5)
print("--- PRIME RIGHE (.head()) ---")
print(df.head())

# .tail() mostra le ultime righe (di default 5)
print("\n--- ULTIME RIGHE (.tail()) ---")
print(df.tail())
print("\n" + "="*40 + "\n")


# ==========================================
# 3. VEDERE IL TIPO DI DATI DELLE COLONNE
# ==========================================
# .dtypes ci dice se una colonna contiene numeri, parole (object), ecc.
print("--- TIPO DI DATI DI OGNI COLONNA ---")
print(df.dtypes)
print("\n" + "="*40 + "\n")


# ==========================================
# 4. STATISTICHE DESCRITTIVE DI BASE
# ==========================================
# .describe() calcola automaticamente il conteggio, media, min, max e i percentili per le colonne numeriche
print("--- STATISTICHE DESCRITTIVE ---")
print(df.describe())

# Per vedere esplicitamente la mediana e la deviazione standard
print("\nMediana delle colonne numeriche:")
print(df.median(numeric_only=True))

print("\nDeviazione standard delle colonne numeriche:")
print(df.std(numeric_only=True))
print("\n" + "="*40 + "\n")


# ==========================================
# 5. RIMUOVERE I DUPLICATI
# ==========================================
# .drop_duplicates() cancella le righe che sono esattamente identiche ad altre
df = df.drop_duplicates()

print("--- DATAFRAME SENZA DUPLICATI ---")
print(df)
print("\n" + "="*40 + "\n")


# ==========================================
# 6. GESTIRE I VALORI MANCANTI
# ==========================================
# Calcoliamo la mediana delle colonne Età e Salario
mediana_eta = df['Età'].median()
mediana_salario = df['Salario'].median()

# Sostituiamo i valori mancanti (NaN) con la rispettiva mediana usando .fillna()
df['Età'] = df['Età'].fillna(mediana_eta)
df['Salario'] = df['Salario'].fillna(mediana_salario)

print("--- DATAFRAME SENZA VALORI MANCANTI ---")
print(df)
print("\n" + "="*40 + "\n")


# ==========================================
# 7. AGGIUNGERE LA NUOVA COLONNA "Categoria Età"
# ==========================================
# Creiamo una lista vuota per raccogliere le categorie
categorie = []

# Facciamo un semplice ciclo riga per riga per controllare l'età
for eta in df['Età']:
    if eta <= 18:
        categorie.append('Giovane')
    elif eta <= 65:
        categorie.append('Adulto')
    else:
        categorie.append('Senior')

# Aggiungiamo la lista come nuova colonna del DataFrame
df['Categoria Età'] = categorie

print("--- DATAFRAME FINALE CON CATEGORIE ---")
print(df)