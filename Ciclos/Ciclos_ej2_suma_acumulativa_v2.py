'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa calculará la suma acumulativa de dos números ingresados por el usuario.
A diferencia del programa anterior, ahora el usuario también definirá el número inicial.

INSTRUCCIONES:
Escribe un programa de nombre Ciclos_ej2_suma_acumulativa_v2.py que realice lo siguiente:
    a) Solicite al usuario los números inicial y final de la suma acumulativa.
    b) Calcule la suma acumulativa entre ambos números.
    c) Muestre el resultado de la suma.
'''
contador = 0
resultado = 0
print("***  Programa que calcula la suma acumulativa entre dos números   ***")
numero_inicial = int(input("Ingresa el número inicial de la cuenta: ")) # a) Solicite al usuario el número inicial de la suma acumulativa.
numero_final = int(input("Ingresa el número final de la cuenta: ")) # a) Solicite al usuario el número final de la suma acumulativa.
contador = numero_inicial
if numero_inicial < numero_final: # Lo solicitado para este programa solo se hará si el número inicial es menor que el número final.
    while contador<=numero_final:
        resultado = resultado + contador    # b) Calcule la suma acumulativa entre ambos números.
        contador+=1
    print()
    print(f"La suma de {numero_inicial} hasta {numero_final} es: {resultado}.") # c) Muestre el resultado de la suma.
else:
    print("\nNo se pudo realizar la suma acumulativa.")
"""
# Resultado en consola:
    ***  Programa que calcula la suma acumulativa entre dos números   ***
    Ingresa el número inicial de la cuenta: -10
    Ingresa el número final de la cuenta: -9
    
    La suma de -10 hasta -9 es: -19.
    
    
    ***  Programa que calcula la suma acumulativa entre dos números   ***
    Ingresa el número inicial de la cuenta: -10
    Ingresa el número final de la cuenta: 0
    
    La suma de -10 hasta 0 es: -55.
    
    
    ***  Programa que calcula la suma acumulativa entre dos números   ***
    Ingresa el número inicial de la cuenta: 0
    Ingresa el número final de la cuenta: 55
    
    La suma de 0 hasta 55 es: 1540.
    
    
    ***  Programa que calcula la suma acumulativa entre dos números   ***
    Ingresa el número inicial de la cuenta: 0
    Ingresa el número final de la cuenta: 10
    
    La suma de 0 hasta 10 es: 55.


    ***  Programa que calcula la suma acumulativa entre dos números   ***
    Ingresa el número inicial de la cuenta: -10
    Ingresa el número final de la cuenta: 10
    
    La suma de -10 hasta 10 es: 0.  
    
    
    ***  Programa que calcula la suma acumulativa entre dos números   ***
    Ingresa el número inicial de la cuenta: 7
    Ingresa el número final de la cuenta: 4
    
    No se pudo realizar la suma acumulativa.
"""
