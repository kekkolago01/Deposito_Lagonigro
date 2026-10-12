class Punto:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def muovi(self, dx, dy):
        
        self.x += dx            #Modifica le coordinate del punto aggiungendo dx e dy.
        self.y += dy
        
    def distanza_da_origine(self):
        return (self.x**2 + self.y**2) ** 0.5                   #Restituisce la distanza del punto dall'origine (0, 0).

    
    def __str__(self):
        return f"Punto({self.x}, {self.y})"

# Esempio di utilizzo:
p = Punto(3, 4)
print(p)  # Stampa: Punto(3, 4)

print("Distanza dall'origine:", p.distanza_da_origine())        # Stampa: 5.0

p.muovi(1, -1)
print("Dopo il movimento:", p)              # Stampa: Punto(4, 3)
print("Nuova distanza dall'origine:", p.distanza_da_origine())              # Stampa: 5.0