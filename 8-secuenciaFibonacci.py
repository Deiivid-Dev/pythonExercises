"""
Escribir una función en Python que reciba un número n y devuelva los primeros n términos de la secuencia de Fibonacci.
"""

num = int(input("Digite un número: "))

def fibonacci(n):
    # Validaciones por si el usuario digita números inferiores
    if n <= 0:
        return []
    if n == 1:
        return [0]

    lista = [0, 1]

    for i in range(2, n):
        lista.append(lista[i - 2] + lista[i - 1])

    return lista

print(fibonacci(num))