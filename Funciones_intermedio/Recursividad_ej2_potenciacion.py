"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de enero del 2025.
Descripción:
Este programa calcula la potencia de un número a otro número de manera recursiva. Ambos son números
enteros positivos ingresados por el usuario.
Notar que: a^b = a*(a^(b-1)).

Para ello:
    a) Solicite al usuario ambos números, validando que tengan el formato adecuado.
    b) Utilice una función recursiva para calcular la potencia, indicando el caso base y el caso recursivo.
    c) Muestre el resultado en consola.
"""
def validar_entero(numero_cadena: str) -> bool:
    """
     Función que valida si una cadena representa un entero no negativo.
    :param numero_cadena: Cadena a validar.
    :return: Se regresa un valor booleano dependiendo si la cadena cumple con el formato
    """
    if numero_cadena.isnumeric():
        return True
    else:
        return False

def funcion_recursiva_potencia(base: int, exponente: int) -> int | str:
    """
    Función para calcular la potencia de forma recursiva, para bases y exponentes entre 0 y un entero positivo.
    :param base: Es la base, 0 o un entero positivo.
    :param exponente: Es el exponente, 0 o un entero positivo.
    :returns Si a^b es definido; regresa un entero e "Indeterminado" si la base y exponente es 0.
        """
    # Caso base: 0^0 es indefinido.
    if base == 0 and exponente == 0:
        return "Indeterminado"
    # Caso base: Cualquier base entero positivo elevado a la potencia 0 es 1.
    elif exponente == 0:
        return 1
    # Caso recursiva: a^b = a*(a^(b-1))
    else:
        return base * funcion_recursiva_potencia(base,exponente - 1)

def main() -> None:
    """
    Función principal. Solicita al usuario la base y exponente, manda validar, si son valores validados manda a calcular
    la potencia y finalmente muestra el resultado.
    """
    print("          ********  Programa que calcula a^b de manera recursiva.  ********")
    print()
    # Se solicita un número y se valida que sea entre 0 y un entero positivo.
    base_cadena = input("Ingresa la base a: ")
    exponente_cadena = input("Ingresa el exponente b: ")

    print()
    # Si el número de la base y exponente es válido, se llama a las funciones recursivas.
    # En caso contrario, mostrar un mensaje de "Formato no válido." y finaliza el programa.
    if validar_entero(base_cadena) and validar_entero(exponente_cadena):
        numero_base = int(base_cadena)
        numero_exponente = int(exponente_cadena)
        resultado = funcion_recursiva_potencia(numero_base, numero_exponente)
        print(f"{numero_base}^{numero_exponente} = {resultado}")
    else:
        print("Formato no válido.")
    print("\nFin del programa.")


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
