class Libro:
    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
        
    def descrizione(self):
        return f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.pagine} pagine."                  #Restituisce una stringa descrittiva del libro.


Mio_libro = Libro("I Promessi Sposi", "Alessandro Manzoni", 550)            # Esempio di utilizzo:

print(Mio_libro.descrizione())