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
opcion = None
# def es una palabra reservada que se utiliza para definir una función.
# Función para imprimir menú.
def menu ():
    print("[1].- Suma.")
    print("[2].- Resta.")
    print("[3].- Multiplicación.")
    print("[4].- División.")
    print("[5].- División entera.")
    print("[6].- Módulo.")
    print("[7].-Potenciación.")
    print("[0].- Salir.")

# Función para realizar los  calculos.
def calculadora (opcion, numero1, numero2): # c) Calcule el resultado de acuerdo a la opción.
    if opcion == 1: # Suma.
        resultado = numero1 + numero2
    elif opcion == 2:   # Resta.
        resultado= numero1 - numero2
    elif opcion == 3:   # Multiplicación.
        resultado = numero1 * numero2
    elif opcion == 4:   # División.
        if numero2 == 0:
            return "No es válido una división entre 0." # Si el segundo valor es 0, no llega a realizarse la operación y se regresa un letrero.
        resultado = numero1 / numero2
    elif opcion == 5:   # División entera.
        if numero2 == 0:
            return "No es válido una división entre 0." # # Si el segundo valor es 0, no llega a realizarse la operación y se regresa un letrero.
        resultado = numero1 // numero2
    elif opcion == 6:   # Módulo.
        resultado = numero1 % numero2
    elif opcion == 7:   # Potenciación.
        resultado = numero1 ** numero2
    return resultado    # Después de verificar que caso aplica, se regresa a la función principal el resultado de la operación.

while opcion != 0:
    menu()  # a) Muestre el menú.
    print()
    opcion = int(input("Ingresa una de las opciones: "))
    if opcion <= 6 and opcion >= 0:
        if opcion != 0:  # b) Si la opción seleccionada fue entre 1 y 6, solicite dos números al usuario.
            numero1 = int(input("Ingresa un número: "))
            numero2 = int(input("Ingresa otro número: "))
            # Mando a llamar a la función calculadora con el argumento opcion, numero1 y numero2.
            print("\nEl resultado es:",calculadora(opcion, numero1, numero2))   # d) Muestre el resultado en pantalla.
            print("----------------------------------------")
            print()
    else:
        print("\nOpción no válida.") # Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
print("\nSaliendo del programa...")


