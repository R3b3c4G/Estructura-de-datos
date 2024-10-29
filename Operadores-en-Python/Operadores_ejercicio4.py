'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Este programa determinará True o False de acuerdo a la expresión (exp1 O exp2) Y (exp3 O exp4).

INSTRUCCIONES:
Escribe un programa de nombre Operadores_ejercicio4.py que realice lo siguiente:
    a) Pida al usuario cuatro valores booleanos (V/F).
    b) Obtenga el resultado de la expresión booleana de acuerdo con los valores ingresados.
    c) Muestre el resultado en consola como valor booleano (True/False).
'''
print("** Expresión booleana (exp1 O exp2) Y (exp3 O exp4) **")
# a) Pida al usuario cuatro valores booleanos (V/F).
# Primer valor.
expresion1=input("Ingresa valor booleano (V/F): ")
expresion1=expresion1.lower()=="v"
# Segundo valor.
expresion2=input("Ingresa valor booleano (V/F): ")
expresion2=expresion2.lower()=="v"
# Tercer valor.
expresion3=input("Ingresa valor booleano (V/F): ")
expresion3=expresion3.lower()=="v"
# Cuarto valor
expresion4=input("Ingresa valor booleano (V/F): ")
expresion4=expresion4.lower()=="v"
print()
# b) Obtenga el resultado de la expresión booleana de acuerdo con los valores ingresados.
print(f"El resultado de la expresión booleana es: {(expresion1 or expresion2) and (expresion3 or expresion4)}")
# c) Muestre el resultado en consola como valor booleano (True/False).
"""
# Resultado en consola:
    ** Expresión booleana (exp1 O exp2) Y (exp3 O exp4) **
    Ingresa valor booleano (V/F): V
    Ingresa valor booleano (V/F): F
    Ingresa valor booleano (V/F): V
    Ingresa valor booleano (V/F): F
    
    El resultado de la expresión booleana es: True
# 
    ** Expresión booleana (exp1 O exp2) Y (exp3 O exp4) **
    Ingresa valor booleano (V/F): F
    Ingresa valor booleano (V/F): F
    Ingresa valor booleano (V/F): V
    Ingresa valor booleano (V/F): V
    
    El resultado de la expresión booleana es: False
#  
    ** Expresión booleana (exp1 O exp2) Y (exp3 O exp4) **
    Ingresa valor booleano (V/F): F
    Ingresa valor booleano (V/F): V
    Ingresa valor booleano (V/F): V
    Ingresa valor booleano (V/F): F
    
    El resultado de la expresión booleana es: True
"""
