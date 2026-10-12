class ContoCorrente:
    def __init__(self, intestatario, saldo=0.0):
        self.intestatario = intestatario
        self.saldo = saldo
        
    def deposita(self, importo):            #Aggiunge un importo al saldo se è positivo.
        
        if importo > 0:
            self.saldo += importo
        else:
            print("Errore: L'importo del deposito deve essere maggiore di zero.")
            
    def preleva(self, importo):
        if importo <= 0:                    #Sottrae un importo dal saldo se il saldo è sufficiente e l'importo è valido.

            print("Errore: L'importo del prelievo deve essere maggiore di zero.")
        elif importo > self.saldo:
            print("Errore: Saldo insufficiente per effettuare il prelievo.")
        else:
            self.saldo -= importo
            
    def stampa_saldo(self):
        print(f"Il saldo di {self.intestatario} è: {self.saldo} €")                 #Stampa il saldo attuale del conto.


            # Esempio di utilizzo:
conto = ContoCorrente("Kekkolago", 100)
conto.stampa_saldo()             # Stampa: Il saldo di Kekkolago è: 100 €

conto.deposita(50)
conto.stampa_saldo()            # Stampa: Il saldo di Kekkolago è: 150.0 €

conto.preleva(200)               # Stampa un messaggio di errore (saldo insufficiente)
conto.preleva(40)
conto.stampa_saldo()             # Stampa: Il saldo di Kekkolago è: 110.0 €