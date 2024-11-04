'''
Nombre: Rebeca Gregorio Espina.
Fecha: 3 de noviembre de 2024.
Descripción:
Este programa es el famoso juego de "piedra, papel o tijera", en donde el contrincante es la CPU. La opción de la CPU se escogerá de forma aleatorio con la función randint().
El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Además, mostrará el siguiente menú:
1) Piedra.
2) Papel.
3) Tijera.
0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

INSTRUCCIONES:
Escribe un programa de nombre Ejercicio3_piedra_papel_tijeras.py y sube el enlace de GitHub.
Para ello:
a) Muestre la cantidad de victorias, empates y derrotas.
b) Pida al usuario una opción del menú.
c) Realice la lógica adecuada para calcular al ganador.
d) Muestre en la consola la elección del jugador, del CPU y el resultado.
e) Repita nuevamente el menú hasta salir.
'''
from random import randint
opcion_jugador = 1
victorias_jugador=0
victorias_cpu=0
empates = 0
while opcion_jugador != 0 :
    print("\n*** Juego de piedra, papel o tijera   ***")
# a) Muestre la cantidad de victorias, empates y derrotas.
    print(f"Victorias del jugador: {victorias_jugador}, empates: {empates} y victorias del CPU: {victorias_cpu}")
    print("[1].- Piedra.")
    print("[2].- Papel.")
    print("[3].- Tijera.")
    print("[0].- Salir.")
    opcion_jugador = int(input("Seleccione una de las opciones anteriores: "))  # b) Pida al usuario una opción del menú.
    if opcion_jugador != 0:
        opcion_cpu = randint(1,3)
    # c) Realice la lógica adecuada para calcular al ganador.
        if opcion_jugador == 1 and opcion_cpu == 1:
            print("Jugador: Piedra. CPU: Piedra. El resultado es empate.")
            empates+=1
        elif opcion_jugador == 2 and opcion_cpu == 2:
            print("Jugador: Papel. CPU: Papel. El resultado es empate.")
            empates+=1
        elif opcion_jugador == 3 and opcion_cpu == 3:
            print("Jugador: Tijera. CPU: Tijera. El resultado es empate.")
            empates+=1
        elif opcion_jugador == 1 and opcion_cpu == 3:
            print("Jugador: Piedra. CPU: Tijera. El ganador es el jugador.")
            victorias_jugador+=1
        elif opcion_jugador == 2 and opcion_cpu == 1:
            print("Jugador: Papel. CPU: Piedra. El ganador es el jugador.")
            victorias_jugador += 1
        elif opcion_jugador == 3 and opcion_cpu == 2:
            print("Jugador: Tijera. CPU: Papel. El ganador es el jugador.")
            victorias_jugador+=1
        elif opcion_jugador == 3 and opcion_cpu == 1:
            print("Jugador: Tijera. CPU: Piedra. El ganador es el CPU.")
            victorias_cpu+=1
        elif opcion_jugador == 1 and opcion_cpu == 2:
            print("Jugador: Piedra. CPU: Papel. El ganador es el CPU.")
            victorias_cpu+=1
        elif opcion_jugador == 2 and opcion_cpu == 3:
            print("Jugador: Papel. CPU: Tijera. El ganador es el CPU.")
            victorias_cpu+=1
        else:
            print("Opción no válida.")  # Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
        print("--------------------------------------")
print()
print("Fin del juego.")

# d) Muestre en la consola la elección del jugador, del CPU y el resultado.
# e) Repita nuevamente el menú hasta salir.
"""
# Resultados en consola:
    *** Juego de piedra, papel o tijera   ***
    Victorias del jugador: 0, empates: 0 y victorias del CPU: 0
    [1].- Piedra.
    [2].- Papel.
    [3].- Tijera.
    [0].- Salir.
    Seleccione una de las opciones anteriores: 1
    Jugador: Piedra. CPU: Tijera. El ganador es el jugador.
    --------------------------------------
    
    *** Juego de piedra, papel o tijera   ***
    Victorias del jugador: 1, empates: 0 y victorias del CPU: 0
    [1].- Piedra.
    [2].- Papel.
    [3].- Tijera.
    [0].- Salir.
    Seleccione una de las opciones anteriores: 2
    Jugador: Papel. CPU: Papel. El resultado es empate.
    --------------------------------------
    
    *** Juego de piedra, papel o tijera   ***
    Victorias del jugador: 1, empates: 1 y victorias del CPU: 0
    [1].- Piedra.
    [2].- Papel.
    [3].- Tijera.
    [0].- Salir.
    Seleccione una de las opciones anteriores: 2
    Jugador: Papel. CPU: Piedra. El ganador es el jugador.
    --------------------------------------
    
    *** Juego de piedra, papel o tijera   ***
    Victorias del jugador: 2, empates: 1 y victorias del CPU: 0
    [1].- Piedra.
    [2].- Papel.
    [3].- Tijera.
    [0].- Salir.
    Seleccione una de las opciones anteriores: 3
    Jugador: Tijera. CPU: Piedra. El ganador es el CPU.
    --------------------------------------
    
    *** Juego de piedra, papel o tijera   ***
    Victorias del jugador: 2, empates: 1 y victorias del CPU: 1
    [1].- Piedra.
    [2].- Papel.
    [3].- Tijera.
    [0].- Salir.
    Seleccione una de las opciones anteriores: 3
    Jugador: Tijera. CPU: Papel. El ganador es el jugador.
    --------------------------------------
    
    *** Juego de piedra, papel o tijera   ***
    Victorias del jugador: 3, empates: 1 y victorias del CPU: 1
    [1].- Piedra.
    [2].- Papel.
    [3].- Tijera.
    [0].- Salir.
    Seleccione una de las opciones anteriores: 3
    Jugador: Tijera. CPU: Papel. El ganador es el jugador.
    --------------------------------------
    
    *** Juego de piedra, papel o tijera   ***
    Victorias del jugador: 4, empates: 1 y victorias del CPU: 1
    [1].- Piedra.
    [2].- Papel.
    [3].- Tijera.
    [0].- Salir.
    Seleccione una de las opciones anteriores: 1
    Jugador: Piedra. CPU: Papel. El ganador es el CPU.
    --------------------------------------
    
    *** Juego de piedra, papel o tijera   ***
    Victorias del jugador: 4, empates: 1 y victorias del CPU: 2
    [1].- Piedra.
    [2].- Papel.
    [3].- Tijera.
    [0].- Salir.
    Seleccione una de las opciones anteriores: 2
    Jugador: Papel. CPU: Tijera. El ganador es el CPU.
    --------------------------------------
    
    *** Juego de piedra, papel o tijera   ***
    Victorias del jugador: 4, empates: 1 y victorias del CPU: 3
    [1].- Piedra.
    [2].- Papel.
    [3].- Tijera.
    [0].- Salir.
    Seleccione una de las opciones anteriores: 4
    Opción no válida.
    --------------------------------------
    
    *** Juego de piedra, papel o tijera   ***
    Victorias del jugador: 4, empates: 1 y victorias del CPU: 3
    [1].- Piedra.
    [2].- Papel.
    [3].- Tijera.
    [0].- Salir.
    Seleccione una de las opciones anteriores: 0
    
    Fin del juego.
"""