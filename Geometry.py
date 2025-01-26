# geometry.py

import math

# Modulul pentru cerc
def circle_area(radius):
    """Calculează aria cercului."""
    return math.pi * radius ** 2

def circle_circumference(radius):
    """Calculează circumferința cercului."""
    return 2 * math.pi * radius

# Modulul pentru dreptunghi
def rectangle_area(length, width):
    """Calculează aria dreptunghiului."""
    return length * width

def rectangle_perimeter(length, width):
    """Calculează perimetrul dreptunghiului."""
    return 2 * (length + width)

# Parte de testare a funcțiilor
if _name_ == "_main_":
    # Calcul pentru cerc
    radius = 5
    area_cerc = circle_area(radius)
    circumference_cerc = circle_circumference(radius)

    print(f"Aria cercului cu raza {radius} este {area_cerc:.2f}")
    print(f"Circumferința cercului cu raza {radius} este {circumference_cerc:.2f}")

    # Calcul pentru dreptunghi
    length = 10
    width = 4
    area_dreptunghi = rectangle_area(length, width)
    perimeter_dreptunghi = rectangle_perimeter(length, width)

    print(f"Aria dreptunghiului cu lungimea {length} și lățimea {width} este {area_dreptunghi}")
    print(f"Perimetrul dreptunghiului cu lungimea {length} și lățimea {width} este {perimeter_dreptunghi}")
