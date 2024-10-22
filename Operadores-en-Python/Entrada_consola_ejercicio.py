'''
Nombre: Rebeca Gregorio Espina.
Fecha: 21 de octubre de 2024.
Descripción:
Este programa es un ejercicio en donde se implementa la entrada de datos por consola.
En este caso se trabajará con números decimales y con esos números se realizarán operaciones básicas como la suma, resta, multiplicación y división.
'''
"""
Instrucciones:
-Escribe un programa de nombre Entrada_consola_ejercicio.py que realice lo siguiente:
    a) Pida 2 números decimales por consola al usuario utilizando la función input.
    b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.
    Nota: Asuma que el usuario siempre va a ingresar números y que el segundo número es diferente de cero.
"""
# a) Pida 2 números decimales por consola al usuario utilizando la función input.
numero1_cadena = input("Introduce un número decimal: ")
numero2_cadena = input("Introduce otro número decimal: ")

# Casting de variables.
numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)
# Las variables se convirtieron en números decimales.



# b) Muestre los resultados de las operaciones básicas con esos números: suma, resta, multiplicación y división.
# Suma.
print(" ****  Suma  ****")
resultado_float = numero1_float + numero2_float
print(f"El resultado de {numero1_float} + {numero2_float} es: {resultado_float}.")
# Resta.
print(" ****  Resta  ****")
resultado_float = numero1_float - numero2_float
print(f"El resultado de {numero1_float} - {numero2_float} es: {resultado_float}.")
# Multiplicación.
print(" ****  Multiplicación  ****")
resultado_float = numero1_float * numero2_float
print(f"El resultado de {numero1_float} * {numero2_float} es: {resultado_float}.")
# Divisón.
print(" ****  División  ****")
resultado_float = numero1_float / numero2_float
print(f"El resultado de {numero1_float} / {numero2_float} es: {resultado_float}.")
