'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa es una calculadora básica.

INSTRUCCIONES:
Escribe un programa de nombre Ciclos_ej3_calculadora.py que realice lo siguiente:
    1) Suma.
    2) Resta.
    3) Multiplicación.
    4) División.
    5) División entera.
    6) Exponenciación.
    0) Salir.
    Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
Para ello:
    a) Muestre el menú.
    b) Si la opción seleccionada fue entre 1 y 6, solicite dos números al usuario.
    c) Calcule el resultado de acuerdo a la opción.
    d) Muestre el resultado en pantalla.
    e) Repita el menú anterior.
'''
opcion = None   # None es una palabra reservada que se utiliza para definir un valor nulo o ningún valor.
# def es una palabra reservada que se utiliza para definir una función.
# Función para imprimir menú.
def menu ():
    print("     [1].- Suma.")
    print("     [2].- Resta.")
    print("     [3].- Multiplicación.")
    print("     [4].- División.")
    print("     [5].- División entera.")
    print("     [6].-Potenciación.")
    print("     [0].- Salir.")

# Función para realizar los  cálculos.
def calculadora (opcion, numero1, numero2): # c) Calcule el resultado de acuerdo con la opción.
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

while opcion != 0:  #  e) Repita el menú anterior.
    print("***  Calculadora básica  ***")
    menu()  # a) Muestre el menú.
    print()
    opcion = int(input("Elige una opción del menú anterior: "))
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
print("\nSaliendo...")
print("----------------------------------\n")

"""
# Resultado en consola:
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].-Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 1
    
    Ingresa un número: 12.1
    Ingresa otro número: 2.3
    
    El resultado es: 14.40
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].-Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 2
    
    Ingresa un número: 1
    Ingresa otro número: -1.3
    
    El resultado es: 2.30
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].-Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 3
    
    Ingresa un número: -2.1
    Ingresa otro número: 2
    
    El resultado es: -4.20
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].-Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 4
    
    Ingresa un número: 10
    Ingresa otro número: 3
    
    El resultado es: 3.33
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].-Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 5
    
    Ingresa un número: 10
    Ingresa otro número: 3
    
    El resultado es: 3.00
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].-Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 6
    
    Ingresa un número: 2
    Ingresa otro número: 3
    
    El resultado es: 8.00
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].-Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 1234
    
    Opción no válida.
    ----------------------------------
    
    ***  Calculadora básica  ***
         [1].- Suma.
         [2].- Resta.
         [3].- Multiplicación.
         [4].- División.
         [5].- División entera.
         [6].-Potenciación.
         [0].- Salir.
    
    Elige una opción del menú anterior: 0
    
    Saliendo...
    ----------------------------------

"""


