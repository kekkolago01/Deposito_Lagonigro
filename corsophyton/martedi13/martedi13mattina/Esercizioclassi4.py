class Convertitore:
    @staticmethod
    def euro_in_dollari(euro):           #Converte un importo in euro in dollari (tasso fisso 1.08).
       
        return euro * 1.08

    @staticmethod
    def km_in_miglia(km):                   #Converte una distanza in chilometri in miglia (fattore fisso 0.621371).

        return km * 0.621371


risultato_dollari = Convertitore.euro_in_dollari(100)           # Test dei metodi chiamati direttamente dalla classe (senza creare oggetti)
print(f"100 € corrispondono a: {risultato_dollari} $")

risultato_miglia = Convertitore.km_in_miglia(50)
print(f"50 km corrispondono a: {risultato_miglia} miglia")