'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Ejemplos de uso de los operadores de asignación.
'''

"""
En programación, las operaciones de asignación se utilizan para almacenar un valor en una variable. 
Es decir, se establece una relación entre un nombre (la variable) y un valor en la memoria de la computadora.
"""

# Asignación múltiple: En una sola línea de código se asignan diferentes valores para las diferentes variables.
print("   ***   Asignación múltiple   ***")
nombre, primer_apellido, segundo_apellido = "Rebeca", "Gregorio", "Espina"
print(f"Asignación múltiple de cadenas: {nombre} {primer_apellido} {segundo_apellido}.")
print()
entero1, entero2 = 1, 2
print(f"Asignación múltiple de enteros: {entero1} y {entero2}.")
print()
decimal1, decimal2, decimal3, decimal4 = 3.14, 3.1416, 3.14159, 3.141592
print(f"Asignación múltiple de decimales: {decimal1}, {decimal2}, {decimal3} y {decimal4}.")
print()
# Asignación múltiple con una combinación de diferentes tipos de datos.
nombre, entero1, decimal4 = "Rebeca", 12, 3.1415926            # Es posible combinar tipos de datos.
print(f"Asignación múltiple: {nombre}, {entero1} y {decimal4}.")
print()
# Asignación múltiple con una combinación de distintas operaciones aritméticas.
suma, resta = entero1 + entero2, decimal1 - decimal2            # Es posible asignar distintas operaciones.
print(f"Asignaciones de operaciones: suma {suma} y resta {resta:.4f}.")
print()
print()
# Asignación encadenada: Se asigna el mismo valor a diferentes variables en una sola línea de código.
print("   ***   Asignación encadenada   ***")
entero3 = entero4 = entero5 = 10    # Se les asigna el mismo valor a todas las variables.
print(f"Asignación encadenada de: {entero3} = {entero4} = {entero5} = 10.")
print()
print()
# Intercambio de variables: Permite el intercambio de los valores de dos variables sin requerir un tercer variable temporal.
print("   ***   Intercambio de variables   ***")
entero5, entero6 = 5, 6
print(f"Valores asignados: entero5 = {entero5} y entero6 = {entero6}.")
entero6, entero5 = entero5, entero6
print(f"Valores intercambiados: entero5 = {entero5} y entero6 = {entero6}.")
print()
# Intercambio de variables con una combinación de diferentes tipos de datos.
variable_prueba1, variable_prueba2 = 100, "Hola mundo"
variable_prueba1, variable_prueba2 = variable_prueba2, variable_prueba1 # Es posible porque las variables son dinámicas.
print(f"Valores asignados: variable_prueba1 = {variable_prueba1} y variable_prueba2 = {variable_prueba2}.")
print(f"Valores intercambiados: variable_prueba1 = {variable_prueba2} y variable_prueba2 = {variable_prueba1}.")

"""
# Resultado en consola:
       ***   Asignación múltiple   ***
    Asignación múltiple de cadenas: Rebeca Gregorio Espina.
    
    Asignación múltiple de enteros: 1 y 2.
    
    Asignación múltiple de decimales: 3.14, 3.1416, 3.14159 y 3.141592.
    
    Asignación múltiple: Rebeca, 12 y 3.1415926.
    
    Asignaciones de operaciones: suma 14 y resta -0.0016.
    
    
       ***   Asignación encadenada   ***
    Asignación encadenada de: 10 = 10 = 10 = 10.
    
    
       ***   Intercambio de variables   ***
    Valores asignados: entero5 = 5 y entero6 = 6.
    Valores intercambiados: entero5 = 6 y entero6 = 5.
    
    Valores asignados: variable_prueba1 = Hola mundo y variable_prueba2 = 100.
    Valores intercambiados: variable_prueba1 = 100 y variable_prueba2 = Hola mundo.
"""