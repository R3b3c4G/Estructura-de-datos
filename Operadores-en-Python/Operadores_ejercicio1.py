"""
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Este programa determinará si el usuario aplica para una bonificación.

INSTRUCCIONES:
Escribe un programa de nombre Operadores_ejercicio1.py que realice lo siguiente:
    a) Solicite al usuario un número decimal con el valor de una compra.
    b) Pregunte al usuario si la compra fue a MSI (Si/No).
    c) El usuario aplica a la bonificación si la compra fue mayor a 5000.00 y si la compra fue a MSI.
    d) Muestre el resultado en consola como valor booleano (True/False).

Nota: Prueba con todos los casos posibles.
"""
print("   ***      Sistema de bonificación  ***   ")
# a) Solicite al usuario un número decimal con el valor de una compra.
compra=float(input("Ingrese el valor de su compra en número decimal: "))
# Pregunte al usuario si la compra fue a MSI (Si/No).
intereses=input("¿Su compra es a meses sin intereses (Si/No)?: ")
#La función .lower convierte letras mayúsculas a minúsculas.
intereses=intereses.lower()=="si"
print()
# c) El usuario aplica a la bonificación si la compra fue mayor a 5000.00 y si la compra fue a MSI.
print(f"¿Aplica para bonificación?: {compra > 5000.00 and intereses}.")#T/F
# d) Muestre el resultado en consola como valor booleano (True/False).

"""
Casos posibles, resultado en consola:
# Compra menor a 5000.00 y no fue a meses sin intereses.
       ***      Sistema de bonificación  ***   
    Ingrese el valor de su compra en número decimal: 40.00
    ¿Su compra es a meses sin intereses (Si/No)?: No
    
    ¿Aplica para bonificación?: False
    
# Compra mayor a 5000.00 y no fue a meses sin intereses.
       ***      Sistema de bonificación  ***   
    Ingrese el valor de su compra en número decimal: 6000.00
    ¿Su compra es a meses sin intereses (Si/No)?: No
    
    ¿Aplica para bonificación?: False.
    
# Compra menor a 5000.00 y a meses sin intereses.
       ***      Sistema de bonificación  ***   
    Ingrese el valor de su compra en número decimal: 400.00
    ¿Su compra es a meses sin intereses (Si/No)?: Si
    
    ¿Aplica para bonificación?: False.

    
# Compra mayor a 5000.00 y a meses sin intereses.
       ***      Sistema de bonificación  ***   
    Ingrese el valor de su compra en número decimal: 5001.00
    ¿Su compra es a meses sin intereses (Si/No)?: Si
    
    ¿Aplica para bonificación?: True. 

# 
    Ingrese el valor de su compra en número decimal: 5500
    ¿Su compra es a meses sin intereses (Si/No)?: si
    
    ¿Aplica para bonificación?: True.
"""
