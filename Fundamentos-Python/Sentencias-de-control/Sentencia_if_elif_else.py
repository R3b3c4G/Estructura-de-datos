'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Uso de la sentencia de control if - elif - else.
'''

"""
La sentencia elif es una extensión del if-else y permite evaluar múltiples condiciones de forma secuencial. 
Es como tener varias opciones a elegir, ejecutándose el bloque de código correspondiente a la primera condición 
que sea verdadera.

Sintaxis:

if condicion_1:
    # Código a ejecutar si la condición_1 es verdadera.

elif condición_2:
    # Código a ejecutar si la condición_2 es verdadera.
  .
  .
  .
else:
    # Código que se ejecuta si todas las condiciones fueron falsas.
"""

# Ejemplo que determina el grupo al que pertenece de acuerdo a su edad.
print("  ***  Programa que determina el grupo de acuerdo a la edad  ***")
edad=int(input("Ingresa tu edad: "))
if edad <=14:
    print("Niños y adolescentes.")
elif edad >=15 and  edad <= 25:
    print("Jóvenes.")
elif edad >=26 and  edad <= 45:
    print("Adultos jóvenes.")
elif edad >=46 and  edad <= 60:
    print("Adultos maduros.")
else:
    print("Adultos mayores.")
###############################################
"""
MODO DEPURACIÓN (DEBUG)

Utilizar ahora el modo depuración.
1) Crear un punto de ruptura en la variable edad. Marcar el número de línea y se pondrá un círculo color rojo.
2) Clic derecho y ejecutar el modo Debug.
3) Observar la nueva pantalla e ir ejecutando paso-a-paso (step over) F8.
4) Observar el comportamiento.
   -Con step over puedo ejecutar el programa paso a paso y en tiempo real, a partir de que ingreso
   la edad, va verificando las condiciones de forma secuencial y al momento que entra 
   a una de ellas, termina el programa.
"""