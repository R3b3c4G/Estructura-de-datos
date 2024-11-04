'''
Nombre: Rebeca Gregorio Espina.
Fecha: 3 de noviembre de 2024.
Descripción:
Este programa es un juego en donde el usuario intente adivinar un número secreto.

INSTRUCCIONES:
Escribe un programa de nombre Ejercicio4_juego_adivinador.py y sube el enlace de GitHub.
Para ello:
    a) El número a adivinar es un número aleatorio entre 1 y 100.
    b) El jugador tendrá 5 intentos para encontrar el número.
    c) Como pista, el juego indicará si el número a adivinar es menor o mayor al número ingresado, si el número no es el correcto.
    d) Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.
    e) Si el jugador no adivina el número, el juego muestra un mensaje con el número.
'''
from random import randint
print("***  Juego del adivinador ***")
#  a) El número a adivinar es un número aleatorio entre 1 y 100.
adivinar_numero = randint(1,100)
# b) El jugador tendrá 5 intentos para encontrar el número.
intento=1
while intento < 6:
    mi_numero = int(input(f"Número de intento: {intento}. Ingresa un número (1-100): "))
    if mi_numero >=1 and mi_numero <= 100 : # Condición que verifica si el número ingresado está dentro del rango especificado.
    # c) Como pista, el juego indicará si el número a adivinar es menor o mayor al número ingresado, si el número no es el correcto.
        if adivinar_numero > mi_numero:
            print("El número a adivinar es mayor.")
        elif adivinar_numero < mi_numero:
            print("El número a adivinar es menor.")
        elif adivinar_numero == mi_numero:  # d) Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.
            print(f"\n¡Felicidades!, adivinaste en {intento} intentos.")
            break       # Al momento en que el jugador adivina, se detiene el ciclo.
        if intento == 5:
            print(f"\nPerdiste. El número era: {adivinar_numero}")# e) Si el jugador no adivina el número, el juego muestra un mensaje con el número.
        print()
    else:
        print("Su número no está dentro del rango, vuelva a intentar.")
        intento-=1
    intento+=1
print("\n\nSaliendo del programa...")

"""
# Resultados en consola:
    -Valor fuera del rango:
        ***  Juego del adivinador ***
    Número de intento: 1. Ingresa un número (1-100): 200
    Su número no está dentro del rango, vuelva a intentar.
    Número de intento: 1. Ingresa un número (1-100): -1
    Su número no está dentro del rango, vuelva a intentar.
    Número de intento: 1. Ingresa un número (1-100): 0
    Su número no está dentro del rango, vuelva a intentar.
    Número de intento: 1. Ingresa un número (1-100): 100
    El número a adivinar es menor.
    
    Número de intento: 2. Ingresa un número (1-100): 20
    El número a adivinar es mayor.
    
    Número de intento: 3. Ingresa un número (1-100): 45
    El número a adivinar es mayor.
    
    Número de intento: 4. Ingresa un número (1-100): 50
    El número a adivinar es mayor.
    
    Número de intento: 5. Ingresa un número (1-100): 54
    El número a adivinar es mayor.
    
    Perdiste. El número era: 67
    
    
    
    Saliendo del programa...
    
    _Número adivinado:
    ***  Juego del adivinador ***
    Número de intento: 1. Ingresa un número (1-100): 34
    El número a adivinar es mayor.
    
    Número de intento: 2. Ingresa un número (1-100): 76
    El número a adivinar es menor.
    
    Número de intento: 3. Ingresa un número (1-100): 56
    El número a adivinar es menor.
    
    Número de intento: 4. Ingresa un número (1-100): 43
    El número a adivinar es menor.
    
    Número de intento: 5. Ingresa un número (1-100): 37
    ¡Felicidades!, adivinaste en 5 intentos.
    
    
    Saliendo del programa...
"""