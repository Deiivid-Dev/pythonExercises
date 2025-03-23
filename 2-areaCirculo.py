"""
Calcular el área de un círculo con un radio dado
"""

import math

radio = int(input("Digite el radio del círculo: "))

area = math.pi * (radio ** 2)

print(f"El área del círculo es: {area}")