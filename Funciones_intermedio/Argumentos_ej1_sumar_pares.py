"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de enero del 2025.
Descripción:
Este programa realiza la suma de todos los números pares ingresados por el usuario.

Para ello:
    a) Solicite al usuario los números enteros. Nota: Hay que validar que tengan el formato adecuado.
    b) Utilice una función con argumentos variables que devuelva la suma de los números pares.
    c) Muestre el resultado en consola.
"""


def suma_numero_par(*vargs):
    """
    Función que calcula la suma de números pares argumentos variables.
    :param vargs: Lista de números enteros ingresados por el usuario.
    :return No regresa nada; sin embargo, muestra en consola la suma de los números pares ingresados.
    """
    # Inicializando la suma en 0.
    suma = 0
    for numero in vargs:
        # Si el número es par, se acumula a la suma.
        if numero % 2 == 0:
            suma += numero
    print(f"\nLa suma de todos los números pares es: {suma}")

def cadena_a_entero(cadena: str) -> float | None:
    """
    Función que convierte una cadena a un número.
    :param cadena: Cadena a convertir.
    :return: Regresa el número entero si cumple con el formato, en caso contrario, devuelve None.
    """
    no_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip('-')
    if revisar_cadena.isnumeric() and no_guiones in (0, 1):
        return int(cadena)
    else:
        return None

def main() -> None:
    """
    Función principal. Solicita números enteros al usuario y los manda a validar para finalmente hacer la suma de números pares.
    """
    print("          ********  Programa que calcula la suma de los números pares.  ********")
    print()
    # Se solicitan los números enteros mediante un ciclo, el cual termina hasta ingresar 'enter'.
    # Los números enteros se almacenan en una lista.
    numeros_enteros = []
    numero_cadena = input(f"Ingresa el número [{len(numeros_enteros) + 1}] o presiona enter para continuar: ")
    while bool(numero_cadena):
        numero = cadena_a_entero(cadena = numero_cadena)
        if numero is None:
            print("Formato no válido, intenta nuevamente.")
        else:
            numeros_enteros.append(numero)
        numero_cadena = input(f"Ingresa el número [{len(numeros_enteros) + 1}] o presiona enter para continuar: ")
    # Llamar a la función suma_numero_par mandando como argumento los números enteros de la lista.
    suma_numero_par(*numeros_enteros)



""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()