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

def menu ():    # Función para imprimir menú y retornar la opción del usuario.
    print("***  Valor máximo y mínimo de una lista de números del usuario  ***")
    print("[1].- Ver lista de números.")
    print("[2].- Añadir número a la lista.")
    print("[3].- Determinar el valor máximo y mínimo de la lista de números.")
    print("[0].- Salir.")
    opcion = int(input("Elige una opción: "))
    return opcion

def mostrar_lista (lista):  # Función para mostrar lista de números.
        print(f"La lista de numeros es: {lista}")

def añadir_numero (lista):  # Función para añadir números a la lista.
        print()
        mi_numero = int(input("Ingresa el número a la lista: "))
        lista.append(mi_numero)
        print(f"¡El número {mi_numero} se agregó con éxito!")

def maximo_minimo (lista):  # Función para determinar el número máximo y minímo de lista de números.
    tupla = (lista)
    maximo = tupla [0]
    minimo = tupla [0]
    for a in tupla:
        if a > maximo:
            maximo = a
        if a < minimo:
            minimo = a
    print(f"El valor máximo es: {maximo}")
    print(f"El valor minímo es: {minimo}")

opcion = None
lista = []
tupla = ()
opcion = menu()
while opcion != 0 :
    print()
    if 0 <= opcion <=3:
        if opcion == 1:
            if len(lista) == 0:
                print("No hay números para mostrar.")
            else:
                mostrar_lista(lista)
        elif opcion == 2:
            añadir_numero(lista)
        elif opcion == 3:
            if len(lista) == 0:
                print("No hay números para mostrar.")
            else:
                maximo_minimo(lista)
        print("-------------------------\n")
    else:
        print("Opción no válida\n")
        print("-------------------------\n")
    opcion = menu()
print("Fin del programa.")
