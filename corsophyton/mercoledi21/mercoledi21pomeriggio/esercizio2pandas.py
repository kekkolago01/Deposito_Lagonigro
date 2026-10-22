import pandas as pd

# 1. Carichiamo il nostro file CSV dal computer usando il percorso
percorso = r"C:\Users\kekkolago\Downloads\mcu-movies.csv"
tabella = pd.read_csv(percorso)

# 2. Vediamo le prime righe della tabella per capire com'è fatta
print("--- LE PRIME RIGHE DELLA TABELLA ---")
print(tabella.head())

# 3. Puliamo un po' i dati (togliamo le righe vuote)
tabella_pulita = tabella.dropna(subset=['movie']).copy()

# Puliamo la colonna dei soldi togliendo le virgole e trasformandola in numeri
tabella_pulita['box_office'] = tabella_pulita['box_office'].astype(str).str.replace(',', '').astype(float)

# 4. Creiamo due nuove colonne con semplici operazioni matematiche (+ e -)
# Prima nuova colonna: Il guadagno (Incassi meno il Budget)
tabella_pulita['guadagno'] = tabella_pulita['box_office'] - tabella_pulita['budget']

# Seconda nuova colonna: La differenza tra il voto del pubblico e quello della critica
tabella_pulita['differenza_voti'] = tabella_pulita['rt_audience_score'] - tabella_pulita['rt_critic_score']

# 5. Facciamo vedere il risultato finale con le nostre nuove colonne
print("\n--- LA TABELLA CON LE NOSTRE NUOVE COLONNE ---")
colarde_da_vedere = ['movie', 'budget', 'box_office', 'guadagno', 'differenza_voti']
print(tabella_pulita[colarde_da_vedere].head(10))