
class Automobile:  # Dichiaro una classe
    numero_di_ruote = 4  # Attributo di classe

    def __init__(self, marca, modello):  # Metodo costruttore
        self.marca = marca  # Attributo di istanza
        self.modello = modello  # Attributo di istanza

    def stampa_info(self):  # Metodo di istanza
        print("L'automobile è una", self.marca, self.modello)


# Creazione degli oggetti
auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

# Chiamata dei metodi
auto1.stampa_info()
auto2.stampa_info()
