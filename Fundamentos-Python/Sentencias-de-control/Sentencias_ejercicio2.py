'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Este programa determinará la estación del año de acuerdo al número de mes ingresado por el usuario.

INSTRUCCIONES:
Escribe un programa de nombre Sentencias_ejercicio2.py que realice lo siguiente:
    a) Solicite al usuario un número que representa al mes.
    b) Utilice la lógica adecuada para determinar la estación del año de acuerdo con:
        3, 4 y 5: Primavera.
        6, 7 y 8: Verano.
        9,10 y 11: Otoño.
        12, 1 y 2: Invierno.
        Otro caso: Mensaje de mes incorrecto.
    c) Muestre la estación correspondiente en consola.
'''

# a) Solicite al usuario un número que representa al mes.
print("***  Programa que determina la estación del año  ***")
numero_de_mes = int(input("Ingresa el número de mes: "))
print()
# b) Utilice la lógica adecuada para determinar la estación del año de acuerdo con:
if numero_de_mes == 3 or numero_de_mes == 4 or numero_de_mes == 5:      #         3, 4 y 5: Primavera.
    estacion = "Primavera."
elif numero_de_mes == 6 or numero_de_mes == 7 or numero_de_mes == 8:    #         6, 7 y 8: Verano.
    estacion = "Verano."
elif numero_de_mes == 9 or numero_de_mes == 10 or numero_de_mes == 11:  #         9,10 y 11: Otoño.
    estacion = "Otoño."
elif numero_de_mes == 12 or numero_de_mes == 1 or numero_de_mes == 2:   #         12, 1 y 2: Invierno.
    estacion = "Invierno."
else:                                                                   #         Otro caso: Mensaje de mes incorrecto.
    estacion = "Mes incorrecto."
# c) Muestre la estación correspondiente en consola.
print("La estación es: ", estacion)

"""
# Resultado en consola:
    ***  Programa que determina la estación del año  ***
    Ingresa el número de mes: 2
    
    La estación es:  Invierno.
    
    
    ***  Programa que determina la estación del año  ***
    Ingresa el número de mes: 8
    
    La estación es:  Verano.
    
    
    ***  Programa que determina la estación del año  ***
    Ingresa el número de mes: 13
    
    La estación es:  Mes incorrecto.
"""