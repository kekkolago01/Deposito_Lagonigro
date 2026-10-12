
class Francesco:
    nome = "francesco"

    # Metodo di classe (metodo dell'oggetto)
    def saluta(self):
        return "ciao mirko"


# Inizializzazione degli oggetti tramite la classe
ogg_1 = Francesco()
ogg_2 = Francesco()

ogg_2.nome = "carola"

print(ogg_1.nome)
print(ogg_2.nome)

print(ogg_1.saluta())
