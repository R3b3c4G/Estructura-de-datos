'''
Nombre: Rebeca Gregorio Espina.
Fecha: 6 de diciembre del 2024.
Descripción:
Este programa es una nueva versión del juego realizado de piedra, papel y tijeras, pero utilizando un diccionario para las reglas del juego.

INSTRUCCIONES:
Escribe un programa de nombre Diccionarios_ej1_piedra_papel_tijera.py que realice lo siguiente:
El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Se debe mostrar el siguiente menú:
      ***  Juego de piedra, papel o tijeras  ***
    1) Piedra.
    2) Papel.
    3) Tijeras.
    0) Salir.
    Cualquier otro caso -> Opción no válida.
Para ello:
    a) Muestre el menú en una función que pida al usuario una de las opciones: piedra, papel o tijeras.
    b) Utilice un diccionario para las distintas combinaciones.
    c) Realice la lógica adecuada para determinar al ganador. Se requiere que utilice al menos una función.
    d) Muestre la elección del jugador y la del cpu.
    e) Muestre la cantidad de victorias, empates y derrotas.
    f) Repita nuevamente el menú hasta salir.

'''
from random import choice
# a) Muestre el menú en una función que pida al usuario una de las opciones: piedra, papel o tijeras.
def menu ():    # Función para imprimir menú y devolver opción del usuario.
    print("*** Juego de piedra, papel o tijera   ***")
    print("     [1].- Piedra.")
    print("     [2].- Papel.")
    print("     [3].- Tijeras.")
    print("     [0].- Salir.")
    opcion = int(input("\nIngresa una de las opciones: "))
    return opcion
# c) Realice la lógica adecuada para determinar al ganador. Se requiere que utilice al menos una función.
def jugar (opcion):
    if opcion == 1:
        opcion_usuario = piedra
    elif opcion == 2:
        opcion_usuario = papel
    elif opcion == 3:
        opcion_usuario = tijeras
    opcion_cpu = choice([piedra, papel, tijeras])   # Generar elemento aleatorio para la CPU.
    return opcion_usuario, opcion_cpu   # Devolver opción del jugador y de la CPU.

piedra = "Piedra."
papel = "Papel."
tijeras = "Tijeras."
jugador = "Gana el jugador."
empate = "Empate."
cpu = "Gana la CPU."
victorias_jugador = 0
victorias_cpu = 0
empate_juego = 0
opcion = menu()
while opcion != 0:
    if opcion >=0 and opcion <= 3:
        opcion_usuario, opcion_cpu = jugar(opcion)
        opciones_juego = {(piedra, papel): cpu, # b) Utilice un diccionario para las distintas combinaciones.
                    (papel, piedra): jugador,
                    (piedra, tijeras): jugador,
                    (tijeras, piedra): cpu,
                    (papel,tijeras) : cpu,
                    (tijeras, papel): jugador
                    }
        resultado = opciones_juego.get((opcion_usuario, opcion_cpu), empate)
        if resultado == jugador:    # Lógica para determinar ganador.
            victorias_jugador += 1  # Cantidad de juegos ganados del jugador.
        elif resultado == cpu:
            victorias_cpu += 1  # Cantidad de juegos ganados de la CPU.
        else:
            empate_juego += 1   # Cantidad de juegos empatados.
        print(f"Jugador:{opcion_usuario} CPU: {opcion_cpu} El resultado es: {resultado}")# d) Muestre la elección del jugador y la del cpu.
        print(f"Victorias del jugador: {victorias_jugador}. Victorias del CPU: {victorias_cpu}. Empates: {empate_juego}.")# e) Muestre la cantidad de victorias, empates y derrotas.
    else:
        print("\nOpción no válida.")
    print("---------------------------------------------------\n")
    opcion = menu() # f) Repita nuevamente el menú hasta salir.
print("\nFin del juego.")
print("---------------------------------------------------")


