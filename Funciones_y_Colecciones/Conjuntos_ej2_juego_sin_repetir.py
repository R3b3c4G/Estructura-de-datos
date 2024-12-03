'''
Nombre: Rebeca Gregorio Espina.
Fecha: 2 de diciembre del 2024.
Descripción:
Este es un juego que se puede jugar de manera grupal, en donde el objetivo es decir palabras de un tema en específico y los jugadores deben tratar de no repetir la misma palabra. Nota: no se debe mostrar las palabras en ningún caso. Además, se debe llevar un contador de la cantidad de palabras que llevan.

INSTRUCCIONES:
Se debe mostrar el siguiente menú:
      ***  Juego "sin repetir"  ***
        Mostrar las reglas del juego.
        Presiona 'enter' para comenzar.
Para ello:
    a) Utilice un conjunto para almacenar las palabras ingresadas.
    b) Utilice la lógica adecuada para realizar el juego.
    c) Al final, se deben mostrar todas las palabras ingresadas.
'''
bandera = 0 # Variable que controla el fin del juego: Si no se repite ninguna palabra permanecerá en 0.
contador = 1    # Variable para contar la cantidad de palabras ingresadas.
# a) Utilice un conjunto para almacenar las palabras ingresadas.
palabras_ingresadas = set() # Se inicializa un conjunto vacío.
print("     ***  Juego 'sin repetir'  ***")
print("Este es un juego que se puede jugar de manera grupal,")
print("en donde el objetivo es decir palabras de un tema en")
print("específico y los jugadores deben tratar de no repetir")
print("la misma palabra.")
tema = input("Ingresa el tema del juego: ")
print()
while bandera == 0:
    mi_palabra = input(f"Ingresa la palabra {contador} del tema {tema}: ")
    if mi_palabra in palabras_ingresadas:   # Se verifica si la palabra ingresada ya existe en el conjunto.
        print(f"El juego ya terminó! Han dicho {(contador-1)} palabras diferentes.")
        print(f"Las palabras del tema de {tema} fueron: {palabras_ingresadas}") # c) Al final, se deben mostrar todas las palabras ingresadas.
        bandera = 1
    else:
        palabras_ingresadas.add(mi_palabra) # Palabra diferente se agrega al conjunto.
    contador += 1



