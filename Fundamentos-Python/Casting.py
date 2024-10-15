'''
Nombre: Rebeca Gregorio Espina.
Fecha: 14 de octubre de 2024.
Descripción:
Conversión de tipos de datos (casting) en Python.
'''

# Notas
'''
La conversión de tipos de datos implica manipular datos que no están en el tipo de dato requerido. Ejemplos:
de cadena a entero, de cadena a número flotante, y viceversa.
'''
# *****   Conversión de cadena a entero     *****
var_cadena = "951"
var_int = int(var_cadena)

# Utiliza la letra "f" antes de las comillas para indicar que la cadena será formateada.
# Esto significa que puedes incluir variables y expresiones dentro de las llaves {}
# y su valor será insertado en el texto final.
print("Conversión de cadena a entero.")
print(f"Número como cadena: {var_cadena}.")
print(f"Número como int más uno: {var_int + 1}.")
"""
Resutado en pantalla:
Conversión de cadena a entero.
Número como cadena: 951.
Número como int más uno: 952.
"""
# *****   Conversión de cadena a flotante     *****
var_cadena = "8.88"
var_float = float(var_cadena)
print()
print("Conversión de cadena a flotante.")
print(f"Número como cadena: {var_cadena}.")
print(f"Número como float más cero punto uno: {var_float + 0.1}.")
"""
Resutado en pantalla:
Conversión de cadena a flotante.
Número como cadena: 8.88.
Número como float más cero punto uno: 8.98.
"""
# *****   Conversión de número a cadena     *****
var_int = 123
var_float = 123.321
print()
print("Conversión de número a cadena.")
print(f"Los números {var_int} y {var_float} se convierten a cadena utilizando str(var_int): {str(var_cadena)}, y "
      f"str(var_float): {str(var_float)}.")
"""
Resutado en pantalla:
Conversión de número a cadena.
Los números 123 y 123.321 se convierten a cadena utilizando str(var_int): 8.88, y str(var_float): 123.321.
"""