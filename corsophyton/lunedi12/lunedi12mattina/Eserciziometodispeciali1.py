class Garage:
    def __init__(self, capienza):
        self.capienza = capienza
        self.auto_presenti = []
        
    def formato_targa_valido(self, targa):          #Verifica se la targa ha una lunghezza valida di esattamente 7 caratteri.
      
        return len(targa) == 7

    def posti_liberi(self):         #Restituisce il numero di posti ancora disponibili.
       
        return self.capienza - len(self.auto_presenti)

    def parcheggia(self, targa):             #Aggiunge un'auto al garage se c'è posto, la targa è valida e non è già presente.
       
        if not self.formato_targa_valido(targa):
            print(f"Errore: La targa '{targa}' non è valida (deve essere di 7 caratteri).")
            return
            
        if targa in self.auto_presenti:
            print(f"Avviso: L'auto con targa '{targa}' è già presente in garage.")
            return
            
        if self.posti_liberi() <= 0:
            print("Errore: Il garage è pieno! Impossibile parcheggiare.")
            return
            
        self.auto_presenti.append(targa)
        print(f"Auto con targa '{targa}' parcheggiata con successo.")

    def rimuovi(self, targa):                   #Rimuove l'auto corrispondente dalla lista se presente.

        if targa in self.auto_presenti:
            self.auto_presenti.remove(targa)
            print(f"Auto con targa '{targa}' rimossa dal garage.")
        else:
            print(f"Errore: L'auto con targa '{targa}' non è presente nel garage.")

# Esempio di utilizzo:
mio_garage = Garage(2)

mio_garage.parcheggia("AB123CD")  # Valida (7 caratteri)
mio_garage.parcheggia("XYZ")      # Rifiutata (troppo corta)
mio_garage.parcheggia("EF456GH")  # Valida (7 caratteri)
mio_garage.parcheggia("XY789ZW")  # Rifiutata (garage pieno)

print("Posti liberi:", mio_garage.posti_liberi())  # Stampa: 0