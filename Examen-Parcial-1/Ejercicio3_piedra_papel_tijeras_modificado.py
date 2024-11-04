'''
Nombre: Rebeca Gregorio Espina.
Fecha: 4 de noviembre de 2024.
Descripción:
Este programa es el famoso juego de "piedra, papel o tijera", en donde el contrincante es la CPU. La opción de la CPU se escogerá de forma aleatorio con la función randint().
El juego mostrará las victorias del jugador, los partidos empatados y las victorias del CPU. Además, mostrará el siguiente menú:
    -No pedir números, sino las palabras "piedra, papel o tijera".
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

    - Muestre la cantidad de victorias, empates y derrotas.
    - Pida al usuario una opción del menú.
    - Realice la lógica adecuada para calcular al ganador.
    - Muestre en la consola la elección del jugador, del CPU y el resultado.
    - Repita nuevamente el menú hasta salir.
'''
from random import randint
opcion_jugador = 1
victorias_jugador=0
victorias_cpu=0
empates = 0
while opcion_jugador != 0 :
    print("\n*** Juego de piedra, papel o tijera   ***")
# Muestre la cantidad de victorias, empates y derrotas.
    print(f"Victorias del jugador: {victorias_jugador}, empates: {empates} y victorias del CPU: {victorias_cpu}")
    opcion_jugador = input("Ingrese 'piedra', 'papel', 'tijera' o 'salir': ") # Pedir una opción al usuario.
    opcion_jugador = opcion_jugador.lower()
    if opcion_jugador == "salir":
        break # Al momento en el que el usuario ingresa la palabra salir, se detiene el ciclo.
    opcion_cpu = randint(1,3)
    if opcion_cpu == 1:
        opcion_cpu = "piedra"
    if opcion_cpu == 2:
        opcion_cpu = "papel"
    if opcion_cpu == 3:
        opcion_cpu = "tijera"
    if opcion_jugador == "piedra" and opcion_cpu == "piedra":
        print("Jugador: Piedra. CPU: Piedra. El resultado es empate.")
        empates+=1
    elif opcion_jugador == "papel" and opcion_cpu == "papel":
        print("Jugador: Papel. CPU: Papel. El resultado es empate.")
        empates+=1
    elif opcion_jugador == "Tijera" and opcion_cpu == "Tijera":
        print("Jugador: Tijera. CPU: Tijera. El resultado es empate.")
        empates+=1
    elif opcion_jugador == "piedra" and opcion_cpu == "tijera":
        print("Jugador: Piedra. CPU: Tijera. El ganador es el CPU.")
        victorias_cpu+=1
    elif opcion_jugador == "papel" and opcion_cpu == "piedra":
        print("Jugador: Papel. CPU: Piedra. El ganador es el CPU.")
        victorias_cpu += 1
    elif opcion_jugador == "tijera" and opcion_cpu == "papel":
        print("Jugador: Tijera. CPU: Papel. El ganador es el CPU.")
        victorias_cpu+=1
    elif opcion_jugador == "tijera" and opcion_cpu == "piedra":
        print("Jugador: Tijera. CPU: Piedra. El ganador es el jugador.")
        victorias_jugador+=1
    elif opcion_jugador == "piedra" and opcion_cpu == "papel":
        print("Jugador: Piedra. CPU: Papel. El ganador es el Jugador.")
        victorias_jugador+=1
    elif opcion_jugador == "papel" and opcion_cpu == "tijera":
        print("Jugador: Papel. CPU: Tijera. El ganador es el jugador.")
        victorias_jugador+=1
    else:
        print("Opción no válida.")  # Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
    print("--------------------------------------")
print()
print("Fin del juego.")