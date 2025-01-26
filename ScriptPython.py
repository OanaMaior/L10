import math

# Definirea valorilor de input
num = 25
angle = 30

# 1. Calcularea rădăcinii pătrate
sqrt_value = math.sqrt(num)
print(f"Rădăcina pătrată a {num} este {sqrt_value}")

# 2. Calcularea factorialului
factorial_value = math.factorial(num)
print(f"Factorialul lui {num} este {factorial_value}")

# 3. Calcularea sinusului unui unghi dat în grade
# Convertim unghiul din grade în radiani
radians = math.radians(angle)
sin_value = math.sin(radians)
print(f"Sinusul unghiului de {angle} grade este {sin_value}")
