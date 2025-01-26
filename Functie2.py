def citeste_si_suma_numere(fisier):
    suma = 0
    try:
        # Deschiderea fișierului pentru citire
        with open(fisier, 'r') as file:
            for linie in file:
                try:
                    # Încercăm să convertim fiecare linie într-un număr
                    numar = float(linie.strip())
                    suma += numar
                except ValueError:
                    print(f"Warning: Linia '{linie.strip()}' nu este un număr valid.")
        return suma
    except FileNotFoundError:
        return f"Eroare: Fișierul '{fisier}' nu a fost găsit."
    except IOError:
        return "Eroare la citirea fișierului."

# Exemplu de utilizare
nume_fisier = input("Introduceti numele fisierului: ")
rezultatul = citeste_si_suma_numere(nume_fisier)
print(f"Suma numerelor din fișier este: {rezultatul}")
