import pandas as pd
import numpy as np

# 1. Carichiamo il file CSV dei prodotti dal computer
percorso = r"C:\Users\kekkolago\Downloads\products.csv"
tabella = pd.read_csv(percorso)

# Puliamo i nomi delle colonne nel caso ci siano spazi vuoti di troppo
tabella.columns = tabella.columns.str.strip()

print("--- 1. LE PRIME RIGHE DELLA TABELLA ---")
print(tabella.head(3))


# 2. Aggiungiamo una colonna "Città" casuale per poter fare l'esercizio
# Creiamo una lista di città d'Italia da assegnare ai prodotti
citta_disponibili = ['Roma', 'Milano', 'Napoli', 'Torino', 'Firenze']

# Assegniamo casualmente una città a ciascuna riga della tabella
np.random.seed(42)  # Per avere sempre le stesse città casuali
tabella['Città'] = np.random.choice(citta_disponibili, size=len(tabella))


# 3. Aggiungiamo la colonna "Totale Vendite" (Quantità stock per Prezzo)
tabella['Totale Vendite'] = tabella['stockOnHand'] * tabella['price']


# 4. VISUALIZZARE IL NUMERO DI VENDITE PER OGNI CITTÀ
# Usiamo .value_counts() che conta quante volte compare ciascuna città nella colonna
vendite_per_citta = tabella['Città'].value_counts()

print("\n--- 4. NUMERO DI RECORD / VENDITE PER OGNI CITTÀ ---")
print(vendite_per_citta)


# 5. Raggruppiamo i dati per Città per vedere anche i guadagni totali di ogni città
guadagni_per_citta = tabella.groupby('Città')['Totale Vendite'].sum()

print("\n--- 5. GUADAGNO TOTALE PER OGNI CITTÀ ---")
print(guadagni_per_citta)