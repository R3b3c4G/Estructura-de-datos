'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Uso de la sentencia de control if.
'''

"""
La sentencia de control if es una estructura de control fundamental que permite ejecutar diferentes bloques de código
 dependiendo de si una condición se cumple o no.

Sintaxis:

if condición:
    # Código a ejecutar si la condición es verdadera. Notar que hay que dejar un espacio de tabulador.

# Código que se continúa ejecutando. Notar que ya no hay espacio y está a la misma altura que el if.
"""

# Ejemplo en donde se imprime un mensaje si el usuario tiene la mayoría de edad.
print("  ***  Programa que determina si eres mayor de edad  ***")
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")

print("Este código se ejecuta después de evaluarse la sentencia if.")

# Probar qué pasa con espacios simples, no dejando una línea entre ambas funciones print()
# y que ambos print() se encuentren a la misma altura.
"""
Resultado: 
    -Al no dejar una línea entre ambas funciones print() y que ambos print() se encuentren a la misma altura, el
     mensaje estaría dentro de la sentencia if y si se ingresa un valor menor a 18 nunca llegaría a imprimirse 
     "Este código se ejecuta después de evaluarse la sentencia if." (se imprime si eres mayor de edad).
     Ejemplo:
        ***  Programa que determina si eres mayor de edad  ***
        Ingresa tu edad: 8 
        
* NOTA: 
    -Es importante dejar un espacio de tabulador para cada bloque de condición.
"""


