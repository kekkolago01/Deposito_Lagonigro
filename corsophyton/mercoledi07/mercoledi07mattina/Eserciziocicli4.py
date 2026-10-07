#4

ripeti = "si"

while ripeti == "si":

    numero = int(input("Inserisci qui un numero! "))

    for numero1 in range(numero, -1, -1):

        print(numero1)

    ripeti = input("Vuoi continuare? ")