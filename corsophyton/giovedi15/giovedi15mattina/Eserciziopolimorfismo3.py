
# 1. CLASSE BASE: Prodotto (Incapsulamento)

class Prodotto:            # Classe base che rappresenta un prodotto generico della fabbrica. Raggruppa gli attributi comuni a tutti i prodotti (nome, quantità, costo unitario).

    def __init__(self, nome, quantita, costo_unitario):
        self.nome = nome                  # Nome del prodotto (stringa)
        self.quantita = quantita          # Quantità prodotta (intero)
        self.costo_unitario = costo_unitario        # Costo di produzione unitario (float)

    def stampa_dettagli(self):          #Metodo base che verrà sovrascritto (override) dalle classi figlie (Polimorfismo).
        
        return f"Prodotto: {self.nome} | Quantità: {self.quantita} | Costo unitario: {self.costo_unitario} €"


# 2. CLASSI DERIVATE (Ereditarietà e Polimorfismo)

class ProdottoStandard(Prodotto):           #Classe derivata per i prodotti standard prodotti in serie. Eredita da Prodotto e mantiene una visualizzazione standard.
    
    def __init__(self, nome, quantita, costo_unitario):
        super().__init__(nome, quantita, costo_unitario)

    def stampa_dettagli(self):          #Override del metodo: aggiunge l'etichetta [STANDARD].
        
        info_base = super().stampa_dettagli()
        return f"[STANDARD] {info_base}"


class ProdottoPersonalizzato(Prodotto): # Classe derivata per i prodotti realizzati su misura per un cliente.  Aggiunge l'attributo specifico 'codice_cliente'.
   
    def __init__(self, nome, quantita, costo_unitario, codice_cliente):
        super().__init__(nome, quantita, costo_unitario)
        self.codice_cliente = codice_cliente  # Attributo extra specifico

    def stampa_dettagli(self):          #Override del metodo: include il codice cliente nella visualizzazione (Polimorfismo).
        info_base = super().stampa_dettagli()
        return f"[PERSONALIZZATO - Cliente: {self.codice_cliente}] {info_base}"


# 3. CLASSE GESTIONE FABBRICA

class Fabbrica:      # Gestisce l'insieme dei prodotti registrati durante la giornata e implementa tutte le operazioni del menu richiesto.
    def __init__(self):     # Dizionario per memorizzare i prodotti in base al nome
        
        self.prodotti = {}

    def aggiungi_prodotto(self, prodotto):          #Aggiunge un oggetto Prodotto (Standard o Personalizzato) al dizionario.
       
        nome = prodotto.nome
        if nome in self.prodotti:
            self.prodotti[nome].quantita += prodotto.quantita
            print(f"Il prodotto '{nome}' esiste già. Quantità incrementata.")
        else:
            self.prodotti[nome] = prodotto
            print(f"Prodotto '{nome}' aggiunto con successo.")

    def visualizza_produzione(self):            #Mostra l'elenco completo sfruttando il polimorfismo sul metodo stampa_dettagli().
        
        if not self.prodotti:
            print("\nNessun prodotto registrato nella produzione odierna.")
        else:
            print("\n--- ELENCO PRODUZIONE ODIERNA ---")
            for prodotto in self.prodotti.values():
                # Polimorfismo in azione: Python chiama il metodo corretto a seconda che l'oggetto sia Standard o Personalizzato
                print(prodotto.stampa_dettagli())
            print("-" * 33)

    def cerca_prodotto(self, nome):         #Cerca un prodotto specifico tramite il suo nome.
        if nome in self.prodotti:
            print(f"Trovato! -> {self.prodotti[nome].stampa_dettagli()}")
        else:
            print(f"Il prodotto '{nome}' non è presente nella produzione.")

    def modifica_quantita(self, nome, nuova_quantita):          #Modifica la quantità di un prodotto esistente.
        if nome in self.prodotti:
            self.prodotti[nome].quantita = nuova_quantita
            print(f"Quantità del prodotto '{nome}' aggiornata a {nuova_quantita}.")
        else:
            print(f"Errore: Il prodotto '{nome}' non esiste.")

    def rimuovi_prodotto(self, nome):           #Rimuove un prodotto dalla lista della produzione.
        if nome in self.prodotti:
            del self.prodotti[nome]
            print(f"Prodotto '{nome}' rimosso con successo.")
        else:
            print(f"Errore: Il prodotto '{nome}' non è stato trovato.")

    def calcola_totale(self):           #Calcola e stampa la somma di tutti i pezzi prodotti.
        totale_pezzi = sum(p.quantita for p in self.prodotti.values())
        print(f"\nTotale complessivo dei pezzi prodotti oggi: {totale_pezzi}")


# 4. PROGRAMMA PRINCIPALE (Menu Continuo)

def avvia_sistema():
    fabbrica = Fabbrica()

    while True:
        print("\n=== MENU GESTIONE PRODUZIONE FABBRICA ===")
        print("1 - Aggiungi prodotto")
        print("2 - Visualizza produzione")
        print("3 - Cerca prodotto")
        print("4 - Modifica quantità")
        print("5 - Rimuovi prodotto")
        print("6 - Calcola totale pezzi prodotti")
        print("7 - Esci")
        
        scelta = input("Scegli un'opzione (1-7): ").strip()

        if scelta == '1':
            nome = input("Inserisci il nome del prodotto: ").strip()
            tipo = input("Il prodotto è personalizzato? (s/n): ").strip().lower()
            try:
                quantita = int(input("Inserisci la quantità prodotta: "))
                costo = float(input("Inserisci il costo unitario (€): "))
                
                if tipo == 's':
                    cliente = input("Inserisci il codice o nome del cliente: ").strip()
                    
                    nuovo_p = ProdottoPersonalizzato(nome, quantita, costo, cliente)            # Creazione di un'istanza della classe derivata ProdottoPersonalizzato
                else:
                    
                    nuovo_p = ProdottoStandard(nome, quantita, costo)           # Creazione di un'istanza della classe derivata ProdottoStandard
                
                fabbrica.aggiungi_prodotto(nuovo_p)
            except ValueError:
                print("Errore: Inserisci valori numerici validi per quantità e costo.")

        elif scelta == '2':
            fabbrica.visualizza_produzione()

        elif scelta == '3':
            nome = input("Inserisci il nome del prodotto da cercare: ").strip()
            fabbrica.cerca_prodotto(nome)

        elif scelta == '4':
            nome = input("Inserisci il nome del prodotto da modificare: ").strip()
            try:
                nuova_quantita = int(input("Inserisci la nuova quantità: "))
                if nuova_quantita >= 0:
                    fabbrica.modifica_quantita(nome, nuova_quantita)
                else:
                    print("Errore: La quantità non può essere negativa.")
            except ValueError:
                print("Errore: Inserisci un numero intero valido.")

        elif scelta == '5':
            nome = input("Inserisci il nome del prodotto da rimuovere: ").strip()
            fabbrica.rimuovi_prodotto(nome)

        elif scelta == '6':
            fabbrica.calcola_totale()

        elif scelta == '7':
            print("Chiusura del programma. Arrivederci!")
            break
        else:
            print("Opzione non valida. Scegli un numero compreso tra 1 e 7.")

if __name__ == "__main__":
    avvia_sistema()