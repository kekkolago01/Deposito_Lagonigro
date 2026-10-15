# ==========================================
# 1. CLASSE BASE Persona (Incapsulamento)
# ==========================================
class Persona:
    
    #Classe base che rappresenta una persona generica. Implementa l'incapsulamento rendendo privati gli attributi nome ed età (__),accessibili e modificabili unicamente tramite appositi metodi getter e setter.
    
    
    def __init__(self, nome, eta):          # Inizializziamo gli attributi privati richiamando i setter per validare subito i dati passati
        
        self.__nome = ""
        self.set_nome(nome)
        
        self.__eta = 0
        self.set_eta(eta)

    # -----------------
    # Getter e Setter per il nome (Incapsulamento)
    # -----------------
    def get_nome(self):         #Metodo getter: restituisce in modo sicuro il nome della persona.
        
        return self.__nome

    def set_nome(self, nome):           #Metodo setter con validazione: controlla che il nome sia una stringa non vuota.
        
        if isinstance(nome, str) and nome.strip():
            self.__nome = nome.strip()
        else:
            print("Errore: Il nome deve essere una stringa valida e non vuota.")

    # -----------------
    # Getter e Setter per l'età (Incapsulamento)
    # -----------------
    def get_eta(self):          #Metodo getter: restituisce in modo sicuro l'età della persona.
        
        return self.__eta

    def set_eta(self, eta):         #Metodo setter con validazione: controlla che l'età sia un numero intero non negativo.
        
        if isinstance(eta, int) and eta >= 0:
            self.__eta = eta
        else:
            print("Errore: L'età deve essere un numero intero non negativo.")

    # Metodo di presentazione generico della classe base
    def presentazione(self):            #Stampa una frase introduttiva con il nome e l'età della persona.
        
        print(f"Ciao, mi chiamo {self.__nome} e ho {self.__eta} anni.")


# ==========================================
# 2. CLASSE STUDENTE (Ereditarietà e Polimorfismo)
# ==========================================
class Studente(Persona):                # Classe Studente che eredita da Persona (Ereditarietà).Aggiunge l'attributo specifico dei voti e sovrascrive il metodo presentazione (Polimorfismo).

    def __init__(self, nome, eta, voti):
        
        super().__init__(nome, eta)         # super() richiama il costruttore della classe genitore (Persona) per inizializzare nome ed età
        self.voti = voti            # Lista di interi che rappresentano i voti dello studente

    def calcola_media(self):            #Calcola e restituisce la media aritmetica dei voti dello studente.
        
        if len(self.voti) == 0:
            return 0.0
        return sum(self.voti) / len(self.voti)

    # Override del metodo presentazione: Polimorfismo (stesso nome del metodo, comportamento specifico)
    def presentazione(self):            #Stampa la presentazione dello studente includendo la media dei voti.
        
        media = self.calcola_media()
        # Sfruttiamo i metodi getter ereditati (get_nome e get_eta) per leggere i campi privati
        print(f"Ciao, sono lo studente {self.get_nome()}, ho {self.get_eta()} anni e la mia media voti è {media:.2f}.")


# ==========================================
# 3. CLASSE PROFESSORE (Ereditarietà e Polimorfismo)
# ==========================================
class Professore(Persona):              #Classe Professore che eredita da Persona (Ereditarietà). Aggiunge l'attributo della materia e adatta il metodo presentazione (Polimorfismo).
        
    def __init__(self, nome, eta, materia):         # Richiamo del costruttore del genitore per riutilizzare la logica di base
        
        super().__init__(nome, eta)
        self.materia = materia              # Stringa che rappresenta la materia insegnata

    # Override del metodo presentazione: Polimorfismo
    def presentazione(self):
        """Stampa la presentazione del professore includendo la materia insegnata."""
        print(f"Buongiorno, sono il professore {self.get_nome()}, ho {self.get_eta()} anni e insegno {self.materia}.")


# ==========================================
# ESEMPIO DI UTILIZZO E TEST DEL SISTEMA
# ==========================================


persona_generica = Persona("Giovanni", 40)          # Creazione di un'istanza della classe base Persona


studente_1 = Studente("Alice", 17, [8, 7, 9, 6, 10])            # Creazione di un'istanza della classe derivata Studente


professore_1 = Professore("Marco Rossi", 45, "Matematica")          # Creazione di un'istanza della classe derivata Professore

# Test del Polimorfismo: chiamiamo lo stesso metodo 'presentazione()' su oggetti di classi diverse
print("--- TEST DEL POLIMORFISMO ---")
persona_generica.presentazione()  # Esegue il metodo di Persona
studente_1.presentazione()        # Esegue la versione sovrascritta di Studente
professore_1.presentazione()      # Esegue la versione sovrascritta di Professore

# Test dell'Incapsulamento e dei Getter/Setter
print("\n--- TEST DELL'INCAPSULAMENTO ---")
print(f"Nome attuale (tramite getter): {studente_1.get_nome()}")

# Tentativo di modifica tramite setter con validazione corretta
studente_1.set_nome("Alice Bianchi")
print(f"Nome modificato (tramite setter): {studente_1.get_nome()}")

# Test di validazione dell'età (il valore negativo genererà un errore controllato)
print("Tentativo di inserire un'età non valida:")
studente_1.set_eta(-5)