# ==========================================
# 1. CLASSE BASE (Interfaccia Comune)
# ==========================================
class MetodoPagamento:
    
    
    def effettua_pagamento(importo):            #Classe base che definisce la struttura comune  per tutti i metodi di pagamento.
        """Metodo generico che verrà sovrascritto (override) dalle classi figlie."""
        raise NotImplementedError("Le sottoclassi devono implementare questo metodo.")


# ==========================================
# 2. CLASSI DERIVATE (Comportamenti Specifici)
# ==========================================

class CartaDiCredito(MetodoPagamento):          #Classe derivata per i pagamenti tramite Carta di Credito.
    
    
    def __init__(self, numero_carta):
        self.numero_carta = numero_carta  # Attributo specifico della carta

    def effettua_pagamento(self, importo):              #Override del metodo: simula l'addebito su carta di credito.

        
        cifre_visibili = self.numero_carta[-4:] # Nascondiamo parte del numero per sicurezza visiva (es. ultime 4 cifre)
        print(f"Pagamento di {importo} € effettuato con successo tramite Carta di Credito (terminante in ****{cifre_visibili}).")


class PayPal(MetodoPagamento):              #Classe derivata per i pagamenti tramite conto PayPal.

    def __init__(self, email_account):
        self.email_account = email_account  # Email associata all'account PayPal

    def effettua_pagamento(self, importo):          #Override del metodo: simula il pagamento via conto PayPal.
        
        print(f"Pagamento di {importo} € effettuato con successo tramite account PayPal ({self.email_account}).")


class BonificoBancario(MetodoPagamento):               # Classe derivata per i pagamenti tramite Bonifico Bancario.
    
    def __init__(self, iban):
        self.iban = iban  # Codice IBAN del conto di appoggio

    def effettua_pagamento(self, importo):
        """Override del metodo: simula il pagamento tramite bonifico."""
        print(f"Pagamento di {importo} € effettuato tramite Bonifico Bancario sul conto IBAN: {self.iban}.")


# ==========================================
# 3. CLASSE GESTORE (Applicazione del Polimorfismo)
# ==========================================

class GestorePagamenti:          #Classe Gestore che sfrutta il Polimorfismo.
    
    def __init__(self, metodo_pagamento):
        # Associazione (composizione): il gestore memorizza l'istanza del pagamento scelta
        self.metodo_pagamento = metodo_pagamento

    def esegui_transazione(self, importo):            #Metodo che aziona il pagamento delegandolo all'oggetto specifico.
      
        print("Inizio elaborazione transazione...")         # Qui avviene il polimorfismo: a seconda di quale classe è stata passata
         
        self.metodo_pagamento.effettua_pagamento(importo)
        print("Transazione completata.\n")


# ==========================================
# ESEMPIO DI UTILIZZO E TEST DEL SISTEMA
# ==========================================

# 1. Creiamo i singoli oggetti specifici per il pagamento
carta = CartaDiCredito("1234567890123456")
paypal = PayPal("utente@email.com")
bonifico = BonificoBancario("IT88X01000000001234567890")

# 2. Creiamo il gestore passando di volta in volta metodi diversi (Polimorfismo in azione)
print("--- TEST 1: Pagamento con Carta di Credito ---")
gestore_1 = GestorePagamenti(carta)
gestore_1.esegui_transazione(150.00)

print("--- TEST 2: Pagamento con PayPal ---")
gestore_2 = GestorePagamenti(paypal)
gestore_2.esegui_transazione(45.50)

print("--- TEST 3: Pagamento con Bonifico Bancario ---")
gestore_3 = GestorePagamenti(bonifico)
gestore_3.esegui_transazione(1200.00)