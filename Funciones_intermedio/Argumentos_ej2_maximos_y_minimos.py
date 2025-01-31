"""
Nombre: Rebeca Gregorio Espina.
Fecha: 31 de enero del 2025.
Descripción:
Este programa encuentra el valor máximo y mínimo de todos los números ingresados por el usuario.

Para ello:
    a) Solicite los números con decimales, validando que tengan el formato adecuado.
    b) Utilice una función con argumentos variables que devuelva el valor máximo y mínimo.
    c) Muestre el resultado en consola.
"""

def valor_minimo_maximo(*vargs):
    """
    Función que calcula el valor mínimo y máximo de los números ingresados por el usuario.
    :param vargs: Lista de números ingresados por el usuario.
    :return No regresa nada; sin embargo, muestra en consola el valor mínimo y máximo de la lista de números ingresados por el usuario.
    """
    # Verificar si la lista no esta vacía.
    if vargs:
        # Inicializar el valor máximo y mínimo con el valor del primer elemento de la lista.
        maximo = vargs[0]
        minimo = vargs[0]
        for numero in vargs:
            # Actualizar el valor de máximo si hay otro valor mayor.
            if numero > maximo:
                maximo = numero
            # Actualizar el valor de mínimo si hay otro valor menor.
            if numero < minimo:
                minimo = numero
        print(f"El número mínimo es: {minimo}")
        print(f"El número máximo es: {maximo}")
    else:
        print("No se ingresaron números.")

def cadena_a_flotante(cadena):
    """
    Función que convierte una cadena a un número flotante.
    :param cadena: Cadena a convertir.
    :return: Regresa el número flotante si cumple con el formato, en caso contrario, devuelve None.
    """
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-').replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None

def main() -> None:
    """
    Función principal. Solicita números flotantes al usuario y los manda a validar para finalmente encontrar el valor máximo y mínimo.
    """
    print("          ********  Programa que calcula la suma de los números pares.  ********")
    print()
    # Se solicitan los números flotantes mediante un ciclo, el cual termina hasta ingresar 'enter'.
    # Los números flotantes se almacenan en una lista.
    numeros_enteros = []
    numero_cadena = input(f"Ingresa el número [{len(numeros_enteros) + 1}] o presiona enter para continuar: ")
    while bool(numero_cadena):
        numero = cadena_a_flotante(cadena = numero_cadena)
        if numero is None:
            print("Formato no válido, intenta nuevamente.")
        else:
            # Agregar número válido a la lista.
            numeros_enteros.append(numero)
        numero_cadena = input(f"Ingresa el número [{len(numeros_enteros) + 1}] o presiona enter para continuar: ")
    # Llamar a la función valor_minimo_maximo mandando como argumento los números flotantes de la lista.
    valor_minimo_maximo(*numeros_enteros)


""" %%%%%%%     CÓDIGO A NIVEL DE MÓDULO    %%%%%%%%%%%%%%%%%%%%% """
if __name__ == '__main__':
    main()
