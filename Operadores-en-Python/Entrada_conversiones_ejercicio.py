"""
Nombre: Rebeca Gregorio Espina.
Fecha: 21 de octubre de 2024.
Descripción:
Escribe un programa de nombre Entrada_conversiones_ejercicio.py que realice lo siguiente:
    a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:
        Nombre (cadena).
        No. de cubículo (int).
        Horas de clase que imparte a la semana (float con 3 decimales).
        ¿Tiene más de 5 años en la unsij? (booleno).
    b) Muestre los datos en consola de forma adecuada.

    Nota: Asuma que el usuario siempre va a ingresar números cuando se requiera.
"""

# a) Pida los datos de los profesores utilizando nombres de variables adecuadas, la función input y el casting:
nombre = input("Ingresa el nombre del profesor: ")
# La función input() obtiene los datos ingresados por el usuario.
numero_cubiculo = int(input("Ingresa el número de cubículo: "))
# Esta función anidada permite que el valor que el usuario ingrese se convierta directamente a un número entero.
horas_clase = float(input("Ingresa las horas de clase que imparte a la semana: "))
# Esta función anidada permite que el valor que el usuario ingrese se convierta directamente a un número decimal.
print()
print(f"{nombre} se encuentra en el cubículo {numero_cubiculo} e imparte {horas_clase:.3f} horas de clase a la semana.")

# b) Muestre los datos en consola de forma adecuada.
"""
Resultado en pantalla:
    -Ingresa el nombre del profesor: Alberto Martínez Barbosa
    -Ingresa el número de cubículo: 12
    -Ingresa las horas de clase que imparte a la semana: 10

    -Alberto Martínez Barbosa se encuentra en el cubículo 12 e imparte 10.000 horas de clase a la semana.
"""