class Produs:
    def __init__(self, nume, cantitate):
        self.nume = nume
        self.cantitate = cantitate

    def actualizeaza_cantitate(self, cantitate):
        if cantitate < 0:
            raise ValueError("Cantitatea nu poate fi negativă!")
        self.cantitate = cantitate

    def __str__(self):
        return f"{self.nume}: {self.cantitate} bucăți"


class Inventar:
    def __init__(self):
        self.produse = {}

    def adauga_produs(self, nume, cantitate):
        if nume in self.produse:
            print(f"Produsul {nume} există deja în inventar. Încercăm să actualizăm cantitatea.")
            self.produse[nume].actualizeaza_cantitate(self.produse[nume].cantitate + cantitate)
        else:
            self.produse[nume] = Produs(nume, cantitate)
            print(f"Produsul {nume} a fost adăugat în inventar.")

    def cauta_produs(self, nume):
        if nume in self.produse:
            print(self.produse[nume])
        else:
            print(f"Produsul {nume} nu există în inventar.")

    def actualizeaza_produs(self, nume, cantitate):
        if nume in self.produse:
            try:
                self.produse[nume].actualizeaza_cantitate(cantitate)
                print(f"Cantitatea produsului {nume} a fost actualizată la {cantitate}.")
            except ValueError as e:
                print(e)
        else:
            print(f"Produsul {nume} nu există în inventar.")


def meniu():
    inventar = Inventar()

    while True:
        print("\nMeniu:")
        print("1. Adaugă produs")
        print("2. Căută produs")
        print("3. Actualizează cantitatea unui produs")
        print("4. Ieși din program")
        
        optiune = input("Alege o opțiune (1-4): ")
        
        if optiune == '1':
            nume = input("Introdu numele produsului: ")
            try:
                cantitate = int(input("Introdu cantitatea: "))
                if cantitate < 0:
                    raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
                inventar.adauga_produs(nume, cantitate)
            except ValueError as e:
                print(e)
        
        elif optiune == '2':
            nume = input("Introdu numele produsului pe care vrei să-l cauți: ")
            inventar.cauta_produs(nume)
        
        elif optiune == '3':
            nume = input("Introdu numele produsului pentru care vrei să actualizezi cantitatea: ")
            try:
                cantitate = int(input("Introdu noua cantitate: "))
                if cantitatea < 0:
                    raise ValueError("Cantitatea trebuie să fie un număr pozitiv.")
                inventar.actualizeaza_produs(nume, cantitate)
            except ValueError as e:
                print(e)
        
        elif optiune == '4':
            print("La revedere!")
            break
        
        else:
            print("Opțiune invalidă! Te rog să alegi o opțiune între 1 și 4.")


if __name__ == "__main__":
    meniu()
