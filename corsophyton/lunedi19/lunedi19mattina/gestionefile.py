def gestisci_file_completo():
    
    while True:
        print("\n=== MENU GESTIONE FILE (METODI SPECIFICI) ===")
        print("1 - Crea/Scrivi un file (usando 'with')")
        print("2 - Leggi interamente un file (usando read())")
        print("3 - Leggi riga per riga un file (usando readline())")
        print("4 - Modifica/Aggiungi testo a un file")
        print("5 - Svuota un file (usando open() e close() manuale)")
        print("6 - Esci")
        
        scelta = input("Scegli un'opzione (1-6): ").strip()
        
        if scelta == '6':
            print("Chiusura del programma. Arrivederci!")
            break
            
        if scelta in ['1', '2', '3', '4', '5']:
            nome_file = input("Inserisci il nome del file (es. prova.txt): ").strip()
            
            if not nome_file:
                print("Errore: Il nome del file non può essere vuoto.")
                continue
                
            # 1. CREAZIONE E SCRITTURA (Usando il blocco 'wi   th' e 'write()')
            if scelta == '1':
                testo = input("Inserisci il testo da scrivere nel file: ")
                try:
                    # Il blocco 'with' apre il file e chiama automaticamente .close() alla fine
                    with open(nome_file, 'w', encoding='utf-8') as f:
                        f.write(testo + "\n")
                    print(f"File '{nome_file}' scritto con successo tramite 'with'.")
                except Exception as e:
                    print(f"Errore: {e}")
                    
            # 2. LETTURA INTERA (Usando 'read()')
            elif scelta == '2':
                try:
                    with open(nome_file, 'r', encoding='utf-8') as f:
                        # read() legge tutto il contenuto del file in un'unica stringa
                        contenuto_totale = f.read()
                        
                    print(f"\n--- CONTENUTO INTEGRALE (read) ---")
                    if contenuto_totale:
                        print(contenuto_totale, end="")
                    else:
                        print("[Il file è vuoto]")
                    print("-" * 35)
                except FileNotFoundError:
                    print(f"Errore: Il file '{nome_file}' non esiste.")
                    
            # 3. LETTURA RIGA PER RIGA (Usando 'readline()')
            elif scelta == '3':
                try:
                    # Esempio di utilizzo dei comandi tradizionali open() e close() senza il blocco 'with'
                    f = open(nome_file, 'r', encoding='utf-8')
                    print(f"\n--- LETTURA RIGA PER RIGA (readline) ---")
                    
                    # readline() legge una singola riga alla volta spostando il cursore in avanti
                    riga = f.readline()
                    while riga != "":
                        print(riga, end="")
                        riga = f.readline()
                        
                    print("-" * 39)
                    # È obbligatorio chiudere manualmente il file quando non si usa il blocco 'with'
                    f.close() 
                except FileNotFoundError:
                    print(f"Errore: Il file '{nome_file}' non esiste.")
                    
            # 4. MODIFICA / AGGIUNTA TESTO (Modalità 'append')
            elif scelta == '4':
                testo_aggiuntivo = input("Inserisci il testo da aggiungere in coda: ")
                try:
                    # La modalità 'a' (append) apre il file per la scrittura aggiuntiva senza cancellare i dati precedenti
                    with open(nome_file, 'a', encoding='utf-8') as f:
                        f.write(testo_aggiuntivo + "\n")
                    print("Testo aggiunto con successo.")
                except Exception as e:
                    print(f"Errore: {e}")
                    
            # 5. SVUOTA IL FILE (Usando apertura e chiusura manuale con close())
            elif scelta == '5':
                try:
                    # Apertura in modalità 'w' azzera il contenuto. Qui usiamo open() e close() espliciti
                    file_pointer = open(nome_file, 'w', encoding='utf-8')
                    file_pointer.close() # Chiusura manuale obbligatoria
                    print(f"File '{nome_file}' svuotato con successo.")
                except Exception as e:
                    print(f"Errore: {e}")
        else:
            print("Opzione non valida. Scegli un numero da 1 a 6.")

if __name__ == "__main__":
    gestisci_file_completo()