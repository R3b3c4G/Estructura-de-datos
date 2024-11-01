'''
Nombre: Rebeca Gregorio Espina.
Fecha: 3 de noviembre de 2024.
Descripción:
Este programa imprime en consola los números, separados por comas, del 1 hasta un número ingresado por el usuario.
Sin embargo, se deben sustituir los siguientes valores:
    3 o sus múltiplos por la palabra "Licenciatura".
    5 y sus múltiplos por la palabra "Informática".
    Múltiplos de 3 y 5 por la frase "Licenciatura en Informática" y se imprima un salto de línea en lugar de la coma.

INSTRUCCIONES:
Escribe un programa de nombre Ejercicio1_lic_informatica.py y sube el enlace de GitHub.
Para ello:
    a) Solicite un número en consola.
    b) Realizar la lógica adecuada para imprimir los números o mensajes adecuados.
    c) Mostrar los resultados en consola.
'''
print("***  Licenciatura en Informática ***")
# a) Solicite un número en consola.
numero_final=int(input("Ingrese el número final de la cuenta: "))
# b) Realizar la lógica adecuada para imprimir los números o mensajes adecuados.
contador=1
while contador <= numero_final:
    if contador % 3 == 0 and contador% 5 == 0:  # sustitución de múltiplos de 3 y 5 por la frase "Licenciatura en Informática" y se imprima un salto de línea en lugar de la coma.
        print("Licenciatura en Informática")
    elif contador % 3 == 0:             # Sustitución de 3 o sus múltiplos por la palabra "Licenciatura".
        print("Licenciatura", end = ", ")
    elif contador % 5 == 0:             # Sustitución de 5 y sus múltiplos por la palabra "Informática".
        print("Informática", end = ", ")
    else:
        print(contador, end=", ")
    contador+=1
print("\n\nSaliendo del programa...")
# c) Mostrar los resultados en consola.
"""
# Resultados en consola:
    ***  Licenciatura en Informática ***
    Ingrese el número final de la cuenta: 16
    1, 2, Licenciatura, 4, Informática, Licenciatura, 7, 8, Licenciatura, Informática, 11, Licenciatura, 13, 14, Licenciatura en Informática
    16, 
    
    Saliendo del programa...
    
        ***  Licenciatura en Informática ***
    Ingrese el número final de la cuenta: 12
    1, 2, Licenciatura, 4, Informática, Licenciatura, 7, 8, Licenciatura, Informática, 11, Licenciatura, 
    
    Saliendo del programa...

    ***  Licenciatura en Informática ***
    Ingrese el número final de la cuenta: 125
    1, 2, Licenciatura, 4, Informática, Licenciatura, 7, 8, Licenciatura, Informática, 11, Licenciatura, 13, 14, Licenciatura en Informática
    16, 17, Licenciatura, 19, Informática, Licenciatura, 22, 23, Licenciatura, Informática, 26, Licenciatura, 28, 29, Licenciatura en Informática
    31, 32, Licenciatura, 34, Informática, Licenciatura, 37, 38, Licenciatura, Informática, 41, Licenciatura, 43, 44, Licenciatura en Informática
    46, 47, Licenciatura, 49, Informática, Licenciatura, 52, 53, Licenciatura, Informática, 56, Licenciatura, 58, 59, Licenciatura en Informática
    61, 62, Licenciatura, 64, Informática, Licenciatura, 67, 68, Licenciatura, Informática, 71, Licenciatura, 73, 74, Licenciatura en Informática
    76, 77, Licenciatura, 79, Informática, Licenciatura, 82, 83, Licenciatura, Informática, 86, Licenciatura, 88, 89, Licenciatura en Informática
    91, 92, Licenciatura, 94, Informática, Licenciatura, 97, 98, Licenciatura, Informática, 101, Licenciatura, 103, 104, Licenciatura en Informática
    106, 107, Licenciatura, 109, Informática, Licenciatura, 112, 113, Licenciatura, Informática, 116, Licenciatura, 118, 119, Licenciatura en Informática
    121, 122, Licenciatura, 124, Informática, 
    
    Saliendo del programa...

"""