class MembroSquadra:
    def __init__(self, nome, eta):
        self.nome = nome             # stringa
        self.eta = eta              # intero

    def descrivi(self):
        
        print(f"Membro della squadra: {self.nome}, Età: {self.eta} anni.")          #Stampa una descrizione generale del membro della squadra

    def __str__(self):
        return f"{self.nome} ({self.eta} anni)"


class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo                        # es., attaccante, difensore
        self.numero_maglia = numero_maglia              

    def gioca_partita(self):            #Azioni specifiche del giocatore
        
        print(f"Il giocatore {self.nome} (n. {self.numero_maglia}), nel ruolo di {self.ruolo}, scende in campo per giocare la partita.")


class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_esperienza):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza  

    def dirige_allenamento(self):           #Dettagli su come l'allenatore conduce gli allenamenti
        
        print(f"L'allenatore {self.nome} dirige la sessione di allenamento forte di {self.anni_di_esperienza} anni di esperienza.")


class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specializzazione):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione  # es., fisioterapista, analista di gioco[cite: 3]

    def supporta_team(self):            #Varie forme di supporto al team
        
        print(f"L'assistente {self.nome}, specializzato come {self.specializzazione}, fornisce supporto tecnico e medico alla squadra.")


class Squadra:
    def __init__(self, nome_squadra):
        self.nome_squadra = nome_squadra  
        self.membri = []

    def aggiungi_membro(self, membro):
        self.membri.append(membro)

    def __str__(self):
        return f"Squadra: {self.nome_squadra} (Membri totali: {len(self.membri)})"

    def gioca_contro(self, altra_squadra):          #Fà giocare la squadra contro un'altra
       
        print(f"\n--- PARTITA: {self.nome_squadra} vs {altra_squadra.nome_squadra} ---")
        print(f"Fischio d'inizio! La squadra {self.nome_squadra} affronta in un match entusiasmante la squadra {altra_squadra.nome_squadra}.")


# Creazione della Squadra 1 e dei suoi membri
squadra_1 = Squadra("Leoni FC")
squadra_1.aggiungi_membro(Allenatore("Roberto", 52, 15))
squadra_1.aggiungi_membro(Giocatore("Marco", 24, "attaccante", 9))
squadra_1.aggiungi_membro(Assistente("Davide", 38, "fisioterapista"))

# Creazione della Squadra 2 e dei suoi membri
squadra_2 = Squadra("Tigri United")
squadra_2.aggiungi_membro(Allenatore("Stefano", 60, 22))
squadra_2.aggiungi_membro(Giocatore("Alessandro", 27, "difensore", 5))
squadra_2.aggiungi_membro(Assistente("Matteo", 31, "analista di gioco"))

# Test dei metodi e delle descrizioni
print(squadra_1)
for membro in squadra_1.membri:
    membro.descrivi()
    if isinstance(membro, Giocatore):
        membro.gioca_partita()
    elif isinstance(membro, Allenatore):
        membro.dirige_allenamento()
    elif isinstance(membro, Assistente):
        membro.supporta_team()

print("\n" + "-"*40 + "\n")

print(squadra_2)
for membro in squadra_2.membri:
    membro.descrivi()
    if isinstance(membro, Giocatore):
        membro.gioca_partita()
    elif isinstance(membro, Allenatore):
        membro.dirige_allenamento()
    elif isinstance(membro, Assistente):
        membro.supporta_team()

# Fai giocare le due squadre contro
squadra_1.gioca_contro(squadra_2)