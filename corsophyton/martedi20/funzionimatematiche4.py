import numpy as np

# Nome del file di testo in cui verranno salvati i risultati della prima metà del lavoro
NOME_FILE_LOG = "registro_matrici_parziale.txt"

def salva_su_file(testo_operazione):
    """
    Funzione ausiliaria per salvare progressivamente ogni operazione
    eseguita sul file di testo specificato.
    """
    try:
        with open(NOME_FILE_LOG, "a", encoding="utf-8") as file:
            file.write(testo_operazione + "\n" + "=" * 50 + "\n\n")
        print(f"-> Operazione salvata con successo nel file '{NOME_FILE_LOG}'")
    except Exception as e:
        print(f"-> Errore durante il salvataggio su file: {e}")


def mostra_menu():
    """
    Visualizza il menu interattivo limitato alla Parte 1 (50% del progetto).
    """
    print("\n" + "=" * 40)
    print("      GESTIONE MATRICI NUMPY (PARTE 1)")
    print("=" * 40)
    print("1. Crea una nuova matrice 2D casuale")
    print("2. Estrai e stampa la sotto-matrice centrale")
    print("3. Trasponi la matrice e stampala")
    print("4. Calcola la somma di tutti gli elementi")
    print("5. Esci dal programma")
    print("=" * 40)


def main():
    matrice = None

    while True:
        mostra_menu()
        scelta = input("Seleziona un'opzione (1-5): ").strip()

        # 1. Creazione nuova matrice casuale
        
        if scelta == "1":
            try:
                righe = int(input("Inserisci il numero di righe: "))
                colonne = int(input("Inserisci il numero di colonne: "))

                if righe <= 0 or colonne <= 0:
                    print("Errore: le dimensioni devono essere numeri interi positivi!")
                    continue

                matrice = np.random.randint(1, 51, size=(righe, colonne))

                testo_log = f"1. CREAZIONE MATRICE ({righe}x{colonne}):\n{matrice}"
                print("\nMatrice creata con successo:")
                print(matrice)
                salva_su_file(testo_log)

            except ValueError:
                print("Errore: inserisci un valore numerico intero valido!")

        elif scelta in ["2", "3", "4"] and matrice is None:
            print("\nAttenzione: Devi prima creare una matrice selezionando l'opzione 1!")

        
        # 2. Sotto-matrice centrale
        
        elif scelta == "2":
            righe, colonne = matrice.shape

            if righe < 3 or colonne < 3:
                print("\nPer estrarre una sotto-matrice centrale, le dimensioni devono essere almeno 3x3.")
                print(f"Dimensione attuale: {righe}x{colonne}")
            else:
                sotto_matrice = matrice[1:-1, 1:-1]
                
                testo_log = f"2. SOTTO-MATRICE CENTRALE (da {righe}x{colonne}):\n{sotto_matrice}"
                print("\nSotto-matrice centrale estratta:")
                print(sotto_matrice)
                salva_su_file(testo_log)

        
        # 3. Trasposizione della matrice
      
        elif scelta == "3":
            matrice_trasposta = matrice.T

            testo_log = f"3. MATRICE TRASPOSTA:\n{matrice_trasposta}"
            print("\nMatrice Trasposta:")
            print(matrice_trasposta)
            salva_su_file(testo_log)

        
        # 4. Calcolo della somma totale
        
        elif scelta == "4":
            somma_totale = matrice.sum()

            testo_log = f"4. SOMMA TOTALE ELEMENTI:\nSomma = {somma_totale}"
            print(f"\nLa somma di tutti gli elementi della matrice è: {somma_totale}")
            salva_su_file(testo_log)

        
        # 5. Uscita dal programma
        
        elif scelta == "5":
            print("\nUscita dal programma in corso... Arrivederci!")
            break

        else:
            print("\nOpzione non valida! Inserisci un numero da 1 a 5.")


if __name__ == "__main__":
    main()