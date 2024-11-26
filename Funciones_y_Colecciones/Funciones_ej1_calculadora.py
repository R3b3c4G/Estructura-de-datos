'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa es la versión del ejercicio Ciclos_ej3_calculadora.py, pero ahora utilizando funciones.

INSTRUCCIONES:
Escribe un programa de nombre Funciones_ej1_calculadora.py que siga mostrando el mismo menú y realice lo siguiente:
    1) Suma.
    2) Resta.
    3) Multiplicación.
    4) División.
    5) División entera.
    6) Exponenciación.
    0) Salir.
    Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
Para ello:
    a) En el código a nivel de módulo, utilice el ciclo en donde se está ejecutando el programa.
    b) Defina una función para el menú y devuelva la opción seleccionada por el usuario.
    c) Defina una función en donde los parámetros sean la opción y los números, devolviendo el resultado.
    d) Muestre el resultado en pantalla.
'''
opcion = None   # None es una palabra reservada que se utiliza para definir un valor nulo o ningún valor.
# def es una palabra reservada que se utiliza para definir una función.
# b) Defina una función para el menú y devuelva la opción seleccionada por el usuario.
def menu ():    # Función para imprimir menú y devolver opción del usuario.
    print("     [1].- Suma.")
    print("     [2].- Resta.")
    print("     [3].- Multiplicación.")
    print("     [4].- División.")
    print("     [5].- División entera.")
    print("     [6].- Potenciación.")
    print("     [0].- Salir.")
    opcion = int(input("\nElige una opción del menú anterior: "))
    return opcion

# Función para realizar los  cálculos.
def calculadora (opcion, numero1, numero2): # c) Defina una función en donde los parámetros sean la opción y los números, devolviendo el resultado.
    if opcion == 1: # Suma.
        resultado = numero1 + numero2
    elif opcion == 2:   # Resta.
        resultado= numero1 - numero2
    elif opcion == 3:   # Multiplicación.
        resultado = numero1 * numero2
    elif opcion == 4:   # División.
        resultado = numero1 / numero2
    elif opcion == 5:   # División entera.
        resultado = numero1 // numero2
    elif opcion == 6:   # Potenciación.
        resultado = numero1 ** numero2
    return resultado    # Después de verificar qué caso aplica, se regresa a la función principal el resultado de la operación.

# a) En el código a nivel de módulo, utilice el ciclo en donde se está ejecutando el programa.
while opcion != 0:  #  e) Repita el menú anterior.
    print("***  Calculadora básica  ***")
    opcion = menu()  # a) Muestre el menú.
    if opcion <= 6 and opcion >= 0:
        if opcion != 0:  # b) Si la opción seleccionada fue entre 1 y 6, solicite dos números al usuario.
            print()
            numero1 = float(input("Ingresa un número: "))
            numero2 = float(input("Ingresa otro número: "))
            # Mando a llamar a la función calculadora con el argumento opcion, numero1 y numero2.
            print(f"\nEl resultado es: {calculadora(opcion, numero1, numero2):.2f}")   # d) Muestre el resultado en pantalla.
            print("----------------------------------\n")
    else:
        print("\nOpción no válida.") # Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
        print("----------------------------------\n")
print("\nFin del programa.")
print("----------------------------------\n")
"""
# Resultado en consola:
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].- Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 1
    
    Ingresa un número: 32.1
    Ingresa otro número: 78
    
    El resultado es: 110.10
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].- Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 2
    
    Ingresa un número: 110.1
    Ingresa otro número: 32.1
    
    El resultado es: 78.00
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].- Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 3
    
    Ingresa un número: 80
    Ingresa otro número: 90
    
    El resultado es: 7200.00
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].- Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 4
    
    Ingresa un número: 7200
    Ingresa otro número: 80
    
    El resultado es: 90.00
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].- Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 7190
    
    Opción no válida.
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].- Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 80
    
    Opción no válida.
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].- Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 5
    
    Ingresa un número: 7190
    Ingresa otro número: 80
    
    El resultado es: 89.00
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].- Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 6
    
    Ingresa un número: 3
    Ingresa otro número: 3
    
    El resultado es: 27.00
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].- Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 0
    
    Fin del programa.
    ----------------------------------
"""
