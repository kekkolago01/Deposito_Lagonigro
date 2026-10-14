
class MembroSquadra:                #Classe  genitore che rappresenta un membro generico della squadra.

    def __init__(self, nome, eta):          # Inizializzazione degli attributi d'istanza
        
        self.nome = nome              # Stringa: memorizza il nome della persona
        self.eta = eta                # Intero: memorizza l'età della persona

    def descrivi(self):         #stampa le informazioni della classe membro
       
        print(f"Membro della squadra: {self.nome}, Età: {self.eta} anni.")

    def __str__(self):                  #Metodo speciale (dunder method): restituisce una stringa formattata quando l'oggetto viene stampato direttamente (es. con print()).

        return f"{self.nome} ({self.eta} anni)"




class Giocatore(MembroSquadra):     #definizione della classe figlia
   
    
    
    def __init__(self, nome, eta, ruolo, numero_maglia):            #Aggiunge attributi e comportamenti specifici del giocatore.
        
       
        super().__init__(nome, eta)         # super() richiama il costruttore della classe genitore (__init__ di MembroSquadra) per inizializzare nome ed età senza riscrivere il codice.
        
        # Attributi specifici del giocatore
        self.ruolo = ruolo                    # Es., attaccante, difensore, portiere
        self.numero_maglia = numero_maglia    # Intero o stringa per il numero di maglia

    def gioca_partita(self):            #Azione specifica che solo un giocatore può compiere in campo.
        
        print(f"Il giocatore {self.nome} (n. {self.numero_maglia}), nel ruolo di {self.ruolo}, scende in campo per giocare la partita.")


class Allenatore(MembroSquadra):               # Classe Allenatore eredita da MembroSquadra. Gestisce le informazioni e le azioni relative all'allenatore.

    
    def __init__(self, nome, eta, anni_di_esperienza):
        # Riutilizziamo il costruttore del genitore per nome ed età
        super().__init__(nome, eta)
        
        # Attributo specifico dell'allenatore
        self.anni_di_esperienza = anni_di_esperienza  

    def dirige_allenamento(self):            #Azione specifica dell'allenatore durante la sessione di lavoro.
      
        print(f"L'allenatore {self.nome} dirige la sessione di allenamento forte di {self.anni_di_esperienza} anni di esperienza.")


class Assistente(MembroSquadra):                #Classe Assistente eredita da MembroSquadra. Rappresenta lo staff tecnico/medico di supporto.

    
    
    def __init__(self, nome, eta, specializzazione):
        # Richiamo del costruttore della classe base
        super().__init__(nome, eta)
        
        # Attributo specifico dell'assistente
        self.specializzazione = specializzazione  # Es., fisioterapista, analista di gioco

    def supporta_team(self):             #Azione specifica per descrivere il supporto fornito al team.      
        print(f"L'assistente {self.nome}, specializzato come {self.specializzazione}, fornisce supporto tecnico e medico alla squadra.")



class Squadra: #Classe Squadra rappresenta la struttura che contiene un nome e una lista di oggetti (membri) di tipo diverso (Polimorfismo).
   
    def __init__(self, nome_squadra):
        self.nome_squadra = nome_squadra  
        self.membri = []                  # Lista vuota che conterrà i vari membri (Allenatore, Giocatori, Assistenti)

    def aggiungi_membro(self, membro):           #Metodo per aggiungere un oggetto membro alla lista della squadra.
        self.membri.append(membro)

    def __str__(self):          #Restituisce una stringa riassuntiva con il nome della squadra e il totale dei membri.
        return f"Squadra: {self.nome_squadra} (Membri totali: {len(self.membri)})"

    def gioca_contro(self, altra_squadra):          #Metodo che simula un incontro tra due oggetti di tipo Squadra.
        print(f"\n--- PARTITA: {self.nome_squadra} vs {altra_squadra.nome_squadra} ---")
        print(f"Fischio d'inizio! La squadra {self.nome_squadra} affronta in un match entusiasmante la squadra {altra_squadra.nome_squadra}.")




# Creazione della Squadra 1 e inserimento dei membri 
squadra_1 = Squadra("Leoni FC")
squadra_1.aggiungi_membro(Allenatore("Roberto", 52, 15))
squadra_1.aggiungi_membro(Giocatore("Marco", 24, "attaccante", 9))
squadra_1.aggiungi_membro(Assistente("Davide", 38, "fisioterapista"))

# Creazione della Squadra 2 e dei rispettivi membri
squadra_2 = Squadra("Tigri United")
squadra_2.aggiungi_membro(Allenatore("Stefano", 60, 22))
squadra_2.aggiungi_membro(Giocatore("Alessandro", 27, "difensore", 5))
squadra_2.aggiungi_membro(Assistente("Matteo", 31, "analista di gioco"))



# Test per la Squadra 1
print(squadra_1)  

# Ciclo for per scorrere tutti i membri della squadra
for membro in squadra_1.membri:
    # 1. Metodo ereditato dalla classe base: funziona per qualsiasi membro
    membro.descrivi()
    
    # 2. Controllo del tipo (isinstance) per eseguire il metodo specifico corretto (Polimorfismo / Type Checking)
    if isinstance(membro, Giocatore):
        membro.gioca_partita()
    elif isinstance(membro, Allenatore):
        membro.dirige_allenamento()
    elif isinstance(membro, Assistente):
        membro.supporta_team()

print("\n" + "-"*40 + "\n")

# Test per la Squadra 2 (stessa logica iterativa)
print(squadra_2)
for membro in squadra_2.membri:
    membro.descrivi()
    if isinstance(membro, Giocatore):
        membro.gioca_partita()
    elif isinstance(membro, Allenatore):
        membro.dirige_allenamento()
    elif isinstance(membro, Assistente):
        membro.supporta_team()

# Simulazione della partita finale tra le due squadre
squadra_1.gioca_contro(squadra_2)