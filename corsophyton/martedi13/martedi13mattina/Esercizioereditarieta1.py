class Animale:
    def __init__(self, nome, eta):
        self.nome = nome            # stringa che descrive il nome dell'animale
        self.eta = eta              # intero che rappresenta l'età dell'animale
        
    def fai_suono(self):
        print(f"{self.nome} emette un suono generico.")                #Stampa un suono generico dell'animale



class Leone(Animale):
    def __init__(self, nome, eta, numero_branco):
        super().__init__(nome, eta)
        self.numero_branco = numero_branco
        
    def fai_suono(self):
        print(f"{self.nome} rugbisce ferocemente!")
        
    def caccia(self):           #Metodo specifico per il leone che descrive la caccia
        
        print(f"Il leone {self.nome} sta cacciando la sua preda nella savana con il branco numero {self.numero_branco}.")


class Giraffa(Animale):
    def __init__(self, nome, eta, altezza_metri):
        super().__init__(nome, eta)
        self.altezza_metri = altezza_metri
        
    def fai_suono(self):
        print(f"{self.nome} emette un verso silenzioso.")
        
    def bruca_foglie(self):          #Metodo specifico per la giraffa.
       
        print(f"La giraffa {self.nome} sta brucando le foglie dagli alberi più alti grazie al suo collo di {self.altezza_metri} metri.")


class Pinguino(Animale):
    def __init__(self, nome, eta,profondita_immersione):
        super().__init__(nome, eta)
        self.profondita_immersione = profondita_immersione
        
    def fai_suono(self):
        print(f"{self.nome} emette un verso gracchiante.")
        
    def nuota(self):                    #Metodo specifico per il pinguino.

        print(f"Il pinguino {self.nome} sta nuotando immergendosi fino a {self.profondita_immersione} metri di profondità.")


            # Esempio di utilizzo:
simba = Leone("Simba", 5, 3)
melman = Giraffa("Melman", 7, 5.2)
pingu = Pinguino("Pingu", 3, 20)

simba.fai_suono()
simba.caccia()

print("---")
melman.fai_suono()
melman.bruca_foglie()

print("---")
pingu.fai_suono()
pingu.nuota()