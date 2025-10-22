"""
Programa que permite convertir entre distintas unidades: Celsius <-> Fahrenheit, Kelvin, Metros <-> Kilómetros
"""

def conversion_celsius_fahrenheit():
    while True:
        print("\n--- Conversor de Unidades ---")
        print("1. Convertir Temperaturas")
        print("2. Convertir Longitudes")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            convertir_temperatura()
        elif opcion == "2":
            convertir_longitud()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")

def convertir_temperatura():
    # Unidad origen
    print("\n--- Conversor de Temperaturas ---")

    print("¿Desde qué unidad quieres convertir?")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Kelvin (K)")
    origen = input("Elige una opción (1-3): ")

    # Unidad final
    print("\n¿A qué unidad quieres convertir?")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Kelvin (K)")
    destino = input("Elige una opción (1-3): ")

    if origen == destino:
        print("⚠️ No puedes convertir a la misma unidad.")
        return

    valor = float(input("\nIngresa el valor de la temperatura a convertir: "))

    if origen == "1" and destino == "2":
        resultado = (valor * 9/5) + 32
    elif origen == "1" and destino == "3":
        resultado = valor + 273.15
    elif origen == "2" and destino == "1":
        resultado = (valor - 32) * 5/9
    elif origen == "2" and destino == "3":
        resultado = (valor - 32) * 5/9 + 273.15
    elif origen == "3" and destino == "1":
        resultado = valor - 273.15
    elif origen == "3" and destino == "2":
        resultado = (valor - 273.15) * 9/5 + 32
    else:
        print("Opción inválida.")
        return
    print(f"\nResultado: {resultado:.2f}")

def convertir_longitud():
    print("\n--- Conversor de Longitudes ---")

    print("¿Desde qué unidad quieres convertir?")
    print("1. Metros (m)")
    print("2. Kilómetros (km)")
    print("3. Centímetros (cm)")
    origen = input("Elige una opción (1-3): ")

    print("\n¿A qué unidad quieres convertir?")
    print("1. Metros (m)")
    print("2. Kilómetros (km)")
    print("3. Centímetros (cm)")
    destino = input("Elige una opción (1-3): ")

    if origen == destino:
        print("⚠️ No puedes convertir a la misma unidad.")
        return
    
    valor = float(input("\nIngresa el valor de la longitud a convertir: "))

    # Conversión según las unidades seleccionadas
    if origen == "1" and destino == "2":      # m → km
        resultado = valor / 1000
    elif origen == "1" and destino == "3":    # m → cm
        resultado = valor * 100
    elif origen == "2" and destino == "1":    # km → m
        resultado = valor * 1000
    elif origen == "2" and destino == "3":    # km → cm
        resultado = valor * 100000
    elif origen == "3" and destino == "1":    # cm → m
        resultado = valor / 100
    elif origen == "3" and destino == "2":    # cm → km
        resultado = valor / 100000
    else:
        print("Opción inválida.")
        return
    print(f"\nResultado: {resultado:.4f}")

conversion_celsius_fahrenheit()