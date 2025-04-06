"""
Escribir una función en Python que reciba una cadena de texto y devuelva la misma cadena pero invertida.
"""

text = input("Digite cualquier texto: ")

def invertir_cadena(string):
    invertida = ""

    for i in reversed(string):
        invertida += i
    return invertida

print(invertir_cadena(text))
