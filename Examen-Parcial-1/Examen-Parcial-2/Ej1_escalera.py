'''
Nombre: Rebeca Gregorio Espina.
Fecha: 8 de diciembre del 2024.
Descripción:
Este programa dibuja una escalera, en donde el usuario ingresa el número de escalones.
Si el número es positivo, la escalera será ascendente.
Un ejemplo cuando se ingresa un valor de 4:
        _
      _|
    _|
  _|
_|

Si el número es negativo, la escalera será descendente. Un ejemplo cuando se ingresa un valor de -4:
_
 |_
   |_
     |_
       |_

Si el número es cero, se deberá salir del programa.

INSTRUCCIONES:
Escribe un programa de nombre Ej1_escalera.py que realice lo que se indica en la descripción del programa.
Se debe mostrar la siguiente pantalla:
      ***  Ejercicio 1. La escalera.  ***
    Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:
    Cualquier otro caso -> Opción no válida.

Para ello:
    a) Solicite el número de escalones utilizando un ciclo.
    b) Muestre la escalera utilizando la lógica adecuada. Se requiere utilizar funciones para dibujar las escaleras para considerar el ejercicio como completo.
'''


def menu():     # Función que imprime el menú y regresa la opción del usuario (número de escalones o salir).
    print("***  Ejercicio 1. La escalera.  ***")
    opcion = int(input(f"Ingresa el número de escalones (positivo - ascendente y negativo - descendente) o ingresa un cero para salir:  "))
    return opcion

def ascendente(opcion):     # Función que imprime escaleras para números positivos.
    print("  " * (opcion),"_")
    for a in range(opcion):
        espacio = "  " * (opcion - 1 - a)   # Espacios antes de cada escalón.
        escalon ="_|"
        print(espacio,escalon)

def descendente(opcion):    # Función que imprime escaleras para números negativos.
    print("_")
    for b in range(-opcion):    # Al ser un número negativo, se le agrega un signo menos para que se vuelva positivo y así el for pueda iterar.
        espacio = "  " * b  # Espacios antes de cada escalón.
        escalon = "|_"
        print(espacio,escalon)


opcion = menu()
while opcion != 0:  # Mientras el usuario no quiera salir.
    if opcion > 0:
        ascendente(opcion)  # Escalera ascendente.
    elif opcion < 0:
        descendente(opcion) # Escalera descendente.
    elif opcion == 0:
        print("\nFin del programa.")
    print("--------------------------------------------------\n")
    opcion = menu()
# Nota: En esta ocasión no puse una condición no válida, debido a que todos los números enteros son válidos y si se ingresa otro valor, de por sí habrá un error durante la ejecución del código.

