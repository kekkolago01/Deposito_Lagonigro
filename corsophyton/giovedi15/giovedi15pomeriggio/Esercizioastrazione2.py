from abc import ABC, abstractmethod

# 1. CLASSE ASTRATTA: VeicoloTrasporto

class VeicoloTrasporto(ABC):
    
   # Classe astratta base che rappresenta un veicolo generico per il trasporto merci.
   #Usa il modulo 'abc' per impedire l'istanziazione diretta e definisce attributi e metodi comuni condivisi da tutte le sottoclassi.
    
    def __init__(self, targa, peso_massimo):
        # Attributi protetti per memorizzare le informazioni di base
        self._targa = targa                    # Targa identificativa del veicolo (stringa)
        self._peso_massimo = peso_massimo      # Capacità massima di carico in kg (intero)
        self._carico_attuale = 0               # Carico attuale impostato inizialmente a 0 (intero)

    # Metodi Getter (Incapsulamento)
    
    def get_targa(self):
        #Restituisce la targa del veicolo in modo sicuro.
        return self._targa

    def get_peso_massimo(self):
        #Restituisce il peso massimo trasportabile.
        return self._peso_massimo

    def get_carico_attuale(self):
       #Restituisce il carico attualmente caricato.
        return self._carico_attuale


    # Metodi Concreti Comuni
    def carica(self, peso):
       # Aumenta il carico attuale se rientra nella capacità massima consentita.
        if peso <= 0:
            print("Errore: Il peso da caricare deve essere maggiore di zero.")
            return False
            
        
        if (self._carico_attuale + peso) <= self._peso_massimo:         # Verifica se il nuovo carico supera la capacità massima del veicolo
            self._carico_attuale += peso
            print(f"Caricati {peso} kg sul veicolo {self._targa}. Carico totale attuale: {self._carico_attuale} kg.")
            return True
        else:
            print(f"Errore: Impossibile caricare {peso} kg su {self._targa}. Il peso supera la capacità massima ({self._peso_massimo} kg).")
            return False

    def scarica(self):
       #Riporta a zero il carico attuale del veicolo.
        carico_precedente = self._carico_attuale
        self._carico_attuale = 0
        print(f"Veicolo {self._targa} scaricato. Rimossi {carico_precedente} kg.")

   
    # Metodo Astratto
    
    @abstractmethod                 #Metodo astratto: obbliga ogni sottoclasse concreta a definire la propria regola specifica per il calcolo del costo di manutenzione.

    def costo_manutenzione(self):
        
        pass



# 2. CLASSI DERIVATE (Sottoclassi Concrete)


class Camion(VeicoloTrasporto):
    
   # Rappresenta un camion per il trasporto pesante.
    # Aggiunge l'attributo relativo al numero di assi.
    
    def __init__(self, targa, peso_massimo, numero_assi):
        super().__init__(targa, peso_massimo)
        self.numero_assi = numero_assi  # Numero di assi del camion (intero)

    def costo_manutenzione(self):
        #Regola manutenzione Camion: 100 € per asse + 1 € per kg di carico massimo.
        costo = (self.numero_assi * 100) + (self._peso_massimo * 1)
        return costo


class Furgone(VeicoloTrasporto):
    
# Rappresenta un furgone per le consegne.
#Aggiunge l'attributo relativo al tipo di alimentazione (es. 'elettrico', 'diesel').
    def __init__(self, targa, peso_massimo, alimentazione):
        super().__init__(targa, peso_massimo)
        self.alimentazione = alimentazione.lower()  # Tipo di alimentazione (stringa)

    def costo_manutenzione(self):
       # Regola manutenzione Furgone: 200 € se elettrico, 150 € se diesel.
        if self.alimentazione == "elettrico":
            return 200.0
        elif self.alimentazione == "diesel":
            return 150.0
        else:
            return 100.0  # Valore di default per altre alimentazioni


class Motocarro(VeicoloTrasporto):

    #Rappresenta un motocarro per piccoli trasporti locali.
    #Aggiunge l'attributo relativo agli anni di servizio.
    
    def __init__(self, targa, peso_massimo, anni_servizio):
        super().__init__(targa, peso_massimo)
        self.anni_servizio = anni_servizio  # Anni di servizio del veicolo (intero)

    def costo_manutenzione(self):
        """Regola manutenzione Motocarro: 50 € per ogni anno di servizio."""
        return self.anni_servizio * 50.0


# 3. CLASSE DI GESTIONE: GestoreFlotta
class GestoreFlotta:

    #Gestisce un elenco (flotta) di veicoli di vario tipo e coordina le operazioni di aggiunta, rimozione e calcolo dei costi.

    def __init__(self):
        self.veicoli = []  # Lista che conterrà oggetti derivati da VeicoloTrasporto

    def aggiungi_veicolo(self, veicolo):
        #Aggiunge un nuovo veicolo alla flotta aziendale.
        self.veicoli.append(veicolo)
        print(f"Veicolo con targa {veicolo.get_targa()} aggiunto alla flotta.")

    def rimuovi_veicolo(self, targa):           #Rimuove un veicolo dalla flotta cercandolo tramite la targa.
        
        for veicolo in self.veicoli:
            if veicolo.get_targa() == targa:
                self.veicoli.remove(veicolo)
                print(f"Veicolo con targa {targa} rimosso dalla flotta.")
                return True
        print(f"Errore: Nessun veicolo trovato con targa {targa}.")
        return False

    def costo_totale_manutenzione(self):

        #Calcola la somma dei costi di manutenzione di tutti i veicoli sfruttando il Polimorfismo sugli oggetti astratti.

        totale = 0.0
        for veicolo in self.veicoli:
            # Polimorfismo: Python richiama automaticamente il metodo 'costo_manutenzione()' 
            # specifico della classe corrispondente (Camion, Furgone o Motocarro)
            totale += veicolo.costo_manutenzione()
        return totale

    def stampa_veicoli(self):                   #Elenca targa, tipo di veicolo e carico attuale di ciascun mezzo.

        print("\n--- ELENCO VEICOLI DELLA FLOTTA ---")
        if not self.veicoli:
            print("Nessun veicolo presente nella flotta.")
        else:
            for veicolo in self.veicoli:
                tipo_veicolo = type(veicolo).__name__
                print(f"Targa: {veicolo.get_targa()} | Tipo: {tipo_veicolo} | Carico Attuale: {veicolo.get_carico_attuale()} / {veicolo.get_peso_massimo()} kg")
        print("-" * 38)


# 4. ESEMPIO DI UTILIZZO E TEST DEL SISTEMA

# Creazione del gestore della flotta
flotta_aziendale = GestoreFlotta()

# Creazione dei diversi veicoli concreti
camion_1 = Camion("AB123CD", peso_massimo=10000, numero_assi=4)
furgone_1 = Furgone("EF456GH", peso_massimo=1500, alimentazione="elettrico")
motocarro_1 = Motocarro("LM789NO", peso_massimo=500, anni_servizio=3)

# Aggiunta dei veicoli alla flotta
flotta_aziendale.aggiungi_veicolo(camion_1)
flotta_aziendale.aggiungi_veicolo(furgone_1)
flotta_aziendale.aggiungi_veicolo(motocarro_1)

# Test dei metodi di carico e scarico
print("\n--- TEST OPERAZIONI DI CARICO ---")
camion_1.carica(4000)       # Caricamento valido
furgone_1.carica(1600)      # Fallirà perché supera il peso massimo (1500 kg)
furgone_1.carica(1000)      # Caricamento valido

# Stampa riassuntiva dei veicoli
flotta_aziendale.stampa_veicoli()

# Test del polimorfismo per il calcolo della manutenzione totale
costo_totale = flotta_aziendale.costo_totale_manutenzione()
print(f"\nCosto totale di manutenzione della flotta: {costo_totale:.2f} €")

# Test di rimozione di un veicolo
print("\n--- TEST RIMOZIONE VEICOLO ---")
flotta_aziendale.rimuovi_veicolo("LM789NO")
flotta_aziendale.stampa_veicoli()