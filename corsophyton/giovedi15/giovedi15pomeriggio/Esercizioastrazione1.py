from abc import ABC, abstractmethod

# 1. CLASSE ASTRATTA: Impiegato
class Impiegato(ABC):           #Classe astratta base che rappresenta un impiegato generico dell'azienda. Usa il modulo 'abc' per impedire la creazione diretta di oggetti di questa classe e definisce un'interfaccia obbligatoria per le sottoclassi.
    def __init__(self, nome, cognome, stipendio_base):
        self.nome = nome                      # Nome dell'impiegato (stringa)
        self.cognome = cognome                # Cognome dell'impiegato (stringa)
        self.stipendio_base = stipendio_base  # Stipendio base fisso (valore numerico)

    @abstractmethod
    def calcola_stipendio(self):                   # Metodo astratto: obbliga tutte le classi derivate a implementare la propria logica specifica per il calcolo dello stipendio.

        pass


# 2. CLASSE DERIVATA: ImpiegatoFisso
class ImpiegatoFisso(Impiegato):                #Rappresenta un impiegato con stipendio fisso mensile. Eredita da Impiegato e non modifica lo stipendio base.

    def __init__(self, nome, cognome, stipendio_base):
        # Richiama il costruttore della classe genitore per inizializzare i dati comuni
        super().__init__(nome, cognome, stipendio_base)

    def calcola_stipendio(self):                    #Implementazione del metodo astratto: restituisce semplicemente lo stipendio base.

        return self.stipendio_base


# 3. CLASSE DERIVATA: ImpiegatoAProvvigione

class ImpiegatoAProvvigione(Impiegato):             #Rappresenta un impiegato che riceve lo stipendio base più un bonus calcolato in percentuale sulle vendite effettuate.

    def __init__(self, nome, cognome, stipendio_base, vendite_totali, percentuale_provvigione):
        super().__init__(nome, cognome, stipendio_base)
        self.vendite_totali = vendite_totali                      # Valore totale delle vendite
        self.percentuale_provvigione = percentuale_provvigione    # Percentuale di bonus (es. 0.10 per il 10%)

    def calcola_stipendio(self):                  # Implementazione del metodo astratto: calcola lo stipendio aggiungendo le provvigioni al salario base.

        bonus = self.vendite_totali * self.percentuale_provvigione
        return self.stipendio_base + bonus


# 4. FUNZIONE DI GESTIONE E STAMPA (Polimorfismo in azione)

def stampa_info_impiegati(lista_impiegati):            #Funzione che riceve una lista di impiegati di tipo diverso e sfrutta il polimorfismo chiamando 'calcola_stipendio()' senza preoccuparsi  della specifica classe a cui l'oggetto appartiene.

    print("\n--- REPORT STIPENDI IMPIEGATI ---")
    for imp in lista_impiegati:
        # Polimorfismo: Python esegue automaticamente la versione corretta di calcola_stipendio()
        stipendio_finale = imp.calcola_stipendio()
        print(f"Impiegato: {imp.nome} {imp.cognome} | Stipendio Totale: {stipendio_finale:.2f} €")
    print("-" * 35)


# 5. ESEMPIO DI UTILIZZO E TEST DEL SISTEMA

# Creazione di alcuni dipendenti con ruoli differenti
impiegato_1 = ImpiegatoFisso("Gino", "Filippi", 1500.00)
impiegato_2 = ImpiegatoAProvvigione("Kekko", "lago", 1200.00, vendite_totali=5000.00, percentuale_provvigione=0.15)
impiegato_3 = ImpiegatoFisso("Pino", "Silvestre", 1800.00)

# Raccolta degli oggetti in un'unica lista aziendale
personale_azienda = [impiegato_1, impiegato_2, impiegato_3]

# Esecuzione della funzione di stampa per verificare il funzionamento del sistema
stampa_info_impiegati(personale_azienda)