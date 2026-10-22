import pandas as pd
import numpy as np

# Per fare in modo che i dati casuali siano sempre gli stessi ogni volta che eseguiamo il codice
np.random.seed(42)

# ==========================================
# 1. GENERAZIONE DEI DATI CASUALI (Un mese di vendite)
# ==========================================
# Creiamo un elenco di date per un mese (ad esempio, 30 giorni di gennaio)
date = pd.date_range(start="2026-01-01", periods=30, freq="D")

# Scegliamo le tre città e i tre prodotti richiesti
citta = ['Roma', 'Milano', 'Napoli']
prodotti = ['Laptop', 'Smartphone', 'Tablet']

# Per creare una tabella di vendite, ripetiamo le combinazioni o generiamo righe casuali
# Creiamo 100 righe di dati casuali per un mese
n_righe = 100

dati_casuali = {
    "Data": np.random.choice(date, n_righe),
    "Città": np.random.choice(citta, n_righe),
    "Prodotto": np.random.choice(prodotti, n_righe),
    "Vendite": np.random.randint(100, 2000, n_righe)  # Valori di vendita casuali tra 100 e 2000 euro
}

# Trasformiamo il dizionario in un DataFrame di pandas
df = pd.DataFrame(dati_casuali)

print("--- PRIME RIGHE DEL DATASET DI VENDITE ---")
print(df.head())
print("\n" + "="*50 + "\n")


# ==========================================
# 2. CREAZIONE DELLA TABELLA PIVOT
# ==========================================
# Vogliamo analizzare le vendite medie di ciascun prodotto per città
# Usiamo pd.pivot_table indicando:
# - index: le righe saranno le Città
# - columns: le colonne saranno i Prodotti
# - values: i valori da calcolare saranno le Vendite
# - aggfunc: la funzione di aggregazione sarà la media ('mean')
tabella_pivot = pd.pivot_table(
    df, 
    index='Città', 
    columns='Prodotto', 
    values='Vendite', 
    aggfunc='mean'
)

print("--- TABELLA PIVOT: VENDITE MEDIE PER PRODOTTO E CITTÀ ---")
print(tabella_pivot)
print("\n" + "="*50 + "\n")


# ==========================================
# 3. APPLICAZIONE DI GROUPBY
# ==========================================
# Vogliamo calcolare le vendite totali per ogni prodotto
# Raggruppiamo per 'Prodotto' e sommiamo la colonna 'Vendite'
vendite_totali_prodotto = df.groupby('Prodotto')['Vendite'].sum()

print("--- VENDITE TOTALI PER CIASCUN PRODOTTO (groupby) ---")
print(vendite_totali_prodotto)