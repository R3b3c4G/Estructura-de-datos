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
while opcion != 0 : # e) Repita el menú.
    print("*** Calculadora básica***")  # a) Muestre el menú.
    print("[1].- Suma.")
    print("[2].- Resta.")
    print("[3].- Multiplicación.")
    print("[4].- División.")
    print("[5].- División entera.")
    print("[6].- Exponenciación.")
    print("[0].- Salir.")
    opcion = int(input("\nIngresa una opción del menú anterior: "))
    if opcion >= 0 and opcion <= 6: # Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
        if opcion >= 1 and opcion <= 6: # b) Si la opción seleccionada fue entre 1 y 6, solicite dos números al usuario.
            numero1 = float(input("\nIngrese el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))
            # c) Calcule el resultado de acuerdo a la opción.
            if opcion == 1:
                resultado = numero1 + numero2
            elif opcion == 2:
                resultado = numero1 - numero2
            elif opcion == 3:
                resultado = numero1 * numero2
            elif opcion == 4:
                resultado = numero1 / numero2
            elif opcion == 5:
                resultado = numero1 // numero2
            elif opcion == 6:
                resultado = numero1 ** numero2
            print(f"\nEl resultado es: {resultado:.2f}")  # d) Muestre el resultado en pantalla.
            print("----------------------------------------")
    else:
        print("\nOpción no válida.")
        print("----------------------------------------")
    print()
print("Saliendo...")
print("----------------------------------------")
"""
# Resultados en consola: 
    *** Calculadora básica***
    [1].- Suma.
    [2].- Resta.
    [3].- Multiplicación.
    [4].- División.
    [5].- División entera.
    [6].- Exponenciación.
    [0].- Salir.
    
    Ingresa una opción del menú anterior: 1
    
    Ingrese el primer número: 12.1
    Ingresa el segundo número: 2.3
    
    El resultado es: 14.40
    ----------------------------------------
    
    *** Calculadora básica***
    [1].- Suma.
    [2].- Resta.
    [3].- Multiplicación.
    [4].- División.
    [5].- División entera.
    [6].- Exponenciación.
    [0].- Salir.
    
    Ingresa una opción del menú anterior: 2
    
    Ingrese el primer número: 1
    Ingresa el segundo número: -1.3
    
    El resultado es: 2.30
    ----------------------------------------
    
    *** Calculadora básica***
    [1].- Suma.
    [2].- Resta.
    [3].- Multiplicación.
    [4].- División.
    [5].- División entera.
    [6].- Exponenciación.
    [0].- Salir.
    
    Ingresa una opción del menú anterior: 3
    
    Ingrese el primer número: -2.1
    Ingresa el segundo número: 2
    
    El resultado es: -4.20
    ----------------------------------------
    
    *** Calculadora básica***
    [1].- Suma.
    [2].- Resta.
    [3].- Multiplicación.
    [4].- División.
    [5].- División entera.
    [6].- Exponenciación.
    [0].- Salir.
    
    Ingresa una opción del menú anterior: 4
    
    Ingrese el primer número: 10
    Ingresa el segundo número: 3
    
    El resultado es: 3.33
    ----------------------------------------
    
    *** Calculadora básica***
    [1].- Suma.
    [2].- Resta.
    [3].- Multiplicación.
    [4].- División.
    [5].- División entera.
    [6].- Exponenciación.
    [0].- Salir.
    
    Ingresa una opción del menú anterior: 5
    
    Ingrese el primer número: 10
    Ingresa el segundo número: 3
    
    El resultado es: 3.00
    ----------------------------------------
    
    *** Calculadora básica***
    [1].- Suma.
    [2].- Resta.
    [3].- Multiplicación.
    [4].- División.
    [5].- División entera.
    [6].- Exponenciación.
    [0].- Salir.
    
    Ingresa una opción del menú anterior: 6
    
    Ingrese el primer número: 2
    Ingresa el segundo número: 3
    
    El resultado es: 8.00
    ----------------------------------------
    
    *** Calculadora básica***
    [1].- Suma.
    [2].- Resta.
    [3].- Multiplicación.
    [4].- División.
    [5].- División entera.
    [6].- Exponenciación.
    [0].- Salir.
    
    Ingresa una opción del menú anterior: 12
    
    Opción no válida.
    ----------------------------------------
    
    *** Calculadora básica***
    [1].- Suma.
    [2].- Resta.
    [3].- Multiplicación.
    [4].- División.
    [5].- División entera.
    [6].- Exponenciación.
    [0].- Salir.
    
    Ingresa una opción del menú anterior: 0
    
    Saliendo...
    ----------------------------------------

"""


