"""
Escribir una función en Python que reciba una cadena de texto y devuelva la misma cadena pero invertida.
"""

text = input("Digite cualquier texto: ")

def invertir_cadena(string):
    string_invertido = ""

    for i in reversed(string):
        string_invertido += i
    return string_invertido

print(invertir_cadena(text))