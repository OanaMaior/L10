# math_operations.py

def add(a, b):
    """Adună două numere."""
    return a + b

def subtract(a, b):
    """Scade b din a."""
    return a - b

def multiply(a, b):
    """Înmulțește două numere."""
    return a * b

def divide(a, b):
    """Împarte a la b."""
    if b == 0:
        raise ValueError("Împărțirea la zero nu este permisă.")
    return a / b

# Parte de testare a funcțiilor
if _name_ == "_main_":
    # Definirea valorilor
    num1 = 10
    num2 = 5

    # Utilizarea funcțiilor din modul
    suma = add(num1, num2)
    diferenta = subtract(num1, num2)
    produsul = multiply(num1, num2)
    impartirea = divide(num1, num2)

    # Afișarea rezultatelor
    print(f"Suma lui {num1} și {num2} este {suma}")
    print(f"Diferența lui {num1} și {num2} este {diferenta}")
    print(f"Produsul lui {num1} și {num2} este {produsul}")
    print(f"Împărțirea lui {num1} la {num2} este {impartirea}")
