'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Este programa mostrará los detalles del tour turístico Ecoturixtlán de acuerdo a las siguientes tarifas:
    - Precio de un adulto: $ 200.00.
    - Precio de un niño: $ 100.00.
    Además, si la visita son los lunes, martes y jueves, se tiene un descuento del 10 %.

INSTRUCCIONES:
Escribe un programa de nombre Sentencias_ejercicio6.py que realice lo siguiente:
    a) Solicite al usuario el nombre de la persona a cargo.
    b) Defina con valores constantes el precio del boleto del adulto y del niño.
    c) Solicite el número de adultos y de niños.
    d) Pregunte el día de la semana.
    e) Calcule el costo total.
    f) Muestre los detalles del cliente y el día, así como el costo total.
'''
print("***  Tour turístico Ecoturisxtlán    ***")
# a) Solicite al usuario el nombre de la persona a cargo.
nombre_cliente = input("Ingresa el nombre del cliente: ")
# b) Defina con valores constantes, el precio del boleto del adulto y del niño.
precio_boleto_adulto = 200.00   # Precio de un adulto: $ 200.00.
precio_boleto_niño = 100.00     # Precio de un niño: $ 100.00.
# c) Solicite el número de adultos y de niños.
numero_adultos = int(input("Ingresa el número de adultos: "))
numero_niños = int(input("Ingresa el número de niños: "))
# d) Pregunte el día de la semana.
dia_semana = input(("Ingresa el día de la semana: "))
dia_semana = dia_semana.lower()
# e) Calcule el costo total.
if dia_semana == "lunes" or dia_semana == "martes" or dia_semana == "jueves" :  # Si la visita son los lunes, martes y jueves, se tiene un descuento del 10 %.
    costo_total = ((precio_boleto_adulto * numero_adultos) + (precio_boleto_niño * numero_niños))-((precio_boleto_adulto * numero_adultos) + (precio_boleto_niño * numero_niños)) * 0.10
else:
    costo_total = (precio_boleto_adulto * numero_adultos) + (precio_boleto_niño * numero_niños)
print()
# f) Muestre los detalles del cliente y el día, así como el costo total.
print(f"Gracias por tu visita {nombre_cliente} este día {dia_semana}. El costo total es de $ {costo_total:.2f}.")
"""
# Resultado en consola:
***  Tour turístico Ecoturisxtlán    ***
Ingresa el nombre del cliente: Rebeca
Ingresa el número de adultos: 2
Ingresa el número de niños: 2
Ingresa el día de la semana: lunes

Gracias por tu visita Rebeca este día lunes. El costo total es de $ 540.00.


***  Tour turístico Ecoturisxtlán    ***
Ingresa el nombre del cliente: Rebeca
Ingresa el número de adultos: 2
Ingresa el número de niños: 2
Ingresa el día de la semana: viernes

Gracias por tu visita Rebeca este día viernes. El costo total es de $ 600.00.
"""