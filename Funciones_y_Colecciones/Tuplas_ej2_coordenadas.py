'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa almacena diversos puntos como coordenadas y permite obtener la ecuación de la recta entre dos de los puntos.

INSTRUCCIONES:
Escribe un programa de nombre Tuplas_ej2_coordenadas.py que realice lo siguiente:
Se debe mostrar el siguiente menú:
      ***  Rectas a partir de puntos (coordenadas) en el plano cartesiano  ***
    1) Ver coordenadas almacenadas.
    2) Agregar coordenada (x,y).
    3) Calcular la pendiente y la ecuación de la recta entre dos coordenadas.
    4) Eliminar coordenada (x,y).
    0) Salir.
    Cualquier otro caso -> Opción no válida.
Para ello:
    a) Utilice funciones para modular el código.
    b) Utilice una tupla para almacenar las coordenadas (x,y) del punto.
    c) Utilice una lista para almacenar las tuplas de las coordenadas.
'''
def menu ():
    print("***  Rectas a partir de puntos (coordenadas) en el plano cartesiano  ***")
    print("     [1].- Ver coordenadas almacenadas.")
    print("     [2].- Agregar coordenada (x,y).")
    print("     [3].- Calcular la pendiente y la ecuación de la recta entre dos coordenadas.")
    print("     [4].- Eliminar coordenada (x,y).")
    print("     [0].- Salir.")
    opcion = int(input("Ingresa una de las opciones: "))
    return opcion

def mostrar_coordenadas (coordenadas):  # Función para ver coordenadas almacenadas.
    if len(coordenadas) == 0:
        print("No hay coordenadas.")
    else:
        print("Lista de coordenadas: ")
        for a in range(len(coordenadas)):
            print(f"Coordenada {a+1}: {coordenadas[a]}")

def agregar_coordenada(coordenadas):    # Función para agregar coordenada (x,y).
    x = float(input("Ingresa el valor de la coordenada x: "))
    y = float(input("Ingresa el valor de la coordenada y: "))
    tupla =(x,y)    # b) Utilice una tupla para almacenar las coordenadas (x,y) del punto.
    coordenadas.append(tupla)
    print(f"La coordenada {tupla} se agregó con éxito!")

def pendiente (coordenadas):    # Función para calcular la pendiente y la ecuación de la recta entre dos coordenadas.
    for a in range(len(coordenadas)):
        print(f"{a + 1}) {coordenadas[a]}")
    coordenada1 = int(input("Seleccione el índice de la primera coordenada: "))
    coordenada2 = int(input("Seleccione el índice de la segunda coordenada: "))
    x1, y1 = coordenadas[coordenada1-1]
    print("x1:", x1, "y1: ",y1)
    x2, y2 = coordenadas[coordenada2-1]
    pendiente = (y2 - y1)/(x2 - x1) # Calcular pendiente.
    b = y1 - pendiente * x1 # Despejar la intersección en el eje y.
    print(f"La pendiente entre la coordenada {coordenadas[coordenada1-1]} y la {coordenadas[coordenada2-1]} es {pendiente}.")
    print(f"La ecuación de la recta es: y = {pendiente}x + {b}")

def eliminar (coordenadas): # Función para eliminar coordenada (x,y).
    for a in range(len(coordenadas)):
        print(f"{a + 1}) {coordenadas[a]}")
    posicion = int(input("Seleccione el índice de la coordenada a eliminar: "))
    coordenadas.pop(posicion - 1)
    print("La coordenada ha siso eliminada correctamente.")

coordenadas = []    # c) Utilice una lista para almacenar las tuplas de las coordenadas.
opcion = menu()
while opcion != 0 :
    print()
    if 0 <= opcion <=4:
        if opcion == 1:
            if len(coordenadas) == 0:
                print("No hay coordenadas para mostrar.")
            else:
                mostrar_coordenadas(coordenadas)
        elif opcion == 2:
             agregar_coordenada(coordenadas)
        elif opcion == 3:
            if len(coordenadas) == 0:
                print("No hay coordenadas.")
            else:
                pendiente(coordenadas)
        elif opcion == 4:
            if len(coordenadas) == 0:
                print("No hay coordenadas a eliminar.")
            else:
                eliminar(coordenadas)
        print("-------------------------\n")
        opcion = menu()
print("\nFin del programa.")
print("-------------------------\n")