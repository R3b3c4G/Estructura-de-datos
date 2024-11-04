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
import random
opcion = 1
victorias_jugador=0
victorias_cpu=0
empates = 0
while opcion != 0 :
    print("*** Juego de piedra, papel o tijera   ***")
    print(f"Victorias del jugador: {victorias_jugador}, empates: {empates} y victorias del CPU: {victorias_cpu}")
    print("[1].- Piedra.")
    print("[2].- Papel.")
    print("[3].- Tijera.")
    print("[0].- Salir.")
    opcion_jugador = int(input("Seleccione una de las opciones anteriores: "))
    opcion_cpu = random.randint(1,3)
    if opcion_jugador == opcion_cpu:
        resultado= "empate"
        empates+=1
    if opcion_jugador == 1 and opcion_cpu == 3:
        resultado_jugador = "piedra"
        resultado_cpu = "tijera"
        victorias_jugador+=1
    if opcion_jugador == 2 and opcion_cpu == 1:
        resultado_jugador= "papel"
        resultado_cpu = "piedra"
        victorias_jugador += 1
    if opcion_jugador == 3 and opcion_cpu == 2:
        resultado_jugador = "tijera"

        resultado_cpu = "papel"
        victorias_jugador+=1
    else:
        victorias_cpu+=1
    print(f"Jugador: {resultado_jugador}. CPU: {resultado_cpu}. El resultado es {resultado}")
print()
print("Saliendo del programa...")