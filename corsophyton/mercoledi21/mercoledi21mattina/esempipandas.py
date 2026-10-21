import pandas as pd

# Creazione di un DataFrame con dati di esempio
data = {
'Nome': ['Alice', 'Bob', 'Carla'],
'Età': [25, 30, 22],
'Città': ['Roma', 'Milano', 'Napoli']
}

# aggiunta di una chiave al dizionario
data["Sesso"] = ["F","M","F"]

df = pd.DataFrame(data)


#print("")
#print("----Dataframe Originale----")
#print (df.head(2))
#print (df.tail(2))
#print (df.describe())
#print (df.info())


df_scv = pd.read_csv("corsophyton\mercoledi21\mercoledi21mattina\studenti.csv")
print(df_scv)