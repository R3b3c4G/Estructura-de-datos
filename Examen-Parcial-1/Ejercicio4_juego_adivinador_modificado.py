'''
Nombre: Rebeca Gregorio Espina.
Fecha: 4 de noviembre de 2024.
Descripción:
Este programa es un juego en donde el usuario intente adivinar un número secreto.

INSTRUCCIONES:
Para ello:
-Solicitar inicialmente en nivel de dificultad.
    [F].- 10 intentos y números entre 1-50.
    [M].- 5 intentos y numeros entre 1-100.
    [D].- 4 intentos y números entre 1-110.
-Como pista, el juego indicará si el número a adivinar es menor o mayor al número ingresado, si el número no es el correcto.
-Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.
-Si el jugador no adivina el número, el juego muestra un mensaje con el número.
'''
from random import randint
print("***  Juego del adivinador ***")
print("[F].- 10 intentos y números entre 1-50.")
print("[M].- 5 intentos y números entre 1-100.")
print("[D].- 4 intentos y números entre 1-110.")
nivel_dificultad = input("Ingrese el nivel de dificultad del juego: ")
nivel_dificultad = nivel_dificultad.lower()
if nivel_dificultad == "f": # Nivel fácil.
    intento = 10    # El jugador tendrá 10 intentos para encontrar el número.
    rango = "(1-50)"
    adivinar_numero = randint(1,50) # El número a adivinar es un número aleatorio entre 1 y 50.
if nivel_dificultad == "m": # Nivel medio.
    intento = 5     # El jugador tendrá 5 intentos para encontrar el número.
    rango = "(1-100)"
    adivinar_numero = randint(1,100)    # El número a adivinar es un número aleatorio entre 1 y 100.
if nivel_dificultad == "d": # Nivel difícil..
    intento = 4         # El jugador tendrá 4 intentos para encontrar el número.
    rango = "(1-110)"
    adivinar_numero = randint(1,110)    # El número a adivinar es un número aleatorio entre 1 y 110.
contador=1
while contador < intento + 1:
    mi_numero = int(input(f"Número de intento: {contador}. Ingresa un número {rango}: "))
    if adivinar_numero > mi_numero:
        print("El número a adivinar es mayor.")
    elif adivinar_numero < mi_numero:
        print("El número a adivinar es menor.")
    elif adivinar_numero == mi_numero:  # Si el jugador adivina el número, el juego muestra un mensaje de felicitación y el número de intentos.
        print(f"\n¡Felicidades!, adivinaste en {contador} intentos.")
        break       # Al momento en que el jugador adivina, se detiene el ciclo.
    if contador == intento:
        print(f"\nPerdiste. El número era: {adivinar_numero}")# Si el jugador no adivina el número, el juego muestra un mensaje con el número.
        print()
    contador+=1
print("\n\nFin del juego")
