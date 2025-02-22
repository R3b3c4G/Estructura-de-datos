"""
Nombre: Patricia Pérez Cruz
Fecha: 26 de enero de 2025
Descripción: Implementación del juego 4 en Raya. Permite jugar entre dos personas o contra una CPU
"""

import random

#Mi función para imprimir el tablero
def imprimir_tablero(tablero):
    """
    Imprime el tablero en su estado actual
    Cada fila del tablero se imprime como una cadena formateada
    """
    for fila in tablero:
        print(fila[0], "|", fila[1], "|", fila[2], "|", fila[3], "|", fila[4], "|", fila[5], "|", fila[6])
    print("\n")


def verificar_ganador(tablero, jugador):
    """
    Verifica si un jugador ha ganado el juego
    Se revisan las filas, columnas y diagonales (de izquierda a derecha y de derecha a izquierda)
    para identificar si hay cuatro fichas consecutivas del mismo jugador
    """
    #Compruebo filas
    for fila in range(6):
        for columna in range(4):  # Para revisar solo las primeras 4 columnas en cada fila
            if tablero[fila][columna] == jugador and tablero[fila][columna + 1] == jugador and tablero[fila][columna + 2] == jugador and tablero[fila][columna + 3] == jugador:
                return True

    #Columnas
    for columna in range(7):
        for fila in range(3):  # Para revisar solo las primeras 3 filas en cada columna
            if tablero[fila][columna] == jugador and tablero[fila + 1][columna] == jugador and tablero[fila + 2][columna] == jugador and tablero[fila + 3][columna] == jugador:
                return True

    #Diagonales de izquierda a derecha
    for fila in range(3):
        for columna in range(4):
            if tablero[fila][columna] == jugador and tablero[fila + 1][columna + 1] == jugador and tablero[fila + 2][columna + 2] == jugador and tablero[fila + 3][columna + 3] == jugador:
                return True

    #Y diagonales de derecha a izquierda
    for fila in range(3):
        for columna in range(3, 7):
            if tablero[fila][columna] == jugador and tablero[fila + 1][columna - 1] == jugador and tablero[fila + 2][columna - 2] == jugador and tablero[fila + 3][columna - 3] == jugador:
                return True

    return False


def verificar_empate(tablero):
    """
    Verifica si el juego ha terminado en empate
    Un empate ocurre cuando no hay casillas vacías en el tablero
    """
    for fila in tablero:
        if " " in fila:
            return False  #Si hay una casilla vacía, no hay empate
    return True


def obtener_jugada_cpu(tablero):
    """
    Genera una jugada aleatoria para la CPU
    Busca una columna válida (no llena) y selecciona la fila más baja disponible en esa columna
    """
    while True:
        columna = random.randint(0, 6)
        for fila in range(5, -1, -1):  #Busca la primera casilla vacía en la columna empezando desde abajo
            if tablero[fila][columna] == " ":
                return fila, columna


def jugar_4_en_raya(modo_juego=None, jugador_1="X", jugador_2="O"):
    """
    Controla el flujo principal del juego 4 en Raya.
    Permite jugar en modo de dos personas o contra la CPU
    """
    if modo_juego is None:
        while True:
            opcion = input("Elige modo (1: Dos personas, 2: Contra CPU): ").strip()
            if opcion == "1" or opcion == "2":
                break
            else:
                print("Opción inválida, porfi ingresar 1 o 2.")
        if opcion == "2":
            modo_juego = "cpu"
        else:
            modo_juego = "dos_personas"

    #Hice mi tablero vacío
    tablero = [
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " "]]  #Tablero de 6 filas por 7 columnas

    #Inicializar turno del jugador
    turno_jugador = jugador_1

    while True:
        imprimir_tablero(tablero)

        # Para el turno de la CPU
        if modo_juego == "cpu" and turno_jugador == jugador_2:
            fila, columna = obtener_jugada_cpu(tablero)
            print(f"Fila de la CPU: {fila+1} | Columna de la CPU: {columna+1}")

        #Turno del jugador
        else:
            while True:
                columna = input(f"Jugador {turno_jugador} - Elige columna (1-7): ")
                if columna.isdigit():
                    columna = int(columna) - 1
                    if columna < 0 or columna > 6:
                        print("Columna fuera de rango, debes ingresar un número entre 1 y 7")
                    else:
                        for fila in range(5, -1, -1):
                            if tablero[fila][columna] == " ":
                                break
                        else:
                            print("Esa columna está llena, elige otra columna")
                        break
                else:
                    print("Entrada no válida, debes ingresar un número entre 1 y 7")

        #Colocar la ficha en el tablero
        tablero[fila][columna] = turno_jugador

        #Verificar si el jugador ha ganado
        if verificar_ganador(tablero, turno_jugador):
            imprimir_tablero(tablero)
            if turno_jugador == jugador_1:
                print("¡Jugador 1 (X) ha ganado!")
            elif modo_juego == "cpu" and turno_jugador == jugador_2:
                print("¡La CPU (O) ha ganado!")
            else:
                print("¡Jugador 2 (O) ha ganado!")
            break

        #Checar empate
        if verificar_empate(tablero):
            imprimir_tablero(tablero)
            print("¡Es un empate!")
            break

        # Cambiar turno
        if turno_jugador == jugador_1:
            turno_jugador = jugador_2
        else:
            turno_jugador = jugador_1


if __name__ == "__main__":
    jugar_4_en_raya()