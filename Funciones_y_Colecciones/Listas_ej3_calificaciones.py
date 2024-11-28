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
    print("     [4].- Ver promedio grupal del Parcial 1.")
    print("     [5].- Agregar alumno y sus calificaciones.")
    print("     [6].- Eliminar alumno y sus calificaciones.")
    print("     [0].- Salir")
    opcion = int(input("\nIngresa una de las opciones: "))
    return opcion

def calificaciones_alumnos (alumnos, calificaciones):     # Función para ver las calificaciones de todos los alumnos.
    print()
    if len(alumnos) == 0:
        print("No hay alumnos para mostrar.")
    else:
        print("Las calificaciones de todos los alumnos son: ")
        for a in range(len(alumnos)): # NOTA: El bucle for empieza en cero por defecto.
                print(f"{alumnos[a]}: {calificaciones[a]}")

def calificacion_alumno(alumnos, calificaciones):   # Función para ver las calificaciones de un alumno.
    print()
    if len(alumnos) == 0:
        print("No hay alumnos para mostrar.")
    else:
        for a in range(len(alumnos)):
            print(f"{a+1}) {alumnos[a]}")
        posicion = int(input("Seleccione el índice del alumno a mostrar: "))
        print(f"Calificaciones de {alumnos[posicion-1]}:")
        print(f"Estructura de datos: {calificaciones[posicion-1][0]}")
        print(f"Derecho: {calificaciones[posicion-1][1]} ")
        print(f"Contabilidad: {calificaciones[posicion-1][2]}")
        print(f"Álgebra: {calificaciones[posicion-1][3]}")
        print(f"Electrónica: {calificaciones[posicion-1][4]}")

def agregar_alumno (alumnos, calificaciones):  # Función para añadir un alumno y sus calificaciones.
    nombre = input("\nIngresa el nombre del alumno: ")
    alumnos.append(nombre)
    materia1 = float(input("Ingresa la calificación de Estructura de datos: "))
    materia2 = float(input("Ingresa la calificación de Derecho: "))
    materia3 = float(input("Ingresa la calificación de Contabilidad: "))
    materia4 = float(input("Ingresa la calificación de Álgebra: "))
    materia5 = float(input("Ingresa la calificación de Electrónica: "))
    calificaciones.append([materia1,materia2,materia3,materia4,materia5])
    print(f"Alumno {nombre} con [{materia1}, {materia2}, {materia3}, {materia4}, {materia5}] se agregó con éxito!")

def promedio_alumnos(alumnos, calificaciones):  # Función para calcular el promedio del parcial 1 de los alumnos.
    promedio_parcial = []   # Lista para promedio del parcial 1 de cada alumno.
    for a in range(len(alumnos)):
        promedio = sum(calificaciones[a])/len(calificaciones[a])    # Cálculo del promedio parcial de un alumno.
        promedio_parcial.append(promedio)   # El promedio parcial del alumno se agrega a la lista de promedio parcial de los alumnos.
        print(f"{alumnos[a]}: {promedio:.1f}")
    return promedio_parcial # Se regresa la lista de promedio del parcial 1 de cada alumno.

def promedio_grupal (alumnos, calificaciones):  # Función para calcular el promedio grupal del parcial 1.
        promedio_alumno = promedio_alumnos(alumnos, calificaciones) # Se reutiliza la función que cálcula el promedio del parcial 1 de los alumnos.
        promedio_grupo = sum(promedio_alumno) / len(promedio_alumno) # Se suma el promedio parcial 1 de los alumnos y se divide entre el número de elementos (número de alumnos).
        print(f"\nEl promedio grupal del parcial 1 es: {promedio_grupo:.1f}")

def eliminar_alumno (alumnos, calificaciones):    # Función para eliminar alumno de la lista.
    print()
    if len(alumnos) == 0:
        print("No hay alumnos para eliminar.")
    else:
        for a in range(len(alumnos)):
            print(f"{a + 1}) {alumnos[a]}")
        eliminar = int(input("Seleccione el índice del alumno a eliminar: "))
        alumnos.pop(eliminar - 1)
        calificaciones.pop(eliminar-1)
        print("El alumno ha sido eliminado correctamente.")

alumnos = [] # Lista de alumnos: nombre del alumno y calificaciones del alumno.
calificaciones = [] # Lista de calificaciones del alumno.
opcion = menu()
while opcion != 0:
    if opcion <= 6 and opcion >=0:
        if opcion == 1:
            calificaciones_alumnos(alumnos,calificaciones)
        elif opcion == 2:
            calificacion_alumno(alumnos,calificaciones)
        elif opcion == 3:
            if len(alumnos) == 0:
                print("\nNo hay alumnos para mostrar.")
            else:
                print("\nEl promedio del parcial 1 de todos los alumnos son: ")
                promedio_alumnos(alumnos,calificaciones)
        elif opcion == 4:
            print()
            if len(alumnos) == 0:
                print("No hay alumnos para mostrar.")
            else:
                promedio_grupal(alumnos,calificaciones)
        elif opcion == 5:
            agregar_alumno(alumnos,calificaciones)
        elif opcion == 6:
            eliminar_alumno(alumnos,calificaciones)
        print("---------------------------------\n")
    else:
        print("\nOpción no válida.")
        print("---------------------------------\n")
    opcion = menu()
print("\nFin del programa.")
print("---------------------------------\n")