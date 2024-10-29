'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Ejemplos de uso de los operadores lógicos.
'''

"""
Los operadores lógicos permiten combinar expresiones booleanas (verdadero o falso) para crear condiciones más complejas.
Estos operadores nos permiten realizar operaciones lógicas como "y", "o" y "no", lo que nos da la capacidad de tomar 
decisiones más sofisticadas dentro de nuestros programas.
"""

# Se solicita por consola que se ingresen dos valores (Si/No) para convertirlas en expresiones booleanas.
expresion1 = input("Ingresa un valor (Si/No): ")
expresion2 = input("Ingresa otro valor (Si/No): ")

# Las cadenas se convierten a expresiones booleanas (ver Fundamentos-Python -> Entrada_conversiones.py).
# El signo "==" se ocupa para comparar valores y devuelve un valor booleano (true/false).
expresion1 = expresion1.lower() == "si"
expresion2 = expresion2.lower() == "si"

# Se imprimen mensajes sobre operaciones lógicas.
# AND (Y)
print(f"¿Ambas expresiones fueron 'si'? {expresion1 and expresion2}")
# OR (O)
print(f"¿Alguna expresión fue 'si'? {expresion1 or expresion2}")
# NOT (NO)
print(f"Lo contrario de la primera expresión es: {not expresion1}")
# NOT (NO)
print(f"Lo contrario de la segunda expresión es: {not expresion2}")

"""
NOTAS:
    -La función lower() convierte en minúscula una cadena.
    -Los operadores lógicos (and, or, not) son palabras clave que se utilizan para conectar y evaluar condiciones dentro de una expresión.
    -Los operadores lógicos permiten trabajar con valores booleanos, que solo pueden ser True o False, y el resultado de las operaciones también será un valor booleano.
"""