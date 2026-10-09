#14

# Variabili globali per memorizzare le credenziali dell'utente
nome_registrato = ""                                  # Salva il nome inserito in registrazione
codice_registrato = ""                                # Salva il codice inserito in registrazione
dati_registrati = False                               # Indica se l'utente si è già registrato (True/False)

# Lista per memorizzare i risultati delle operazioni effettuate
lista_risultati = []                                  # Lista vuota dove salveremo i risultati dei calcoli

# Variabile per controllare il primo ciclo while (Menu Principale)
sistema_attivo = True                                 # Mantiene attivo il programma generale

while sistema_attivo:
    print("\n=== MENU PRINCIPALE ===")                  # Stampa a schermo il titolo del menu
    print("1. Registrazione")                          # Opzione per registrarsi
    print("2. Login")                                  # Opzione per accedere
    print("3. Esci dal programma")                     # Opzione per chiudere lo script

    scelta_principale = input("Scegli un'opzione (1-3): ") # Chiede l'input all'utente

    match scelta_principale:

        case "1":
            # OPERAZIONE: REGISTRAZIONE OBBLIGATORIA
            print("\n--- REGISTRAZIONE UTENTE ---")
            
            # Ciclo while per l'inserimento del nome non vuoto
            nome_input = ""                           # Variabile di supporto per il controllo
            while nome_input == "":                   # Continua a chiedere finché l'utente lascia vuoto
                nome_input = input("Inserisci il tuo nome: ")
                if nome_input == "":                  # Controllo con if per segnalare l'errore
                    print("Il nome non può essere vuoto!")

            # Ciclo while per l'inserimento del codice non vuoto
            codice_input = ""                         # Variabile di supporto per il controllo
            while codice_input == "":                 # Continua a chiedere finché il codice è vuoto
                codice_input = input("Inserisci il tuo codice: ")
                if codice_input == "":                # Controllo con if se il codice è vuoto
                    print("Il codice non può essere vuoto!")

            # Salviamo i dati presi in input nelle variabili principali
            nome_registrato = nome_input              # Salva il nome valido
            codice_registrato = codice_input          # Salva il codice valido
            dati_registrati = True                    # Cambiamo lo stato a True per confermare la registrazione
            print("Registrazione completata con successo!")

        case "2":
            # OPERAZIONE: LOGIN
            print("\n--- LOGIN UTENTE ---")

            # Verifichiamo prima se l'utente si è registrato
            if dati_registrati == False:              # Se dati_registrati è ancora False
                print("Errore: Devi prima registrarti per poter accedere!")
            else:
                # Chiediamo le credenziali di accesso
                nome_login = input("Inserisci il tuo nome: ")
                codice_login = input("Inserisci il tuo codice: ")

                # Verifichiamo se nome == nome e codice == codice
                if nome_login == nome_registrato and codice_login == codice_registrato:
                    print("\nLogin effettuato! Benvenuto/a", nome_registrato) # Usiamo la virgola al posto della f-string
                    
                    # Variabile per il secondo ciclo while (Menu Operazioni)
                    utente_loggato = True             # Mantiene l'utente dentro il menu di login

                    while utente_loggato:
                        print("\n=== MENU OPERAZIONI ===") # Menu secondario di secondo livello
                        print("1. Calcola Somma")      # Opzione per la somma
                        print("2. Calcola Sottrazione") # Opzione per la sottrazione
                        print("3. Visualizza Risultati Salvati") # Opzione per vedere i risultati
                        print("4. Logout (Torna al menu principale)") # Opzione per uscire dal login

                        scelta_operazione = input("Scegli un'opzione (1-4): ") # Input per il secondo menu

                        match scelta_operazione:

                            case "1":
                                # SOMMA TRA DUE NUMERI
                                num1 = float(input("Inserisci il primo numero: ")) # Converte il testo in float
                                num2 = float(input("Inserisci il secondo numero: ")) # Converte il testo in float
                                somma = num1 + num2   # Calcola la somma
                                lista_risultati.append(somma) # Aggiunge il risultato in fondo alla lista
                                print("Risultato Somma:", somma, "(Salvato in memoria)") # Usiamo la virgola per stampare

                            case "2":
                                # SOTTRAZIONE TRA DUE NUMERI
                                num1 = float(input("Inserisci il primo numero: ")) # Converte in float
                                num2 = float(input("Inserisci il secondo numero: ")) # Converte in float
                                sottrazione = num1 - num2 # Calcola la sottrazione
                                lista_risultati.append(sottrazione) # Aggiunge il risultato alla lista
                                print("Risultato Sottrazione:", sottrazione, "(Salvato in memoria)") # Usiamo la virgola

                            case "3":
                                # VISUALIZZA RISULTATI SALVATI
                                print("\n--- RISULTATI MEMORIZZATI ---")
                                if len(lista_risultati) == 0: # Controlliamo se la lista è vuota con len()
                                    print("Nessun risultato ancora salvato.")
                                else:
                                    # Ciclo for per mostrare tutti i risultati presenti nella lista
                                    for i in range(len(lista_risultati)): # Iteriamo sugli indici della lista
                                        print("Operazione", i + 1, ":", lista_risultati[i]) # Stampa ogni elemento con virgole

                            case "4":
                                # LOGOUT
                                print("Logout effettuato. Torno al menu principale.")
                                utente_loggato = False # Imposta a False per chiudere il menu di login

                            case _:
                                print("Opzione non valida! Scegli un numero da 1 a 4.")

                else:
                    # Se il nome o il codice inseriti nel login non coincidono
                    print("Credenziali errate! Nome o Codice non corrispondono.")

        case "3":
            # CHIUSURA DEL PROGRAMMA
            print("Chiusura del programma in corso. Arrivederci!")
            sistema_attivo = False                    # Imposta a False per arrestare il primo ciclo while

        case _:
            print("Opzione non valida! Scegli un numero da 1 a 3.")