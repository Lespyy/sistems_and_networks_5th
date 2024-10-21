class Testo():
    def __init__(self, stringa, chiave, cifrato):
        self.stringa = stringa.lower() 
        self.chiave = chiave.lower() 
        self.cifrato = cifrato  # bool per indicare se è cifrato o meno
        self.cifra = []
        self.decifra = []
                
    def cifra_cod(self, dizio):
        if not self.cifrato:
            lista_chiave = [c for c in self.chiave]
            for indice, char in enumerate(self.stringa):
                if char in dizio and lista_chiave[indice] in dizio:
                    self.cifra.append((dizio[char] + dizio[lista_chiave[indice]]) % 21)
                else:
                    raise ValueError(f"Carattere '{char}' o '{lista_chiave[indice]}' non valido")
            self.cifrato = True
            print("Cifrato:", ",".join(str(c) for c in self.cifra))  # La virgola per separare i numeri
        else:
            print("La stringa è già cifrata")
    
    def decifra_cod(self, dizio, diz_num):
        if self.cifrato:
            lista_chiave = [c for c in self.chiave]
            for indice, elem in enumerate(self.cifra):
                self.decifra.append(dizio[(elem - diz_num[lista_chiave[indice]]) % 21])
            self.cifrato = False
            print("Decifrato:", "".join(c for c in self.decifra))  # Unisci le lettere
        else:
            print("La stringa è già decifrata")
        
def main():
    """
    Codice Cifrario di Vernam. 
    Tradurre una stringa in input usando il cifrario di Vernam.
    """
    diz_par = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f',
               6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 
               12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r',
               18: 's', 19: 't', 20: 'u'}  # Mappatura aggiornata
    
    diz_num = {v: k for k, v in diz_par.items()}  # Dizionario inverso: lettere -> numeri
    
    parola = input("Inserisci una parola: ").strip()
    chiave = input("Inserisci una chiave (almeno lunga quanto la parola): ").strip()
    
    if len(chiave) < len(parola):
        print("La chiave deve essere lunga almeno quanto la parola.")
        return

    testo = Testo(parola, chiave, False)
    testo.cifra_cod(diz_num)
    testo.decifra_cod(diz_par, diz_num)

if __name__ == "__main__":
    main()
