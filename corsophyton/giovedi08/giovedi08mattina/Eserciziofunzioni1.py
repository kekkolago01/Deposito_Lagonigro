#1

import random

def indovina_il_numero():
    numero_segreto = random.randint(1, 100)             # 1. Generiamo un numero casuale tra 1 e 100 usando la funzione random.randint

    
    print("Benvenuto al gioco di indovina il numero!")
    print("Ho pensato a un numero tra 1 e 100. Prova a indovinarlo, oppure scrivi 'esci'.")
    
    while True:             # 2. Usiamo un ciclo while per continuare a chiedere tentativi finché non si esce o si vince

        tentativo_utente = input("Inserisci il tuo tentativo o 'esci': ")                   # Chiediamo il tentativo all'utente (viene letto come stringa)

        
        match tentativo_utente:                 # 3. Controlliamo se l'utente vuole uscire con il match

            case "esci":
                print(f"Hai deciso di uscire. Il numero segreto era: {numero_segreto}")
                break
                
            case _:
                tentativo = int(tentativo_utente)                           # Visto che l'input è una stringa, se non è 'esci' lo convertiamo in intero

                
                if tentativo < numero_segreto:                          # 4. Confrontiamo il numero inserito con quello segreto usando i blocchi if/elif/else

                    print("Il numero da indovinare è più alto!")
                elif tentativo > numero_segreto:
                    print("Il numero da indovinare è più basso!")
                else:
                    print("Bravo! Hai indovinato il numero!")
                    break           # Usciamo dal ciclo while perché abbiamo vinto

indovina_il_numero()            # Chiamiamo la funzione per far partire il programma

