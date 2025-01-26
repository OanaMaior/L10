def imparte_numere(a, b):
    try:
        # Împărțirea celor două numere
        rezultat = a / b
        return rezultat
    except ZeroDivisionError:
        # Tratarea excepției de împărțire la zero
        return "Eroare: Împărțirea la zero nu este permisă!"

# Introducerea datelor de la tastatură
numar1 = float(input("Introdu primul numar: "))
numar2 = float(input("Introdu al doilea numar: "))

# Apelarea funcției
rezultatul = imparte_numere(numar1, numar2)

# Afișarea rezultatului
print(f"Rezultatul împărțirii este: {rezultatul}")
