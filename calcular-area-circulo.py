import math

# PASO 1: Solicitar al usuario que ingrese el radio del circulo.
radio = float(input("Por favor, ingrese el radio del circulo: "))

# PASO 2: Calcular el area del circulo utilizando la formula area = π * radio^2
area = math.pi * (radio**2)

# PASO 3: Mostrar al usuario el area calculada
print("El area del circulo con radio", radio, "es:", area)