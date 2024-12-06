'''
Nombre: Rebeca Gregorio Espina.
Fecha: 6 de diciembre del 2024.
Descripción:
Este programa es una versión mejorada del juego de piedra, papel y tijeras.

INSTRUCCIONES:
Escribe un programa de nombre Diccionarios_ej2_piedra_papel_tijera_lagarto_spock.py que realice lo siguiente:
Se debe mostrar el siguiente menú:
      ***  Juego de piedra, papel, tijeras, lagarto, spock  ***
    1) Piedra.
    2) Papel.
    3) Tijeras.
    4) Lagarto.
    5) Spock.
    6) Ver reglas.
    0) Salir.
    Cualquier otro caso -> Opción no válida.

Para ello:
    a) Muestre el menú en una función que pida al usuario una de las opciones.
    b) Utilice un diccionario para las distintas combinaciones.
    c) Realice la lógica adecuada para determinar al ganador.
    d) Muestre la elección del jugador y la del cpu.
    e) Muestre la cantidad de victorias, empates y derrotas.
    f) Repita nuevamente el menú hasta salir.
'''
from random import choice
# a) Muestre el menú en una función que pida al usuario una de las opciones.
def menu ():    # Función para imprimir menú y devolver opción del usuario.
    print("***  Juego de piedra, papel, tijeras, lagarto, spock  ***")
    print("     [1].- Piedra.")
    print("     [2].- Papel.")
    print("     [3].- Tijeras.")
    print("     [4].- Lagarto.")
    print("     [5].- Spock.")
    print("     [6].- Ver reglas.")
    print("     [0].- Salir.")
    opcion = int(input("\nIngresa una de las opciones: "))
    return opcion

def reglas ():  # Función para mostrar las reglas del juego.
    print("Reglas:")
    print("Selecciona una de las opciones de acuerdo a lo siguiente:")
    print("- Tijeras cortan papel.")
    print("- Papel cubre piedra.")
    print("- Piedra aplasta lagarto.")
    print("- Lagarto envenena Spock.")
    print("- Spock destruye tijeras.")
    print("- Tijeras decapitan lagarto.")
    print("- Lagarto come papel.")
    print("- Papel desaprueba Spock.")
    print("- Spock vaporiza piedra.")
    print("- Piedra aplasta tijeras.")
    print("La cpu va a elegir una de las opciones de manera aleatoria.")
    print("------------------------------------------------------------\n")
# Función para determinar que elemento es el jugador y cuál es la CPU.
def jugar (opcion):
    if opcion == 1:
        opcion_usuario = piedra
    elif opcion == 2:
        opcion_usuario = papel
    elif opcion == 3:
        opcion_usuario = tijeras
    elif opcion == 4:
        opcion_usuario = lagarto
    elif opcion == 5:
        opcion_usuario = spock
    opcion_cpu = choice([piedra, papel, tijeras, lagarto, spock])   # Generar elemento aleatorio para la CPU.
    return opcion_usuario, opcion_cpu   # Devolver opción del jugador y de la CPU.

piedra = "Piedra."
papel = "Papel."
tijeras = "Tijeras."
lagarto = "Lagarto."
spock = "Spock."
jugador = "Gana el jugador."
empate = "Empate."
cpu = "Gana la CPU."
victorias_jugador = 0
victorias_cpu = 0
empate_juego = 0
opcion = menu()
while opcion != 0:
    if opcion >=0 and opcion <= 6:
        if opcion == 6:
            reglas()
        else:
            opcion_usuario, opcion_cpu = jugar(opcion)
            opciones_juego = {(tijeras, papel): jugador,  # b) Utilice un diccionario para las distintas combinaciones.
                              (papel, tijeras): cpu,
                              (papel, piedra): jugador,
                              (piedra, papel): cpu,
                              (piedra, lagarto): jugador,
                              (lagarto, piedra): cpu,
                              (lagarto, spock): jugador,
                              (spock, lagarto): cpu,
                              (spock, tijeras): jugador,
                              (tijeras, spock): cpu,
                              (tijeras, lagarto): jugador,
                              (lagarto, tijeras): cpu,
                              (lagarto, papel): jugador,
                              (papel, lagarto): cpu,
                              (papel, spock): jugador,
                              (spock, papel): cpu,
                              (spock, piedra): jugador,
                              (piedra, spock): cpu,
                              (piedra, tijeras): jugador,
                              (tijeras, piedra): cpu
                              }
            resultado = opciones_juego.get((opcion_usuario, opcion_cpu), empate)
            if resultado == jugador:    # c) Realice la lógica adecuada para determinar al ganador.
                victorias_jugador += 1  # Cantidad de juegos ganados del jugador.
            elif resultado == cpu:
                victorias_cpu += 1  # Cantidad de juegos ganados de la CPU.
            else:
                empate_juego += 1   # Cantidad de juegos empatados.
            print(f"Jugador:{opcion_usuario} CPU: {opcion_cpu} El resultado es: {resultado}")   # d) Muestre la elección del jugador y la del cpu.
            print(f"Victorias del jugador: {victorias_jugador}. Victorias del CPU: {victorias_cpu}. Empates: {empate_juego}.")   # e) Muestre la cantidad de victorias, empates y derrotas.
    else:
        print("\nOpción no válida.")
    print("---------------------------------------------------\n")
    opcion = menu()  # f) Repita nuevamente el menú hasta salir.
print("\nFin del juego.")
print("---------------------------------------------------")