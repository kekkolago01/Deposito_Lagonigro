#condizione match

comando = input ("Inserisci un comando: ")
match comando:
    case "start":
        print ( "Invio del programma." )
    
    case "stop":
        print ("Chiusura del programma")    
        
    case "pausa":
        print ("pausa del programma")
        
    case _:
        
        print ("programma non riconosciuto." )
