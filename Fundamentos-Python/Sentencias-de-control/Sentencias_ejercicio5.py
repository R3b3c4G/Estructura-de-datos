'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Este programa determinará el promedio de una materia e indicará si el alumno aprobó o no la materia.

INSTRUCCIONES:
Escribe un programa de nombre Sentencias_ejercicio5.py que realice lo siguiente:
a) Solicite al usuario sus tres calificaciones parciales y la calificación del ordinario.
b) Calcule el promedio y determine si aprobó (calificación mínima de 6.0).
d) Muestre el promedio (utilizando un decimal) y el mensaje: "¡Felicidades! Aprobaste.", o el mensaje: "Lo siento, no aprobaste.", según sea el caso.
'''
print("*** Programa para calcular el promedio de una materia ***")
#   a) Solicite al usuario sus tres calificaciones parciales y la calificación del ordinario.
calificacion_parcial1 = float(input("Ingresa la calificación del parcial 1: "))
calificacion_parcial2 = float(input("Ingresa la calificación del parcial 2: "))
calificacion_parcial3 = float(input("Ingresa la calificación del parcial 3: "))
calificacion_ordinaria = float(input("Ingresa la calificación del ordinario: "))
# b) Calcule el promedio.
promedio_parcial = ((calificacion_parcial1 + calificacion_parcial2 + calificacion_parcial3)/3) * 0.5
promedio_ordinario = calificacion_ordinaria * 0.5
promedio = promedio_ordinario + promedio_parcial
print()
# Determine si aprobó (calificación mínima de 6.0).
if promedio >= 6.0:
    print(f"La calificación final es de {promedio:.1f}. ¡Felicidades! Aprobaste.")
else:
    print(f"La calificación final es de {promedio:.1f}. Lo siento, no aprobaste.")
# d) Muestre el promedio (utilizando un decimal) y el mensaje: "¡Felicidades! Aprobaste.", o el mensaje: "Lo siento, no aprobaste.", según sea el caso.
"""
# Resultados en consola:
    *** Programa para calcular el promedio de una materia ***
    Ingresa la calificación del parcial 1: 8
    Ingresa la calificación del parcial 2: 8
    Ingresa la calificación del parcial 3: 7
    Ingresa la calificación del ordinario: 9
    
    La calificación final es de 8.3. ¡Felicidades! Aprobaste.

    *** Programa para calcular el promedio de una materia ***
    Ingresa la calificación del parcial 1: 8
    Ingresa la calificación del parcial 2: 8
    Ingresa la calificación del parcial 3: 7
    Ingresa la calificación del ordinario: 3
    
    La calificación final es de 5.3. Lo siento, no aprobaste.
"""