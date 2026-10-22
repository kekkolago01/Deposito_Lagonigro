import pandas as pd

# Caricamento dei 3 file CSV 
df_iscritti = pd.read_csv(r'C:\Users\kekkolago\OneDrive\Documenti\GitHub\Deposito_Lagonigro\corsophyton\giovedi22\giovedi22mattina\iscritti.csv')
df_presenze = pd.read_csv(r'C:\Users\kekkolago\OneDrive\Documenti\GitHub\Deposito_Lagonigro\corsophyton\giovedi22\giovedi22mattina\presenze.csv')
df_costi = pd.read_csv(r'C:\Users\kekkolago\OneDrive\Documenti\GitHub\Deposito_Lagonigro\corsophyton\giovedi22\giovedi22mattina\costi_abbonamento.csv')

# ==========================================
# 1. PULIZIA DEI DATI ISCRITTI
# ==========================================
print("--- 1. PULIZIA ISCRITTI ---")

# Rimuoviamo eventuali duplicati
df_iscritti = df_iscritti.drop_duplicates()

# Gestiamo il valore mancante nell'età sostituendolo con la mediana
mediana_eta = df_iscritti['Eta'].median()
df_iscritti['Eta'] = df_iscritti['Eta'].fillna(mediana_eta)

print(df_iscritti)
print("\n" + "="*50 + "\n")

# ==========================================
# 2. ANALISI DELLE PRESENZE
# ==========================================
print("--- 2. ANALISI PRESENZE ---")

# Totale partecipanti per ciascun corso
partecipanti_per_corso = df_presenze.groupby('Corso')['Partecipanti'].sum()
print("Partecipanti totali per corso:")
print(partecipanti_per_corso)

print("\n" + "="*50 + "\n")

# ==========================================
# 3. REPORT RIEPILOGATIVO FINALE
# ==========================================
print("--- 3. REPORT RIEPILOGATIVO ---")

# Uniamo la tabella degli iscritti con quella dei costi in base al tipo di abbonamento
df_report = pd.merge(df_iscritti, df_costi, on='Tipo_Abbonamento', how='left')

print(df_report[['Nome', 'Citta', 'Tipo_Abbonamento', 'Costo_Mensile']])

# Calcoliamo l'incasso mensile totale del centro sportivo
incasso_totale = df_report['Costo_Mensile'].sum()
print(f"\nIncasso mensile totale del centro sportivo: {incasso_totale} €")