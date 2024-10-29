'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Este programa determinará cuál de dos números ingresados por el usuario es menor o si son iguales.

INSTRUCCIONES:
Escribe un programa de nombre Sentencias_ejercicio1.py que realice lo siguiente:
    a) Solicite al usuario dos números decimales.
    b) Utilice la lógica adecuada para determinar cuál de los dos números es menor o si es que son iguales.
    c) Muestre el número menor (o que son iguales) en consola.
'''
# a) Solicite al usuario dos números decimales.
numero1 = float(input("Ingresa un número decimal: "))
numero2 = float(input("Ingresa otro número decimal: "))
print()
# b) Utilice la lógica adecuada para determinar cuál de los dos números es menor o si es que son iguales.
if numero1 > numero2:
    resultado = (f"El número {numero2} es menor que {numero1}.")
elif numero1<numero2:
    resultado = (f"El número {numero1} es menor que {numero2}.")
else:
    resultado = (f"El número {numero1} y {numero2} son iguales.")


# c) Muestre el número menor (o que son iguales) en consola.
print(f"{resultado}")
"""
# Resultado en consola:
    # 
    Ingresa un número decimal: 20.2
    Ingresa otro número decimal: 20.2
    
    El número 20.2 y 20.2 son iguales.
    
    #
    Ingresa un número decimal: -16.2
    Ingresa otro número decimal: -21.2
    
    El número -21.2 es menor que -16.2.

    #
    Ingresa un número decimal: -21.2
    Ingresa otro número decimal: -16.2
    
    El número -21.2 es menor que -16.2.
"""