'''
Nombre: Rebeca Gregorio Espina.
Fecha: 2 de diciembre del 2024.
Descripción:
Este programa es una rifa, en donde se registra el correo electrónico y solamente permite ingresar un correo por participante.

INSTRUCCIONES:
Escribe un programa de nombre Conjuntos_ej1_rifa.py que realice lo siguiente:
Se debe mostrar el siguiente menú:
      ***  Rifa de una computadora  ***
    1) Ver correos de participantes.
    2) Agregar correo de participante.
    3) Eliminar correo de participante.
    4) Seleccionar ganador.
    0) Salir.
    Cualquier otro caso -> Opción no válida.
Para ello:
    a) Utilice un conjunto para almacenar los correos de los participantes.
    b) Utilice un valor aleatorio utilizando la función random.choice(lista). Notar que hay que convertir primero a una lista.
'''
from random import choice
def menu ():    # Función para imprimir menú y devolver opción del usuario.
    print("***  Rifa de una computadora  ***")
    print("     [1].- Ver correos de participantes.")
    print("     [2].- Agregar correo de participante.")
    print("     [3].- Eliminar correo de participante.")
    print("     [4].- Seleccionar ganador.")
    print("     [0].- Salir.")
    opcion = int(input("\nElige una opción del menú anterior: "))
    return opcion
opcion = None
# a) Utilice un conjunto para almacenar los correos de los participantes.
conjunto_correo = set() # Se declara un conjunto vacío.
opcion = menu()
while opcion != 0 :
    print()
    if 0 <= opcion <=4: # Valida la opción del usuario.
        if opcion == 1: # Ver correos de participantes.
            if len(conjunto_correo) == 0:
                print("No hay participantes para mostrar.")
            else:
                print("El conjunto de correos es: ")
                for a in conjunto_correo:
                    print(f"- {a}")
        elif opcion == 2:   # Agregar correo de participante.
            mi_correo = input("Ingresa el correo del participante a agregar: ")
            if mi_correo in conjunto_correo:
                print("Ya existe el correo.")
            else:
                conjunto_correo.add(mi_correo)
                print(f"El correo {mi_correo} ha sido agregado con éxito!")
        elif opcion == 3:   # Eliminar correo de participante.
            if len(conjunto_correo) == 0:
                print("No hay correos para eliminar.")
            else:
                for a in conjunto_correo:
                    print(f"- {a}")
                eliminar_correo = input("Ingrese el correo del participante a aliminar: ")
                if eliminar_correo in conjunto_correo:
                    conjunto_correo.remove(eliminar_correo)
                    print("El correo ha sido eliminado con éxito.")
                else:
                    print("El correo no existe.")
        if opcion == 4: # Seleccionar ganador.
            if len(conjunto_correo) == 0:
                print("No hay participantes.")
            else:
                lista_correo = list(conjunto_correo)    # b) Utilice un valor aleatorio utilizando la función random.choice(lista).
                print(f"El ganador es {choice(lista_correo)}. Muchas felicidades!")
        print("----------------------------------------------\n")
        opcion = menu()
print("\nFin del programa.")