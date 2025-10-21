"""
Crear un programa en Python que permita jugar Piedra, Papel o Tijeras contra la computadora.
"""

import random

def init_game():
    print("Juego de Piedra, Papel y Tijeras")

    while True:
        player_name = input("Hola jugador, ingrese su nombre para iniciar: ")
        if not player_name:
            print("El nombre es requerido")
        else:
            break

    print(f"Vale {player_name}, ¿qué elemento quieres seleccionar?\n ")
    while True:
        opcion = input("Escoge: \n1. Para Piedra ✊ \n2. Para Papel ✋ \n3. Para Tijeras ✌️\n")

        if not opcion.isdigit() or int(opcion) not in [1, 2, 3]:
            print("Debes ingresar un número válido (1, 2 o 3).")
        else:
            player_selection = int(opcion)
            break

    cpu_selection = cpu_game()
    determinar_ganador(player_selection, cpu_selection)
    
def cpu_game():
    number = random.randint(1, 3)

    return number

def determinar_ganador(player_selection, cpu_selection):
    opciones = {1: "Piedra ✊", 2: "Papel ✋", 3: "Tijeras ✌️"}

    print(f"\nTú elegiste: {opciones[player_selection]}")
    print(f"La maquina eligió: {opciones[cpu_selection]}")

    if player_selection == cpu_selection:
        print("Empate 🤝")
    elif (player_selection == 1 and cpu_selection == 3) or \
         (player_selection == 2 and cpu_selection == 1) or \
         (player_selection == 3 and cpu_selection == 2):
        print("¡Ganaste! 🎉")
    else:
        print("Perdiste 😢")

init_game()