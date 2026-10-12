# main.py
import utility

def mostra_menu():
    print("" + "="*30)
    print("      CALCOLATRICE PYTHON")
    print("="*30)
    print("1. Addizione (+)")
    print("2. Sottrazione (-)")
    print("3. Moltiplicazione (*)")
    print("4. Divisione (/)")
    print("5. Esci")
    print("="*30)

def avvia_calcolatrice():
    while True:
        mostra_menu()
        scelta = input("Scegli un'operazione (1-5): ").strip()

        if scelta == '5':
            print("Grazie per aver usato la calcolatrice. Arrivederci!")
            break

        if scelta in ['1', '2', '3', '4']:
            # Gestione dell'input per evitare errori di battitura (es. inserimento di lettere)
            try:
                num1 = float(input("Inserisci il primo numero: "))
                num2 = float(input("Inserisci il secondo numero: "))
            except ValueError:
                print("[!] Errore: inserisci solo valori numerici validi.")
                continue

            # Chiamata alla funzione corrispondente dal file utility
            if scelta == '1':
                risultato = utility.addizione(num1, num2)
                print(f"Risultato: {num1} + {num2} = {risultato}")
            elif scelta == '2':
                risultato = utility.sottrazione(num1, num2)
                print(f"Risultato: {num1} - {num2} = {risultato}")
            elif scelta == '3':
                risultato = utility.moltiplicazione(num1, num2)
                print(f"Risultato: {num1} * {num2} = {risultato}")
            elif scelta == '4':
                risultato = utility.divisione(num1, num2)
                print(f"Risultato: {num1} / {num2} = {risultato}")
        else:
            print("[!] Scelta non valida. Inserisci un numero da 1 a 5.")

if __name__ == "__main__":
    avvia_calcolatrice()