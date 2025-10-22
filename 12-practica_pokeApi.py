# Práctica de manejo de APIs - PokeAPI en Python

import requests

URL = 'https://pokeapi.co/api/v2/pokemon/'

pokemon = input("Qué pokemón requieres buscar?\n")

respuesta = requests.get(URL + pokemon)

datos = respuesta.json()

print(f"------- Movimientos de {pokemon} -------")
for move in datos["moves"]:
    print(move["move"]["name"]) 

print(f"------- Tipos de {pokemon} -------")
for tipo in datos["types"]:
    print(tipo["type"]["name"])