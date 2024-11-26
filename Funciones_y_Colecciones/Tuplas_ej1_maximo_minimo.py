'''
Nombre:
Fecha:
Descripción:
Este programa muestra el valor máximo y mínimo de una lista de números. En este caso, la tupla se utiliza para devolver los valores máximo y mínimo de la función.

INSTRUCCIONES:
Escribe un programa de nombre Tuplas_ej1_maximo_minimo.py que realice lo siguiente:
    Se debe mostrar el siguiente menú:
      ***  Valor máximo y mínimo de una lista de números del usuario  ***
    1) Ver lista de números.
    2) Añadir número a la lista.
    3) Determinar el valor máximo y mínimo de la lista de números.
    0) Salir.
Cualquier otro caso -> Opción no válida.
Para ello:
    a) Se sugiere utilizar una función para mostrar el menú.
    b) Se debe utilizar una única función para devolver el valor máximo y mínimo en una tupla.
'''


opcion = None
def menu ():
    print("[1].- Ver lista de números.")
    print("[2].- Añadir número a la lista.")
    print("[3].- Determinar el valor máximo y mínimo de la lista de números.")
    print("[0].- Salir.")

def valor ():
    opcion = menu()
    if opcion == 1:     # Ver lista de números.
        if len(tupla) != 0:
            for a in mi_numero:
                print(a)
        else:
            print("No hay números a mostrar.")
    if opcion == 2:     # Añadir número a la lista.
        print()
        mi_numero = int(input("Ingresa el número a la lista. "))
        tupla = (mi_numero)
        print(f"¡El número {mi_numero} se agregó con éxito!")

    if opcion == 3:     # Determinar el valor máximo y mínimo de la lista de números.
        if len(tupla) != 0:
            maximo = tupla [0]
            minimo = tupla [0]
            for a in mi_numero:
                if a > maximo
                    maximo = a
                if a < minimo
                    minimo = a
        else:
            print("No hay números.")

    if opcion == 0:
        print("Saliendo del programa.")
    else:
        print("Opción no válida.")

print("***  Valor máximo y mínimo de una lista de números del usuario  ***")
while opcion != 0 :
    menu()
    opcion = int(input("Elige una opción: "))
    print(valor)
    print("-------------------------")
