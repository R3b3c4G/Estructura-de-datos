'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Este programa determinará si te permiten el acceso al bar "La Negra", por lo que se debe cumplir lo siguiente:
    Tener al menos 18 años.
    Tener al menos $ 250.00 para gastar.
    Si ambas condiciones se cumplen, se imprime el mensaje en consola: "¡Bienvenido a tu mejor bar!". En caso contrario, se imprime: "Lo sentimos, ya estamos por cerrar!".

INSTRUCCIONES:
Escribe un programa de nombre Sentencias_ejercicio4.py que realice lo siguiente:
    a) Solicite al usuario su edad.
    b) Solicite al usuario el dinero con el que cuenta.
    c) Utilice la lógica adecuada para determinar el mensaje.
    d) Muestre el mensaje adecuado en consola.
'''
print("***  Acceso al bar 'La Negra'    ***")
# a) Solicite al usuario su edad.
edad = int(input("Ingrese tu edad: "))
# b) Solicite al usuario el dinero con el que cuenta.
presupuesto = int(input("Ingrese tu presupuesto: "))
print()
# c) Utilice la lógica adecuada para determinar el mensaje.
if edad > 18 and presupuesto >= 250.00:
    print("¡Bienvenido a tu mejor bar!")
else :
    print("Lo sentimos, ya estamos por cerrar.")
# d) Muestre el mensaje adecuado en consola.
"""
# Resultados en consola:
    ***  Acceso al bar 'La Negra'    ***
    Ingrese tu edad: 12
    Ingrese tu presupuesto: 580
    
    Lo sentimos, ya estamos por cerrar.
    
    ***  Acceso al bar 'La Negra'    ***
    Ingrese tu edad: 31
    Ingrese tu presupuesto: 300
    
    ¡Bienvenido a tu mejor bar!
    
    ***  Acceso al bar 'La Negra'    ***
    Ingrese tu edad: 31
    Ingrese tu presupuesto: 200
    
    Lo sentimos, ya estamos por cerrar.
"""