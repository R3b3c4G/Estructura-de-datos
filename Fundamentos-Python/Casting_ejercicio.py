'''
Nombre: Rebeca Gregorio Espina.
Fecha: 14 de octubre de 2024.
Descripción:
Ejercicios de conversión de tipos de datos (casting) en Python.
'''
"""
INSTRUCCIONES: Realiza un programa de nombre Casting_ejercicio.py que realice lo siguiente:
a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.
b) De los números anteriores, indica su valor booleano.
c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".
d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".
"""
#a) Convierta los siguientes números en cadenas: 3.14159265, 12, 0.
# Este ejercicio es una implementación de cómo convertir un número a cadena.
var_float = 3.14159265
var_int = 12
print("Conversión de número a cadena.")
print(f"Número: {var_float} --> Número como cadena: {str(var_float)}.")
print(f"Número: {var_int} --> Número como cadena: {str(var_int)}.")
var_int = 0
print(f"Número: {var_int} --> Número como cadena: {str(var_int)}.")
print()

#b)De los números anteriores, indica su valor booleano: 3.14159265, 12, 0.
# Este ejercicio es una implementación de como convertir un número a un valor booleano.
print("Conversión a booleanos.")
var_float = 3.14159265
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")
var_int = 12
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")
var_int = 0
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")
print()

#c) Convierta las siguientes cadenas a números: "10002", "100.02", "0".
# Este ejercicio es una implementación de como convertir una cadena a entero.
var_cadena = "10002"
var_int = int(var_cadena)

print("Conversión de cadena a entero.")
print(f"-Número como cadena: {var_cadena} --> Número como entero: {var_int }.")
var_cadena = "100.02"
var_float = float(var_cadena)
print(f"-Número como cadena: {var_cadena} --> Número como entero: {var_int }.")
var_cadena = "0"
var_int = int(var_cadena)
print(f"-Número como cadena: {var_cadena} --> Número como entero: {var_int }.")
print()

#d) De las cadenas anteriores, indica su valor booleano. Nota: especificar por qué el resultado de la cadena "0".
# Este ejercicio es una implementación de como convertir una cadena a booleano.
var_cadena= "10002"
es_verdadero = bool(var_int)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")
var_cadena = "100.02"
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")
var_cadena = "0"
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")
"""
El valor booleano de la cadena "0" es verdadero, porque la cadena no está vacía.
NOTA: En este problema podemos destacar que hay una gran diferencia entre un 0 (número) y un "0" (caracter). 
para 0 el valor booleano sería falso.
"""

