#5
numero1= float(input("Inserisci qui il primo numero "))
numero2= float(input("Inserisci qui il secondo numero "))
operazione=  input("Inserisci qui l'operazione da effettuare ( + , - , * , /)")

match operazione:
    case "+":
        risultato = numero1 + numero2
        print("risultato",risultato)
    
    case "-":
            risultato = numero1 - numero2
            print("risultato",risultato)
            
    case "*":
                risultato = numero1 * numero2
                print("risultato",risultato)
    
    case "/":
                if numero2 ==0:
                    print("Errore: Divisione per zero")
                else:
                    risultato = numero1 / numero2
                    print("Risultato:", risultato)
    
    case "_":
             print("Operazione non valida")
