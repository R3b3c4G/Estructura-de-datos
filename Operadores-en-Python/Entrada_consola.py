'''
Nombre: Rebeca Gregorio Espina.
Fecha: 21 de octubre de 2024.
Descripción:
Entrada de datos por consola para interactuar con el usuario con valores dinámicos.
'''

# Comentar sobre la función input.
"""
-La función input() permite leer datos que el usuario esté ingresando por el teclado mientras el programa está en ejecución.
-Devuelve la entrada en una cadena aunque sea número. 
"""
numero1_cadena = input("Introduce un número decimal: ")
numero2_cadena = input("Introduce otro número decimal: ")
resultado_cadena = numero1_cadena + numero2_cadena
# Verificar qué es lo que realiza esta instrucción (ver el print).

print()
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}")
"""
-Las variables "numero1_cadena" y "numero2_cadena" se almacenan como cadenas y la suma de estos se guarda en la variable "resultado_cadena".
    *Al realizar la suma no se refleja la operación aritmética debido a que son cadenas y en lugar de esto la variable "resultado_cadena" 
     almacena la concatenación de "numero1_cadena" y "numero2_cadena".
Resultado sin casting de variables:
****  Recibir número sin un casting de variables  ****
El resultado de 69 y 1 es: 691
"""
# Comentar por qué se realiza el casting de variables.
"""
-El casting de variables se realiza porque la función input siempre regresa una cadena y 
para trabajar con operaciones aritméticas es necesario que la cadena se convierta a valores numéricos. 
"""
numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)
# Las variables se convirtieron en números decimales.
resultado_float = numero1_float + numero2_float
# Verificar qué es lo que realiza de esta manera y compáralo.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")
"""
-Las variables "numero1_cadena" y "numero2_cadena" se convierten a números decimales y se guardan en una nueva variable.
-La variable "resultado_float" almacena la suma de las variables "numero1_float" y "numero1_float" .
    *Al realizar la suma si se refleja la operación aritmética debido a que los datos ingresados (cadenas) se convirtieron a
     decimal.
Resultado con casting de variables:
****  Casting de variables  ****
El resultado de 69.0 y 1.0 es: 70.0
"""
#Nota: Sin casting en lugar de sumar concatena los valores y  con casting si realiza la operación correspondiente.
