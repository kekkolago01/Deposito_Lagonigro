# esercizio 4

età = int(input("Digita la tua età, per capire se puoi vedere o meno il film: "))

maggiorenne = età >= 18

match maggiorenne:

    case True:
        print("Puoi vedere questo film")

    case False:
        print("Mi dispiace, non puoi vedere questo film")