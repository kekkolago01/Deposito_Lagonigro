class Contatore:

    numero_istanze = 0  # Attributo di classe


    def __init__(self):

        Contatore.numero_istanze += 1


    @classmethod

    def mostra_numero_istanze(cls):

        print("Sono state create”, cls.numero_istanze, “ istanze.")


# Creazione di alcune istanze

c1 = Contatore()

c2 = Contatore()


Contatore.mostra_numero_istanze()  

# Output: Sono state create 2 istanze.