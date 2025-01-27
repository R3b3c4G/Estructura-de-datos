import random

lista_palabras = ["Anexo", "Campamento", "Feniletilamina", "Telescopio", "Papaya", "Otorrinolaringologo", "Uno"]
adivinar_palabra = random.choice(lista_palabras).lower()
intentos_acertados = set()
intentos_fallidos = 0
while intentos_fallidos < 5:
    print(f"te quedan {5 - intentos_fallidos} intentos: {(5 - intentos_fallidos) * "❤"}")
    print("Palabra: ", end=" ")
    for letra in adivinar_palabra:
        if letra in intentos_acertados:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    intento = input("\nIngresa una letra: ").lower()
    if intento in adivinar_palabra:
        print("Correcto,", end=" ")
        intentos_acertados.add(intento)
    else:
        print("Incorrecto,", end=" ")
        intentos_fallidos += 1
    if set(adivinar_palabra) == intentos_acertados:
        print(f"¡Felicidades ganaste! 👏🏻👏🏻")
        break
if intentos_fallidos == 5:
    print(f"perdiste, la palabra era: {adivinar_palabra}")
    print("Fin del juego...💀💀💀💀")

