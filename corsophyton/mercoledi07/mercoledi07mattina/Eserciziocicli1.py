#1

numero= int (input ("Inserisci un numero ")) # da x numero e fa il conto alla rovescia
for numero1 in range (numero , 0, -1) :
    print (numero1)
    
ripeti= input("Vuoi ripetere l'operazione? ")
ripeti = "si"

while ripeti == "si":

    numero = int(input("Inserisci un numero ")) # da x numero e fa il conto alla rovescia 
    for numero1 in range(numero, 0, -1): 
        print(numero1)

    ripeti = input("Vuoi ripetere l'operazione? ")
