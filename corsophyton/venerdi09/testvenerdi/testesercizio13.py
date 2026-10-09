# 13

# Creiamo 4 liste distinte, una per ogni tipo di dato
lista_interi = []     # Contiene i numeri interi (int)
lista_decimali = []   # Contiene i numeri con virgola (float)
lista_testi = []      # Contiene le stringhe di testo (str)
lista_booleani = []   # Contiene i valori True / False (bool)


# FUNZIONE PER STAMPARE TUTTE LE LISTE A SCHERMO
def mostra_tutte_le_liste():            # Usiamo print() per mostrare il contenuto di ciascuna lista

    print("\n--- STATO DELLE LISTE ---")
    print("1. Lista Interi:", lista_interi)
    print("2. Lista Decimali:", lista_decimali)
    print("3. Lista Testi:", lista_testi)
    print("4. Lista Booleani:", lista_booleani)
    print("-------------------------")


# CICLO PRINCIPALE PER RENDERE IL PROGRAMMA RIPETIBILE
programma_attivo = True         # Usiamo una variabile booleana come condizione del ciclo while

while programma_attivo:
    
    print("=== MENU OPERAZIONI ===")            # Stampa delle opzioni del menu
    print("1. Inserisci in fondo")
    print("2. Inserisci in una posizione specifica")
    print("3. Modifica un elemento")
    print("4. Elimina un elemento")
    print("5. Stampa tutte le liste")
    print("6. Esci")

    
    scelta_menu = input("Scegli un'opzione (1-6): ")            # Prendiamo l'input della scelta dell'utente dall'interfaccia a riga di comando

    
    match scelta_menu:          # Gestiamo la selezione con il costrutto match-case

        case "1":
            # OPERAZIONE: INSERIMENTO IN FONDO (.append)
            print("\nQuale lista vuoi aggiornare?")
            print("1. Interi | 2. Decimali | 3. Testi | 4. Booleani")
            scelta_tipo = input("Scegli il tipo (1-4): ")

            valore_inserito = input("Inserisci il valore da aggiungere: ")

            
            if scelta_tipo == "1":          # Verifichiamo la scelta del tipo con if-elif-else
                
                valore_convertito = int(valore_inserito)            # Convertiamo la stringa in numero intero
                lista_interi.append(valore_convertito)          # Aggiunge in coda
                print("Elemento inserito nella lista interi!")

            elif scelta_tipo == "2":
                            
                valore_convertito = float(valore_inserito)          # Convertiamo in floatx
                lista_decimali.append(valore_convertito)
                print("Elemento inserito nella lista decimali!")

            elif scelta_tipo == "3":
                
                lista_testi.append(valore_inserito)         # Resta una stringa (str)
                print("Elemento inserito nella lista testi!")

            elif scelta_tipo == "4":
                
                if valore_inserito.lower() == "true":           # Verifichiamo se l'utente ha scritto True
                    lista_booleani.append(True)
                else:
                    lista_booleani.append(False)
                print("Elemento inserito nella lista booleani!")

            else:
                print("Tipo selezionato non valido!")

        case "2":
            # OPERAZIONE: INSERIMENTO IN UNA POSIZIONE SPECIFICA (.insert)
            print("\nIn quale lista vuoi inserire?")
            print("1. Interi | 2. Decimali | 3. Testi | 4. Booleani")
            scelta_tipo = input("Scegli il tipo (1-4): ")

            valore_inserito = input("Inserisci il valore: ")
            
            posizione = int(input("Inserisci l'indice dove posizionarlo: "))            # Chiediamo l'indice di posizione e lo convertiamo in numero intero

            if scelta_tipo == "1":
                
                lista_interi.insert(posizione, int(valore_inserito))            # Usiamo il metodo .insert(indice, valore)
                print("Inserito con successo!")

            elif scelta_tipo == "2":
                lista_decimali.insert(posizione, float(valore_inserito))
                print("Inserito con successo!")

            elif scelta_tipo == "3":
                lista_testi.insert(posizione, valore_inserito)
                print("Inserito con successo!")

            elif scelta_tipo == "4":
                valore_bool = True if valore_inserito.lower() == "true" else False
                lista_booleani.insert(posizione, valore_bool)
                print("Inserito con successo!")

            else:
                print("Tipo selezionato non valido!")

        case "3":
            
            print("Quale lista vuoi modificare?")         # OPERAZIONE: MODIFICA ELEMENTO
            print("1. Interi | 2. Decimali | 3. Testi | 4. Booleani")
            scelta_tipo = input("Scegli il tipo (1-4): ")

            
            if scelta_tipo == "1":          # Gestiamo la modifica separatamente per ogni lista
                
                if len(lista_interi) > 0:           # Usiamo len() per verificare la lunghezza della lista
                    print("Lista attuale:", lista_interi)
                    posizione = int(input("Inserisci l'indice dell'elemento da modificare: "))

                    
                    if 0 <= posizione < len(lista_interi):          # Controlliamo che l'indice esista con un controllo if
                        nuovo_valore = int(input("Inserisci il nuovo intero: "))
                        lista_interi[posizione] = nuovo_valore          # Sovrascrittura all'indice
                        print("Modificato con successo!")
                    else:
                        print("Posizione non valida!")
                else:
                    print("La lista è vuota!")

            elif scelta_tipo == "2":
                if len(lista_decimali) > 0:
                    print("Lista attuale:", lista_decimali)
                    posizione = int(input("Inserisci l'indice dell'elemento da modificare: "))

                    if 0 <= posizione < len(lista_decimali):
                        nuovo_valore = float(input("Inserisci il nuovo decimale: "))
                        lista_decimali[posizione] = nuovo_valore
                        print("Modificato con successo!")
                    else:
                        print("Posizione non valida!")
                else:
                    print("La lista è vuota!")

            elif scelta_tipo == "3":
                if len(lista_testi) > 0:
                    print("Lista attuale:", lista_testi)
                    posizione = int(input("Inserisci l'indice dell'elemento da modificare: "))

                    if 0 <= posizione < len(lista_testi):
                        nuovo_valore = input("Inserisci il nuovo testo: ")
                        lista_testi[posizione] = nuovo_valore
                        print("Modificato con successo!")
                    else:
                        print("Posizione non valida!")
                else:
                    print("La lista è vuota!")

            elif scelta_tipo == "4":
                if len(lista_booleani) > 0:
                    print("Lista attuale:", lista_booleani)
                    posizione = int(input("Inserisci l'indice dell'elemento da modificare: "))

                    if 0 <= posizione < len(lista_booleani):
                        nuovo_valore_str = input("Inserisci il nuovo valore (True/False): ")
                        lista_booleani[posizione] = True if nuovo_valore_str.lower() == "true" else False
                        print("Modificato con successo!")
                    else:
                        print("Posizione non valida!")
                else:
                    print("La lista è vuota!")

        case "4":
            # OPERAZIONE: ELIMINAZIONE ELEMENTO 
            print("\nDa quale lista vuoi eliminare?")
            print("1. Interi | 2. Decimali | 3. Testi | 4. Booleani")
            scelta_tipo = input("Scegli il tipo (1-4): ")

            if scelta_tipo == "1" and len(lista_interi) > 0:
                print("Lista attuale:", lista_interi)
                posizione = int(input("Inserisci l'indice dell'elemento da eliminare: "))
                if 0 <= posizione < len(lista_interi):
                    rimosso = lista_interi.pop(posizione) # Rimuove l'elemento all'indice[cite: 36]
                    print("Rimosso:", rimosso)

            elif scelta_tipo == "2" and len(lista_decimali) > 0:
                print("Lista attuale:", lista_decimali)
                posizione = int(input("Inserisci l'indice dell'elemento da eliminare: "))
                if 0 <= posizione < len(lista_decimali):
                    rimosso = lista_decimali.pop(posizione)
                    print("Rimosso:", rimosso)

            elif scelta_tipo == "3" and len(lista_testi) > 0:
                print("Lista attuale:", lista_testi)
                posizione = int(input("Inserisci l'indice dell'elemento da eliminare: "))
                if 0 <= posizione < len(lista_testi):
                    rimosso = lista_testi.pop(posizione)
                    print("Rimosso:", rimosso)

            elif scelta_tipo == "4" and len(lista_booleani) > 0:
                print("Lista attuale:", lista_booleani)
                posizione = int(input("Inserisci l'indice dell'elemento da eliminare: "))
                if 0 <= posizione < len(lista_booleani):
                    rimosso = lista_booleani.pop(posizione)
                    print("Rimosso:", rimosso)

            else:
                print("Scelta non valida o lista selezionata vuota!")

        case "5":
            # OPERAZIONE: STAMPA LISTE
            mostra_tutte_le_liste()

        case "6":
            # OPERAZIONE: ESCI
            print("Chiusura del programma!")
            
            programma_attivo = False            # Impostiamo la variabile su False per interrompere il ciclo while

        case _:
                        # Caso di default se l'utente inserisce un numero errato
            print("Opzione non valida, riprova!")