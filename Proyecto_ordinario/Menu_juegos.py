"""
Nombre: Rebeca Gregorio Espina
Fecha: 10 de febrero de 2025

Descripción:
Este programa es el menú principal de todos los videojuegos.
"""
import Ahorcado
import Gato
import Cuatro_en_raya
import Carta_española_carrera_de_caballos
import Batalla_naval
import Menu_desplazable

def mostrar_menu():
    while True:
        print("[1].- Ahorcado")
        print("[2].- Juego del Gato")
        print("[3].- 4 en Raya")
        print("[4].- Juego de caballos")
        print("[5].- Batalla Naval")
        print("[0].- Salir")

        eleccion = input("Ingresa tu selección: ")

        if eleccion.isnumeric():
            eleccion = int(eleccion)

            if eleccion == 1:
                print("Iniciando Ahorcado...")
                Ahorcado.jugar_ahorcado()
                break
            elif eleccion == 2:
                print("Iniciando Juego del Gato...")
                Gato.jugar_gato()
                break
            elif eleccion == 3:
                print("Iniciando 4 en Raya...")
                Cuatro_en_raya.jugar_4_en_raya()
                break
            elif eleccion == 4:
                print("Iniciando Juego de caballos...")
                Carta_española_carrera_de_caballos.jugar_carrera_de_caballos()
                break
            elif eleccion == 5:
                print("Iniciando Batalla Naval...")
                Batalla_naval.jugar_batalla()
                break
            elif eleccion == 0:
                print("¡Hasta luego!")
                break
            else:
                print("Seleccion no válida, por favor elige una opción entre 0 y 3")
        else:
            print("Por favor, ingresa un número válido")


if __name__ == "__main__":
    Menu_desplazable.mostrar_mensaje("~~ JUEGOS ~~")
    mostrar_menu()