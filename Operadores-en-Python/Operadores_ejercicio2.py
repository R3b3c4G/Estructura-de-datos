"""
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Este programa determinará si una persona forma parte de la comunidad de la UNSIJ.

INSTRUCCIONES:
Escribe un programa de nombre Operadores_ejercicio2.py que realice lo siguiente:
    a) Pregunte al usuario si es profesor de la UNSIJ (Si/No).
    b) Pregunte al usuario si es alumno de la UNSIJ (Si/No).
    c) La persona forma parte de la UNSIJ si es profesor o alumno de la UNSIJ.
    d) Muestre el resultado en consola como valor booleano (True/False).
Nota: Prueba con todos los casos posibles.
"""
# a) Pregunte al usuario si es profesor de la UNSIJ (Si/No).
respuesta1=input("¿Es profesor de la UNSIJ?: ")
# Conversión de la cadena a minúscula.
respuesta1=respuesta1.lower()=="si"
# b) Pregunte al usuario si es alumno de la UNSIJ (Si/No).
respuesta2=input("¿Es estudiante de la UNSIJ?: ")
respuesta2=respuesta2.lower()=="si"
print()
# c) La persona forma parte de la UNSIJ si es profesor o alumno de la UNSIJ.
print(f"Forma parte de la comunidad UNSIJ: {respuesta1 or respuesta2}.")

"""
Casos posibles, resultado en consola:
#
    ¿Es profesor de la UNSIJ?: No
    ¿Es estudiante de la UNSIJ?: No
    
    Forma parte de la comunidad UNSIJ: False.

#
    ¿Es profesor de la UNSIJ?: Si
    ¿Es estudiante de la UNSIJ?: No
    
    Forma parte de la comunidad UNSIJ: True.

#
    ¿Es profesor de la UNSIJ?: No
    ¿Es estudiante de la UNSIJ?: Si
    
    Forma parte de la comunidad UNSIJ: True.
"""
