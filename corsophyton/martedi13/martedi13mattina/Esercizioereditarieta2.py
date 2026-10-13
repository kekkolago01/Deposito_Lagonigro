class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome            # stringa che descrive il nome del prodotto
        self.costo_produzione = costo_produzione            # costo per produrre il prodotto
        self.prezzo_vendita = prezzo_vendita            # prezzo a cui il prodotto viene venduto al pubblico
        
    def calcola_profitto(self):
        
        return self.prezzo_vendita - self.costo_produzione          #Restituisce la differenza tra il prezzo di vendita e il costo di produzione


class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia            # attributo specifico per Elettronica (es. mesi di garanzia)


class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale              # attributo specifico per Abbigliamento (es. tipo di tessuto)


class Fabbrica:
    def __init__(self):
                    # un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino
        self.inventario = {}

    def aggiungi_prodotto(self, prodotto, quantita=1):          #Aggiunge prodotti all'inventario
        
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
        print(f"Aggiunti {quantita} pezzi di '{prodotto.nome}' all'inventario.")

    def vendi_prodotto(self, prodotto, quantita=1):         #Diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita
        
        if prodotto in self.inventario and self.inventario[prodotto] >= quantita:
            self.inventario[prodotto] -= quantita
            profitto_unitario = prodotto.calcola_profitto()
            profitto_totale = profitto_unitario * quantita
            print(f"Venduti {quantita} pezzi di '{prodotto.nome}'. Profitto realizzato: {profitto_totale} €")
        else:
            print(f"Errore: Quantità insufficiente o prodotto '{prodotto.nome}' non disponibile in inventario.")

    def resi_prodotto(self, prodotto, quantita=1):                  #Aumenta la quantità di un prodotto restituito in inventario

        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
        print(f"Reso registrato: {quantita} pezzi di '{prodotto.nome}' rientrati in inventario.")


# Esempio di utilizzo del sistema:
# Creazione dei prodotti (classi parallele)

smartphone = Elettronica("Smartphone X", 250.0, 500.0, "24 mesi")
giacca = Abbigliamento("Giacca Invernale", 30.0, 90.0, "Lana")


mia_fabbrica = Fabbrica()           # Inizializzazione della fabbrica


mia_fabbrica.aggiungi_prodotto(smartphone, 10)          # Aggiunta prodotti in magazzino
mia_fabbrica.aggiungi_prodotto(giacca, 25)


mia_fabbrica.vendi_prodotto(smartphone, 2)          # Vendita di prodotti
mia_fabbrica.vendi_prodotto(giacca, 5)


mia_fabbrica.resi_prodotto(smartphone, 1)           # Gestione dei resi