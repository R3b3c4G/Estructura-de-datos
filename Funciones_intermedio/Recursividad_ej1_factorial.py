"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de enero del 2025.
Descripción:
Este programa calcula el factorial de un número entero positivo ingresado por el usuario, utilizando recursividad.
Notar que: n! = n*(n-1)!

Para ello:
    a) Solicite al usuario el número al que se requiere calcular el factorial, validando que tenga el formato adecuado.
    b) Utilice una función recursiva para calcular el factorial, indicando el caso base y el caso recursivo.
    c) Muestre el resultado en consola.
"""
def validar_entero(numero_cadena: str) -> bool:
    """
    Función que determina si el número ingresado se encuentra entre 0 y un entero positivo.
    :param numero_cadena: Cadena a validar.
    :return: Se regresa un valor booleano dependiendo si la cadena cumple con el formato
    """
    if numero_cadena.isnumeric():
        return True

    else:
        return False

def funcion_recursiva_factorial(numero: int) -> int:
    """
    Función que calcula el factorial de un número entre 0 y un entero positivo utilizando recursividad.
    :param numero: Se imprime del cero hasta este número.
        """
    # Primer caso base: Factorial de 0 es 1.
    if numero == 0:
        return 1
    # Segundo caso base: Factorial de 1 es 1.
    elif numero == 1:
        return numero
    # Caso recursiva: numero! = numero * (numero -1)!  para numero > 1.
    else:
        return numero * funcion_recursiva_factorial(numero - 1)

def main() -> None:
    """
    Función principal.
    """
    print("          ********  Programa que calcula el factorial de manera recursiva.  ********")
    print()
    # Se solicita un número y se valida que sea entre 0 y un entero positivo.
    numero_cadena = input("Ingresa un número entre 0 y un entero positivo: ")
    print()
    # Si es un número válido, se llama a las funciones recursivas.
    # En caso contrario, mostrar un mensaje de "Formato no válido." y finaliza el programa.
    if validar_entero(numero_cadena):
        numero = int(numero_cadena)
        resultado = funcion_recursiva_factorial(numero)
        print(f"El factorial de {numero} es: {resultado}")
    else:
        print("Formato no válido.")
    print("\nFin del programa.")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
