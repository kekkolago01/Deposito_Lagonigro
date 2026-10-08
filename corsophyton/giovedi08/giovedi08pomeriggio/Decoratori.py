"""

def decoratore(funzione):

    def wrapper():

        print("Prima dell'esecuzione della funzione")

        funzione()

        print("Dopo l'esecuzione della funzione")

    return wrapper


@decoratore

def saluta():

    print("Ciao!")


saluta()



"""

