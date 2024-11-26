'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa imprime una pirámide de caracteres '*' de cuatro formas y es la versión del ejercicio Ciclos_ej5_piramide.py, pero ahora utilizando funciones.

INSTRUCCIONES:
Escribe un programa de nombre Funciones_ej2_piramide.py que realice lo siguiente:
Cada pirámide debe estar en una función, la cual se llama en el código a nivel de módulo de acuerdo a las filas requeridas por el usuario.
    1)
    *
    **
    ***

    2)
    ***
    **
    *

    3)
      *
     ***
    *****

    4)
      *
     **
    ***
Para ello:
    a) Solicite el número de filas de la pirámide en el código a nivel de módulo.
    b) Defina una función para cada pirámide, recibiendo el número de filas como parámetro.
'''
def forma1 (filas):  # b) Defina una función para cada pirámide, recibiendo el número de filas como parámetro.
    for i in range(1, filas + 1):  # Conforme va iterando, aumenta a 1 el número de asteriscos en los renglones siguientes.
        print(f"{"*" * i}")
def forma2 (filas):
    contador = filas
    for i in range(1, filas + 1):  # Imprime el primer renglón de asterisco según el número de filas y en los siguientes renglones, va disminuyendo en 1.
        print(f"{"*" * contador}")
        contador -= 1
def forma3 (filas):
    for i in range(1, filas + 1):
        espacio = " " * (filas - i)  # El espacio se imprime según el número de fila menos la iteración y va aumentando conforme avanzan los renglones.
        asterisco = "*" * ((2 * i) - 1)  # Los asteriscos van aumentando de manera impar, con el objetivo de que queden centrados.
        print(f"{espacio}{asterisco}")
def forma4 (filas):
    contador = filas - 1
    for i in range(1, filas + 1):
        asterisco = "*" * i  # El asterisco aumenta a 1.
        espacio = " " * contador  # Imprime el primer renglón de espacios según el número de filas y en las siguientes iteraciones disminuye a 1 el número de espacios en los renglones siguientes.
        print(f"{espacio}{asterisco}")
        contador -= 1
# Código principal.
filas = int(input("Ingresa el número de filas de la pirámide: "))   # a) Solicite el número de filas de la pirámide en el código a nivel de módulo.
print("\nForma 1:")
forma1(filas)
print("---------------------\n")
print("Forma 2:")
forma2(filas)
print("---------------------\n")
print("Forma 3:")
forma3(filas)
print("---------------------\n")
print("Forma 4:")
forma4(filas)
print("---------------------\n")

"""
# Resultados en consola:
    Ingresa el número de filas de la pirámide: 4
    
    Forma 1:
    *
    **
    ***
    ****
    ---------------------
    
    Forma 2:
    ****
    ***
    **
    *
    ---------------------
    
    Forma 3:
       *
      ***
     *****
    *******
    ---------------------
    
    Forma 4:
       *
      **
     ***
    ****
    ---------------------

Ingresa el número de filas de la pirámide: 10

Forma 1:
*
**
***
****
*****
******
*******
********
*********
**********
---------------------

Forma 2:
**********
*********
********
*******
******
*****
****
***
**
*
---------------------

Forma 3:
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
---------------------

Forma 4:
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
---------------------

Ingresa el número de filas de la pirámide: 6

Forma 1:
*
**
***
****
*****
******
---------------------

Forma 2:
******
*****
****
***
**
*
---------------------

Forma 3:
     *
    ***
   *****
  *******
 *********
***********
---------------------

Forma 4:
     *
    **
   ***
  ****
 *****
******
---------------------
"""

