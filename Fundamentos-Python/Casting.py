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

# La letra "f" antes de las comillas es para indicar que la cadena será formateada.
# Esto significa que puedes incluir variables y expresiones dentro de las llaves {}
# y su valor será insertado en el texto final.
print("Conversión de cadena a entero.")
print(f"Número como cadena: {var_cadena}.")
#Una vez que la cadena de texto se convierte en un tipo de dato entero, se le suma 1.
print(f"Número como int más uno: {var_int + 1}.")
"""
Resultado en pantalla:
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
#Una vez que la cadena de texto se convierte en un tipo de dato flotante, se le suma 0.1.
print(f"Número como float más cero punto uno: {var_float + 0.1}.")
"""
Resultado en pantalla:
Conversión de cadena a flotante.
Número como cadena: 8.88.
Número como float más cero punto uno: 8.98.
"""
# *****   Conversión de número a cadena     *****
var_int = 123
var_float = 123.321
print()
#str es una función que convierte un objeto en cadena.
print("Conversión de número a cadena.")
print(f"Los números {var_int} y {var_float} se convierten a cadena utilizando str(var_int): {str(var_cadena)}, y "
      f"str(var_float): {str(var_float)}.")
"""
Resultado en pantalla:
Conversión de número a cadena.
Los números 123 y 123.321 se convierten a cadena utilizando str(var_int): 8.88, y str(var_float): 123.321.
"""
# *****   Conversión a booleano     *****
# Si el valor es 0, cadena vacía o None, la función bool regresa un valor de False. En caso contrario, regresa True.
print()
print("Conversión a booleanos.")

var_int = 0
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")
var_int = -30
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")

var_float = 0.0
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")
var_float = 0.01
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")

var_cadena = ""
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")
var_cadena = None
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")
var_cadena = " "
es_verdadero = bool(var_cadena)
print(f"¿El valor de {var_cadena} es verdadero? {es_verdadero}.")
"""
Resultado en pantalla:
Conversión número a booleano.
¿El valor de 0 es verdadero? False.
¿El valor de -30 es verdadero? True.
¿El valor de 0.0 es verdadero? False.
¿El valor de 0.01 es verdadero? True.
¿El valor de  es verdadero? False.
¿El valor de None es verdadero? False.
¿El valor de   es verdadero? True.
"""