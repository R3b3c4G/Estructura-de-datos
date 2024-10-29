'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Este programa determinará un descuento en compras en "La cona":
    Si tiene membresía, obtiene un 5 % de descuento en todas sus compras.
    Si tiene la membresía y su compra fue mayor o igual a $ 1000.00, entonces el descuento es del 8 %.
    Si no tiene la membresía, no obtiene ningún descuento y se invita a ser miembro.

INSTRUCCIONES:
Escribe un programa de nombre Sentencias_ejercicio3.py que realice lo siguiente:
    a) Solicite al usuario la cantidad comprada en la tienda.
    b) Pregunte al usuario si cuenta con la membresía (Si/No).
    c) Utilice la lógica adecuada para determinar el total a pagar.
    d) Muestre el descuento y el total a pagar en consola utilizando dos decimales.
'''
print("***  Descuentos por ser miembros de la cona    ***")
# a) Solicite al usuario la cantidad comprada en la tienda.
cantidad_comprada = float(input("Ingrese la cantidad comprada: "))
# b) Pregunte al usuario si cuenta con la membresía (Si/No).
membresia = input("¿Cuenta con membresía?: ")
membresia = membresia.lower() == "si"
print()
# c) Utilice la lógica adecuada para determinar el total a pagar.
if membresia and cantidad_comprada < 1000.00:                                       # Si tiene membresía, obtiene un 5 % de descuento en todas sus compras.
    print("Tu descuento es del 5 %.")
    print(f"El total es de $ {cantidad_comprada-cantidad_comprada * 0.05:.2f}.")
elif membresia and cantidad_comprada >= 1000.00:    # Si tiene la membresía y su compra fue mayor o igual a $ 1000.00, entonces el descuento es del 8 %.
    print("Tu descuento es del 8 %.")
    print(f"El total es de $ {cantidad_comprada-cantidad_comprada * 0.08:.2f}.")
else :                                              # Si no tiene la membresía, no obtiene ningún descuento y se invita a ser miembro.
    print("Se te invita a ser miembro de la tienda para obtener un descuento de hasta el 8 %.")
    print(f"El total es de $ {cantidad_comprada:.2f}.")
# d) Muestre el descuento y el total a pagar en consola utilizando dos decimales.
"""
# Resultados en cosola:
    ***  Descuentos por ser miembros de la cona    ***
    Ingrese la cantidad comprada: 500
    ¿Cuenta con membresía?: si
    
    Tu descuento es del 5 %.
    El total es de $ 475.00.
    
    ***  Descuentos por ser miembros de la cona    ***
    Ingrese la cantidad comprada: 500
    ¿Cuenta con membresía?: no
    
    Se te invita a ser miembro de la tienda para obtener un descuento de hasta el 8 %.
    El total es de $ 500.00.
    
    ***  Descuentos por ser miembros de la cona    ***
    Ingrese la cantidad comprada: 2000
    ¿Cuenta con membresía?: si
    
    Tu descuento es del 8 %.
    El total es de $ 1840.00.
"""