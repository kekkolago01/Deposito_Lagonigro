
class ContoBancario:
    def __init__(self, titolare, saldo_iniziale=0.0):           # Inizializziamo l'attributo privato del titolare impostandolo prima a stringa vuota
        self.__titolare = ""
       
        self.set_titolare(titolare)          # Sfruttiamo il metodo setter per validare e assegnare il nome del titolare in modo sicuro
        
        
        self.__saldo = 0.0
        if saldo_iniziale >= 0:         # Inizializziamo l'attributo privato del saldo verificando che non sia negativo
            self.__saldo = float(saldo_iniziale)
        else:
            print("Errore: Il saldo iniziale non può essere negativo. Impostato a 0.0.")


    # ==========================================
    # METODI GETTER E SETTER (Incapsulamento)
    # ==========================================
    def get_titolare(self):          # Metodo Getter: restituisce in modo sicuro il valore dell'attributo privato __titolare
       
        return self.__titolare

    def set_titolare(self, nuovo_titolare):         # Metodo Setter con validazione: controlla che il nuovo valore sia una stringa e non sia vuota prima di assegnarlo
        
        if isinstance(nuovo_titolare, str) and nuovo_titolare.strip():
            self.__titolare = nuovo_titolare.strip()
        else:
            print("Errore: Il titolare deve essere una stringa non vuota.")


    # ==========================================
    # METODI OPERATIVI PUBBLICI
    # ==========================================
    def visualizza_saldo(self):
        
        print(f"Il saldo del conto di {self.__titolare} è: {self.__saldo} €")           # Stampa il saldo corrente protetto e restituisce il valore senza permettere modifiche dirette esterne
        return self.__saldo

    def deposita(self, importo):
        
        if importo > 0:         # Verifica che l'importo da depositare sia strettamente maggiore di zero per evitare valori negativi o nulli
            
            self.__saldo += importo         # Aggiorna l'attributo privato __titolare non direttamente, ma tramite logica interna sicura
            print(f"Deposito di {importo} € effettuato con successo.")
        else:
            print("Errore: L'importo del deposito deve essere maggiore di zero.")
            
    def preleva(self, importo):
        
        if importo <= 0:            # Controlla prima se l'importo richiesto è non valido (minore o uguale a zero)
            print("Errore: L'importo del prelievo deve essere maggiore di zero.")
        
        elif importo > self.__saldo:            # Controlla se l'importo supera il saldo disponibile per evitare un conto in rosso
            print("Errore: Saldo insufficiente per effettuare il prelievo.")
        else:
            
            self.__saldo -= importo         # Sottrae l'importo dal saldo privato solo se tutti i controlli di sicurezza sono superati
            print(f"Prelievo di {importo} € effettuato con successo.")


# ==========================================
# ESEMPIO DI UTILIZZO E TEST DELLA CLASSE
# ==========================================


conto = ContoBancario("Kekkolago", 100)         # Crea un'istanza (oggetto) della classe ContoBancario passando titolare e saldo iniziale

# Chiama il metodo pubblico per visualizzare lo stato attuale del saldo
conto.visualizza_saldo()            # Stampa: Il saldo del conto di Kekkolago è: 100.0 €

# Esegue un'operazione di deposito valida
conto.deposita(50)

# Mostra il saldo aggiornato dopo il deposito
conto.visualizza_saldo()            # Stampa: Il saldo del conto di Kekkolago è: 150.0 €

# Tenta di prelevare una cifra superiore al saldo disponibile (genera errore controllato)
conto.preleva(200)                  

# Esegue un prelievo valido entro i limiti del saldo
conto.preleva(40)

# Visualizza il saldo finale dopo tutte le operazioni
conto.visualizza_saldo()            # Stampa: Il saldo del conto di Kekkolago è: 110.0 €

# Utilizza il metodo getter per leggere l'attributo privato in modo sicuro dall'esterno
print(f"Titolare attuale: {conto.get_titolare()}")

