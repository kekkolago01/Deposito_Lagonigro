# esercizio 6 

nome = input("Inserisci il nome: ")
eta = input("Inserisci l'età: ")
sesso = input("Inserisci il sesso (M/F): ")
premium = input("Sei premium? (True/False): ")


if nome == "":
    print("Errore: il nome non può essere vuoto.")

elif eta == "":
    print("Errore: l'età non può essere vuota.")

elif sesso == "":
    print("Errore: il sesso non può essere vuoto.")

elif premium == "":
    print("Errore: il campo premium non può essere vuoto.")

else:
    
    eta = int(eta)

    if sesso == "M" or sesso == "F":

        if premium == "True" or premium == "False":

            if premium == "True":
                premium = True
            else:
                premium = False

            
            utente = [nome, eta, sesso, premium] # Prima lista

            print("Prima lista:", utente)

           
            scelta = input("Cosa vuoi fare? (modificare/creare/rimuovere): ")  # Scelta dell'operazione

            match scelta:

                
                case "modificare": # MODIFICARE

                    campo = input("Quale campo vuoi modificare? (nome/eta/sesso/premium): ")

                    match campo:

                        case "nome":
                            nuovo_nome = input("Inserisci il nuovo nome: ")

                            if nuovo_nome == "":
                                print("Il nome non può essere vuoto.")
                            else:
                                utente[0] = nuovo_nome

                        case "eta":
                            nuova_eta = input("Inserisci la nuova età: ")

                            if nuova_eta == "":
                                print("L'età non può essere vuota.")
                            else:
                                utente[1] = int(nuova_eta)

                        case "sesso":
                            nuovo_sesso = input("Inserisci il nuovo sesso (M/F): ")

                            if nuovo_sesso == "M" or nuovo_sesso == "F":
                                utente[2] = nuovo_sesso
                            else:
                                print("Il sesso deve essere M oppure F.")

                        case "premium":
                            nuovo_premium = input("Inserisci True oppure False: ")

                            if nuovo_premium == "True":
                                utente[3] = True

                            elif nuovo_premium == "False":
                                utente[3] = False

                            else:
                                print("Inserisci True oppure False.")

                        case _:
                            print("Campo non valido.")


                
                case "creare": # CREARE UNA SECONDA LISTA

                    nome2 = input("Inserisci il nome del secondo utente: ")
                    eta2 = input("Inserisci l'età del secondo utente: ")
                    sesso2 = input("Inserisci il sesso del secondo utente (M/F): ")
                    premium2 = input("Il secondo utente è premium? (True/False): ")

                    if nome2 == "":
                        print("Il nome non può essere vuoto.")

                    elif eta2 == "":
                        print("L'età non può essere vuota.")

                    elif sesso2 == "":
                        print("Il sesso non può essere vuoto.")

                    elif premium2 == "":
                        print("Premium non può essere vuoto.")

                    else:

                        eta2 = int(eta2)

                        if premium2 == "True":
                            premium2 = True
                        else:
                            premium2 = False

                        utente2 = [nome2, eta2, sesso2, premium2]

                        print("Seconda lista:", utente2)


                case "rimuovere":                 # RIMUOVERE LA PRIMA LISTA

                    utente.clear()

                    print("La prima lista è stata rimossa.")


                case _:
                    print("Operazione non valida.")


            print("Lista finale:", utente)

        else:
            print("Premium deve essere True oppure False.")

    else:
        print("Il sesso deve essere M oppure F.")