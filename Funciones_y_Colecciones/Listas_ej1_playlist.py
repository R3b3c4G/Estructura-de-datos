'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa es una playlist de videos de YouTube.

INSTRUCCIONES:
Escribe un programa de nombre Listas_ej1_playlist.py que realice lo siguiente:
Se debe mostrar el siguiente menú:
  ***  Playlist de videos de YouTube  ***
    1) Ver playlist por videos añadidos.
    2) Ver playlist por orden ascendente (A-Z).
    3) Ver playlist por orden descendente (Z-A).
    4) Añadir video de YouTube a la playlist.
    5) Añadir varios videos de YouTube a la playlist.
    6) Eliminar video de la playlist.
    0) Salir.
    Cualquier otro caso -> Opción no válida.

Para ello:
    a) Utilice funciones para modular el código.
    b) Utilice una lista para la playlist.
    c) Utilice índices para mostrar los videos.
'''
def menu ():    # Función para imprimir menú y devolver opción del usuario.
    print("***  Playlist de videos de YouTube  ***")
    print("     [1].- Ver playlist por videos añadidos.")
    print("     [2].- Ver playlist por orden ascendente (A-Z).")
    print("     [3].- Ver playlist por orden descendente (Z-A).")
    print("     [4].- Añadir video de YouTube a la playlist.")
    print("     [5].- Añadir varios videos de YouTube a la playlist.")
    print("     [6].- Eliminar video de la playlist.")
    print("     [0].- Salir")
    opcion = int(input("\nIngresa una de las opciones: "))
    return opcion
def mostrar(videos):    # Función para mostrar el listado de videos.
    if len(videos) == 0:
        print("No hay videos para mostrar.")
    else:
        numero_video = 1
        for a in videos:
            print(f"{numero_video}) {a}")
            numero_video += 1

def añadir():   # Función para añadir videos.
        mi_video = input("Ingresa el nombre del video a agregar a la playlist: ")
        videos.append(mi_video)
        print(f"El video '{mi_video}' ha sido agregado con éxito!")
def borrar():
    print()
    if len(videos) == 0:
        print("No hay videos para borrar.")
    else:
        mostrar(videos)
        eliminar_video = int(input("Ingresa el índice del video a eliminar: "))
        videos.pop(eliminar_video - 1)
        print("El video ha sido eliminado con éxito!")
videos = []
opcion = menu()
print()
while opcion != 0:
    if opcion <= 6 and opcion >=0:
        if opcion == 1:
            print("Lista de videos por añadidos:")
            mostrar(videos)
        elif opcion == 2:
            if len(videos) == 0:
                print("No hay videos por ordenar.")
            else:
                print("Lista de videos por orden ascendente (A-Z):")
                ascendente = videos.copy()  # Crear una copia, para no modificar la lista de videos por añadidos.
                ascendente.sort()
                mostrar(ascendente)
        elif opcion == 3:
            if len(videos) == 0:
                print("No hay videos por ordenar.")
            else:
                print("Lista de videos por orden descendente (Z-A):")
                descendente = videos.copy() # Crear una copia, para no modificar la lista de videos por añadidos.
                descendente.sort(reverse=True)
                mostrar(descendente)
        elif opcion == 4:
            añadir()
        elif opcion == 5:
            auxiliar = 0
            cantidad = int(input("Cuantos vídeos desea añadir: "))
            while auxiliar < cantidad:
                añadir()
                auxiliar+=1
        elif opcion == 6:
            borrar()
        print("--------------------\n")
        opcion = menu()
        print()
    else:
        print("Opción no válida.")
        opcion = menu()
        print("--------------------\n")
print("Fin del programa.")
print("--------------------\n")

