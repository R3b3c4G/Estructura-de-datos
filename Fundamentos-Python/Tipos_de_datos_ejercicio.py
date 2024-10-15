#Rebeca Gregorio Espina.
#8 de octubre de 2024.
"""
Descripción: Este programa contiene algunos ejemplos del uso de los tipos de
datos básicos en Python, tales como variables de tipo:
- Int
- Float
- String
- Boolean

De manera general, después de la impresión del título "*** Gastos diarios ***", la línea de código
almacena un dato en una variable y en la siguiente línea se imprime el contenido de esa variable
y así repetitivamente para las diferentes variables.
"""

print("*** Gastos diarios ***")
# En esta variable se almacena una cadena de texto.
mi_variable_dia = "lunes"
print("Día: ",mi_variable_dia)
# En esta variable se almacena un valor de tipo entero.
mi_variable_pasaje = 20
print("Pasaje: ",mi_variable_pasaje)
#En esta variable se almacena un número decimal.
mi_variable_comida = 135.5
print("Comida: ",mi_variable_comida)
# En esta variable se almacena un número decimal.
mi_variable_otros_gastos = 34.5
print("Otros gastos: ",mi_variable_otros_gastos)
#Esta variable almacena un tipo de dato lógico en este caso con una condición verdadera.
mi_variable_pregunta_presupuesto = True
print("¿Fue mayor a mi presupuesto?: ",mi_variable_pregunta_presupuesto)
#Salto de línea.
print()

"""
En las siguientes líneas de código se hace uso de las variables anteriores y realiza las mismas instrucciones,
con la excepción de que se reasigna con otros valores.
"""
print("*** Gastos diarios ***")
mi_variable_dia = "martes"
print("Día: ",mi_variable_dia)
mi_variable_pasaje = 12
print("Pasaje: ",mi_variable_pasaje)
mi_variable_comida = 45.5
print("Comida: ",mi_variable_comida)
mi_variable_otros_gastos = 4.5
print("Otros gastos: ",mi_variable_otros_gastos)

mi_variable_pregunta_presupuesto = False
print("¿Fue mayor a mi presupuesto?: ",mi_variable_pregunta_presupuesto)