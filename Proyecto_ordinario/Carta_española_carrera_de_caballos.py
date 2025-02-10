"""
Nombre: Rebeca Gregorio Espina.
Fecha: 10 de febrero de 2025
Descripción:
Este juego simula una carrera de caballos utilizando la baraja española.
Cada jugador apuesta por un caballo, y el avance de cada uno se determina extrayendo cartas de la baraja
Dependiendo del valor o palo de la carta, un caballo avanzará o se quedará atrás
El primer caballo en llegar a la meta gana la partida.
"""

import random

# Definir cartas para el volteo de cartas.
cartas_horizontales = [
    "1 de Oros", "2 de Oros", "7 de Copas", "4 de Espadas", "5 de Espadas", "12 de Bastos"
]
# Definir baraja principal.
mazo_cartas = [
    "3 de Oros", "4 de Oros", "5 de Oros", "6 de Oros", "7 de Oros", "10 de Oros", "12 de Oros",
    "1 de Copas", "2 de Copas", "3 de Copas", "4 de Copas", "5 de Copas", "6 de Copas", "10 de Copas", "12 de Copas",
    "1 de Espadas", "2 de Espadas", "3 de Espadas", "6 de Espadas", "7 de Espadas", "10 de Espadas", "12 de Espadas",
    "1 de Bastos", "2 de Bastos", "3 de Bastos", "4 de Bastos", "5 de Bastos", "6 de Bastos", "7 de Bastos",
    "10 de Bastos"
]
# Definir posición de victoria.
meta = 6

def voltear_carta() -> str:
    """
    Función que selecciona e imprime una carta horizontal (carta volteada).
    :return: Regresa la carta volteada aleatoriamente.
    """
    payaso = random.choice(cartas_horizontales)
    print(f"¡La carta {payaso} se ha volteado! 🤡\n")
    return payaso

def sacar_carta() -> str:
    """
    Función que selecciona y elimina una carta de la baraja principal.
    :return: Regresa la carta volteada aleatoriamente.
    """
    carta = random.choice(mazo_cartas)
    mazo_cartas.remove(carta)
    print(f"La carta seleccionada es: {carta}")
    return carta

def contar_cartas(carta:str, oro:int, espadas:int, copas:int, bastos:int) -> tuple[int, int, int, int]:
    """
    Función que actualiza el contador de posiciones de cada carta dependiendo al la familia perteneciente (Oro, Espada, Copa y Basto).
    :param carta: Carta seleccionada.
    :param oro: Contador actual de cartas de Oros.
    :param espadas: Contador actual de cartas de Espadas.
    :param copas: Contador actual de cartas de Copas.
    :param bastos: Contador actual de cartas de Bastos.
    :return: Regresa una tupla de los contadores actualizados de Oro Espada, Copa y Basto.
    """
    if "Oros" in carta:
        oro += 1
    elif "Espadas" in carta:
        espadas += 1
    elif "Copas" in carta:
        copas += 1
    elif "Bastos" in carta:
        bastos += 1
    return oro, espadas, copas, bastos

def retroceder_caballo(carta_volteada, oro:int , espadas:int, copas:int, bastos:int)-> tuple[int, int, int, int]:
    """
    Función que decrementa el contador de posiciones si la carta principal pertenece la familia (Oro, Espada, Copa y Basto) de la carta volteada.
    :param carta_volteada: Es la carta volteda.
    :param oro: Contador actual de cartas de Oros.
    :param espadas: Contador actual de cartas de Espadas.
    :param copas: Contador actual de cartas de Copas.
    :param bastos: Contador actual de cartas de Bastos.
    :return: Regresa una tupla de los contadores actualizados de Oro Espada, Copa y Basto.
    """
    if "Oros" in carta_volteada and oro > 0:
        oro -= 1
    elif "Espadas" in carta_volteada and espadas > 0:
        espadas -= 1
    elif "Copas" in carta_volteada and copas > 0:
        copas -= 1
    elif "Bastos" in carta_volteada and bastos > 0:
        bastos -= 1
    return oro, espadas, copas, bastos

def mostrar_tablero(oro:int , espadas:int, copas:int, bastos:int) -> None:
    """
    Función que muestra el tablero de juego (avance de cada caballo).
    """
    nombres = ["[O]", "[E]", "[C]", "[B]"]
    valores = [oro, espadas, copas, bastos]
    for indice in range(4):
        print("______________________")
        print(f"{nombres[indice]}|" + " " * (valores[indice] * 3) + "🐎")
    print()

def jugar_carrera_de_caballos() -> None:
    """
    Función principal del juego.
    """
    # Inicializar contadores de posición de cada palo a 0.
    oro, espadas, copas, bastos = 0, 0, 0, 0
    # Definir límite para aplicar el volteo de cartas.
    limite_actual = 1
    # Afirmar que aún no hay ganador.
    no_ganador = True
    print("🃏🏇🏿 🃏🏇   Carta española carrera de caballos  🃏🏇🏿 🃏🏇🏿\n")
    mostrar_tablero(oro, espadas, copas, bastos)
    # Mientras no haya ganador y queden cartas de la baraja.
    while no_ganador and mazo_cartas:
        opcion = input("Ingresa el número '5' para sacar cartas del mazo o '0' para salir: ")
        if opcion == '0':   # Opción para salir del juego.
            break
        elif opcion == '5': # Opción para continuar el juego.
            carta = sacar_carta()
            oro, espadas, copas, bastos = contar_cartas(carta, oro, espadas, copas, bastos)
            print(f"🌷 Contadores actuales: Oros={oro}, Espadas={espadas}, Copas={copas}, Bastos={bastos}")
            mostrar_tablero(oro, espadas, copas, bastos)
            # Comprobar si debe voltear una carta.
            if min(oro, espadas, copas, bastos) >= limite_actual:
                carta_volteada = voltear_carta()
                oro, espadas, copas, bastos = retroceder_caballo(carta_volteada, oro, espadas, copas, bastos)
                limite_actual += 1  # Incrementar límite para el próximo volteo de carta.
                mostrar_tablero(oro, espadas, copas, bastos)
            # Comprobar ganador.
            if oro >= meta:
                ganador = "Oros"
            elif espadas >= meta:
                ganador = "Espadas"
            elif copas >= meta:
                ganador = "Copas"
            elif bastos >= meta:
                ganador = "Bastos"
            else:
                ganador = None
            if ganador:
                no_ganador = False
                print(f"¡El caballo {ganador} ha ganado la carrera!")
                mostrar_tablero(oro, espadas, copas, bastos)
        else:
            # Mensaje para valor no válida.
            print("Opción no válida, ingresa el número '5' para sacar cartas del mazo o '0' para salir")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    jugar_carrera_de_caballos()