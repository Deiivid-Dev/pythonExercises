"""
Escribir una función en Python que determine si un número es primo.
"""

def es_primo(num):
    if (num < 2):
        print("El número debe ser mayor a 2")
        return False
    
    # Se realiza el cálculo solo hasta la raíz cuadrada del número
    for i in range(2, int(num ** 0.5) + 1):
         if num % i == 0:
              # Si se encuentra un divisor, significa que no es primo
              return False

    # Si no se encuentra ningún divisor, significa que es primo
    return True

num = int(input("Digite un número: "))
print(es_primo(num))