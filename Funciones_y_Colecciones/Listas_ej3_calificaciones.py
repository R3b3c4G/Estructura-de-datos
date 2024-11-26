'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa es una lista de las calificaciones de los alumnos del Parcial 1. La lista está conformada por
el nombre del alumno y sus calificaciones.

INSTRUCCIONES:
Escribe un programa de nombre Listas_ej3_calificaciones.py que realice lo siguiente:
Cada alumno tiene 5 calificaciones: estructuras de datos, derecho, contabilidad, álgebra y electrónica.

Se debe mostrar el siguiente menú:
      ***  Calificaciones del Parcial 1  ***
    1) Ver calificaciones de todos los alumnos.
    2) Ver calificaciones detalladas de un alumno.
    3) Ver promedios del Parcial 1 de todos los alumnos.
    4) Ver promedio grupal del Parcial 1.
    5) Agregar alumno y sus calificaciones.
    6) Eliminar alumno y sus calificaciones.
    0) Salir.
    Cualquier otro caso -> Opción no válida.

Para ello:
    a) Se sugiere utilizar funciones para modular el código.
    b) Se sugiere utilizar listas para las cinco calificaciones, los nombres y las calificaciones de los alumnos.
    c) Todas las calificaciones y promedios se deben mostrar únicamente con un decimal.
'''
def menu ():    # Función para imprimir menú y devolver opción del usuario.
    print("***  Calificaciones del Parcial 1  ***")
    print("     [1].- Ver calificaciones de todos los alumnos.")
    print("     [2].- Ver calificaciones detalladas de un alumno.")
    print("     [3].- Ver promedios del Parcial 1 de todos los alumnos.")
    print("     [0].- Ver promedio grupal del Parcial 1.")
    print("     [0].- Agregar alumno y sus calificaciones.")
    print("     [0].- Eliminar alumno y sus calificaciones.")
    print("     [0].- Salir")
    opcion = int(input("\nIngresa una de las opciones: "))
    return opcion
def ver_calificaciones (compras):     # Función para ver lista de productos.
    print()
    if len(compras) == 0:
        print("No hay alumnos para mostrar.")
    else:
        numero_compra = 1
        for a in compras:
            print(f"{numero_compra}) {a[0]}..... {a[1]}")
            numero_compra += 1
def agregar_alumno (compras):  # Función para añadir producto a la lista.
    calificaciones = []
    nombre = input("\nIngresa el nombre del alumno: ")
    alumnos.append([nombre])
    print("Ingresa la calificación de Estructura de datos: ")
    alumnos.append([calificaciones])
    print(f"El producto{[nombre, cantidad]} ha sido agregado con éxito!")
def eliminar_producto (compras):    # Función para eliminar producto de la lista.
    print()
    if len(compras) == 0:
        print("No hay productos para eliminar.")
    else:
        eliminar = int(input("Seleccione el índice del producto a eliminar: "))
        compras.pop(eliminar - 1)
        print("El producto ha sido eliminado correctamente.")

alumnos = [] # Lista de alumnos: nombre del alumno y calificaciones del alumno.
opcion = menu()
while opcion != 0:
    if opcion <= 6 and opcion >=0:
        if opcion == 1:
            print("Las calificaciones de todos los alumnos son: ")
            ver_alumnos(alumnos)
        elif opcion == 2:
            añadir_producto(compras)
        elif opcion == 3:
            eliminar_producto(compras)
        print("---------------------------------\n")
    else:
        print("\nOpción no válida.")
        print("---------------------------------\n")
    opcion = menu()
print("\nFin del programa.")
print("---------------------------------\n")