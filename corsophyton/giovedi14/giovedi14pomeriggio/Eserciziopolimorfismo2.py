# 1. CLASSE BASE: Posto (Incapsulamento)
class Posto:
    #Classe base che rappresenta un posto generico all'interno del teatro.
    #Gli attributi principali sono resi privati (__) per garantire la sicurezza dello stato.
    def __init__(self, numero, fila):
        self.__numero = numero                  # Attributo privato: numero identificativo del posto
        self.__fila = fila                      # Attributo privato: fila in cui si trova il posto
        self.__occupato = False                 # Attributo privato: stato iniziale libero (False)


    # Metodi Getter (Incapsulamento)
    def get_numero(self):           #Restituisce il numero del posto in modo sicuro.
        
        return self.__numero

    def get_fila(self):         #Restituisce la fila del posto in modo sicuro.
    
        
        return self.__fila

    def is_occupato(self):          #Restituisce True se il posto è occupato, False se è libero.
        
        return self.__occupato


    # Metodi Operativi
    def prenota(self):          #Prenota il posto se non è già occupato; altrimenti segnala l'errore.
        
        if not self.__occupato:
            self.__occupato = True
            print(f"Posto {self.__fila}{self.__numero} prenotato con successo.")
            return True
        else:
            print(f"Errore: Il posto {self.__fila}{self.__numero} è già occupato!")
            return False

    def libera(self):           #Libera il posto se è occupato; altrimenti segnala che era già libero.
        
        if self.__occupato:
            self.__occupato = False
            print(f"Posto {self.__fila}{self.__numero} liberato con successo.")
            return True
        else:
            print(f"Il posto {self.__fila}{self.__numero} non era prenotato.")
            return False


# 2. CLASSE DERIVATA: PostoVIP (Ereditarietà e Polimorfismo)



class PostoVIP(Posto):
    #Classe derivata PostoVIP che eredita da Posto.
    #Aggiunge servizi esclusivi e personalizza il comportamento della prenotazione.

    def __init__(self, numero, fila, servizi_extra):
        
        super().__init__(numero, fila)          # Richiama il costruttore del genitore per numero e fila
        self.servizi_extra = servizi_extra      # Lista di servizi extra (es. "Accesso al lounge")

    def prenota(self):          #Override del metodo prenota(): gestisce la prenotazione e attiva i servizi extra (Polimorfismo).
        
        # Sfruttiamo il controllo di prenotazione del genitore
        successo = super().prenota()
        if successo:
            print(f"Servizi extra attivati per il posto VIP {self.get_fila()}{self.get_numero()}: {', '.join(self.servizi_extra)}")
        return successo



# 3. CLASSE DERIVATA: PostoStandard (Ereditarietà e Polimorfismo)

class PostoStandard(Posto):

    #Classe derivata PostoStandard che eredita da Posto.
    #Aggiunge la gestione del costo e personalizza la stampa in fase di prenotazione.

    def __init__(self, numero, fila, costo):            # Richiama il costruttore della classe base
        
        super().__init__(numero, fila)
        self.costo = costo                      # Valore numerico che rappresenta il costo del biglietto

    def prenota(self):
        #Override del metodo prenota(): include la visualizzazione del costo (Polimorfismo).
        successo = super().prenota()
        if successo:
            print(f"Costo della prenotazione per il posto {self.get_fila()}{self.get_numero()}: {self.costo:.2f} €")
        return successo



# 4. CLASSE DI GESTIONE: Teatro

class Teatro:
    
    #Classe Teatro: gestisce una collezione (lista) di posti di vario tipo (VIP e Standard) e coordina le operazioni di prenotazione e visualizzazione.

    def __init__(self, nome_teatro):
        self.nome_teatro = nome_teatro
        self._posti = []                        # Lista protetta che conterrà tutti gli oggetti posto

    def aggiungi_posto(self, posto):            #Aggiunge un nuovo oggetto posto (sia VIP che Standard) alla lista del teatro.
        
        self._posti.append(posto)
        print(f"Aggiunto posto {posto.get_fila()}{posto.get_numero()} al teatro {self.nome_teatro}.")

    def prenota_posto(self, numero, fila):                 # Cerca il posto corrispondente nella lista e invoca il metodo prenota() (Polimorfismo).

        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
               
                return posto.prenota()
        
        print(f"Posto {fila}{numero} non trovato nel teatro.")
        return False

    def stampa_posti_occupati(self):
        
        print(f"\n--- ELENCO POSTI OCCUPATI ({self.nome_teatro}) ---")          #Scorre la lista e stampa tutti i posti che risultano attualmente occupati.
        trovati = False
        for posto in self._posti:
            if posto.is_occupato():
                print(f"-> Posto {posto.get_fila()}{posto.get_numero()} (Categoria: {type(posto).__name__})")
                trovati = True
        
        # CONTROLLO CORRETTO: se non è stato trovato alcun posto occupato, stampa il messaggio
        if not trovati:
            print("Nessun posto attualmente occupato.")
        print("-" * 40)



# 5. ESEMPIO DI UTILIZZO E TEST DEL SISTEMA

# Creazione del teatro
teatro_comunale = Teatro("Teatro Politeama")

# Creazione e aggiunta di vari posti (sia Standard che VIP)
teatro_comunale.aggiungi_posto(PostoStandard(1, "A", 15.00))
teatro_comunale.aggiungi_posto(PostoStandard(2, "A", 15.00))
teatro_comunale.aggiungi_posto(PostoVIP(1, "VIP", ["Accesso al lounge", "Servizio in posto", "Drink di benvenuto"]))
teatro_comunale.aggiungi_posto(PostoVIP(2, "VIP", ["Accesso al lounge", "Servizio in posto"]))

print("\n" + "="*40 + "\n")

# Test delle prenotazioni (Polimorfismo in azione)
teatro_comunale.prenota_posto(1, "A")       # Prenota un posto Standard (mostra il costo)
print()
teatro_comunale.prenota_posto(1, "VIP")     # Prenota un posto VIP (attiva i servizi extra)
print()

# Tentativo di riprenotare lo stesso posto VIP (dovrebbe segnalare errore)
teatro_comunale.prenota_posto(1, "VIP")

print("\n" + "="*40)

# Stampa l'elenco dei posti attualmente occupati
teatro_comunale.stampa_posti_occupati()