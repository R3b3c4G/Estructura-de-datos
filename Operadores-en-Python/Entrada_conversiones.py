'''
Nombre: Rebeca Gregorio Espina.
Fecha: 21 de octubre de 2024.
Descripción:
Conversión de cadenas a int, float y boolean mediante la interacción con consola.
'''

# Comentar sobre las funciones anidadas.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")
# La función input() obtiene los datos ingresados por el usuario.
semestre = int(input("Ingresa el no. de semestre: "))
# Esta funcion anidada permite que el valor que el usuario ingrese se convierta directamente a un número entero.
promedio = float(input("Ingresa el promedio: "))
# Esta función anidada permite que el valor que el usuario ingrese se convierta directamente a un número decimal.
es_mujer = input("¿Es mujer (Si/No)?: ")
# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si"
# La función .lower convierte letras mayúsculas a minúsculas.

# Se imprimen los datos del alumno.
# Comentar  qué es lo que realiza {promedio:.2f} probando con números diferentes.
print()
print(f"{nombre} cursa el {semestre} semestre con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.")
"""
# :.2f-->Es un formato de impresión en el que se especifica que se deben mostrar dos decimales.
# Por lo tanto, para la variable promedio se mostrarán dos decimales.
Ejemplo con diferentes valores:
    -Ana cursa el 6 semestre con un promedio de 7.00. Además, es mujer: True.
    -Raúl cursa el 3 semestre con un promedio de 8.00. Además, es mujer: False.
    -Diego cursa el 9 semestre con un promedio de 9.00. Además, es mujer: False.
"""
