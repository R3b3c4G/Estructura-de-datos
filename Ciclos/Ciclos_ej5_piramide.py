'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa imprime una pirámide de caracteres '*' de cuatro formas:
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

INSTRUCCIONES:
Escribe un programa de nombre Ciclos_ej5_piramide.py que realice lo siguiente:
    a) Solicite el número de filas de la pirámide.
    b) Muestre los cuatro tipos de pirámides utilizando la lógica adecuada.
'''
filas = int(input("Ingresa el número de filas de la pirámide: "))   # a) Solicite el número de filas de la pirámide.
# b) Muestre los cuatro tipos de pirámides utilizando la lógica adecuada.
print()
print("Forma 1:")
for i in range(1, filas + 1):   # Conforme va iterando, aumenta a 1 el número de asteriscos en los renglones siguientes.
    asterisco = "*" * i
    print(f"{asterisco}")
print("---------------------\n")
print("Forma 2:")
contador = filas
for i in range(1,filas + 1):    # Imprime el primer renglón de asterisco según el número de filas y en los siguientes renglones, va disminuyendo en 1.
    asterisco = "*" * contador
    print(f"{asterisco}")
    contador -= 1
print("---------------------\n")
print("Forma 3:")
for i in range(1, filas + 1):
    espacio = " " * (filas - i) # El espacio se imprime según el número de fila menos la iteración y va aumentando conforme avanzan los renglones.
    asterisco = "*" * ((2 * i) - 1) # Los asteriscos van aumentando de manera impar, con el objetivo de que queden centrados.
    print(f"{espacio}{asterisco}")
print("---------------------\n")
print("Forma 4:")
contador = filas - 1
for i in range(1, filas + 1):
    asterisco = "*" * i # El asterisco aumenta a 1.
    espacio = " " * contador    # Imprime el primer renglón de espacios según el número de filas y en las siguientes iteraciones disminuye a 1 el número de espacios en los renglones siguientes.
    print(f"{espacio}{asterisco}")
    contador -= 1
print("---------------------\n")
"""
# Resultados en consola:
    Ingresa el número de filas de la pirámide: 1
    
    Forma 1:
    *
    ---------------------
    
    Forma 2:
    *
    ---------------------
    
    Forma 3:
    *
    ---------------------
    
    Forma 4:
    *
    ---------------------
    
    Ingresa el número de filas de la pirámide: 2
    
    Forma 1:
    *
    **
    ---------------------
    
    Forma 2:
    **
    *
    ---------------------
    
    Forma 3:
     *
    ***
    ---------------------
    
    Forma 4:
     *
    **
    ---------------------
    
    Ingresa el número de filas de la pirámide: 5
    
    Forma 1:
    *
    **
    ***
    ****
    *****
    ---------------------
    
    Forma 2:
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
    ---------------------
    
    Forma 4:
        *
       **
      ***
     ****
    *****
    ---------------------
    
    Ingresa el número de filas de la pirámide: 20
    
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
    ***********
    ************
    *************
    **************
    ***************
    ****************
    *****************
    ******************
    *******************
    ********************
    ---------------------
    
    Forma 2:
    ********************
    *******************
    ******************
    *****************
    ****************
    ***************
    **************
    *************
    ************
    ***********
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
             *********************
            ***********************
           *************************
          ***************************
         *****************************
        *******************************
       *********************************
      ***********************************
     *************************************
    ***************************************
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
             ***********
            ************
           *************
          **************
         ***************
        ****************
       *****************
      ******************
     *******************
    ********************
    ---------------------
"""