'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa realiza las operaciones básicas de una cuenta.


INSTRUCCIONES:
Escribe un programa de nombre Ciclos_ej4_cuenta_bancaria.py que realice lo siguiente:
    1) Mostrar saldo.
    2) Ingresar dinero.
    3) Retirar dinero.
    0) Salir.
    Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
Para ello:
    a) Suponga un saldo inicial cualquiera.
    b) Muestre el menú.
    c) Si la opción seleccionada es 1 o 2, verificando la cantidad a modificar.
    c) Calcule el resultado de acuerdo a la opción.
    d) Muestre el saldo en pantalla.
    e) Repita el menú anterior.
'''
opcion = None
saldo = 100 # a) Suponga un saldo inicial cualquiera.
while opcion != 0:
    print("***   Bienvenido a tu cuenta de Banco Azteca   ***")  # b) Muestre el menú.
    print("[1].- Consultar saldo.")
    print("[2].- Ingresar dinero.")
    print("[3].- Retirar dinero.")
    print("[0].- Salir.")
    opcion = int(input("\nElige una opción del menú anterior: "))
    print()
    if opcion <= 6 and opcion >= 0:
        if opcion == 1:
            print(f"Tu saldo es de: $ {saldo:.2f}")  # d) Muestre el saldo en pantalla.
        elif opcion == 2:
            ingreso = float(input("Cantidad a ingresar: "))   # d) Muestre el saldo en pantalla.
            saldo= saldo + ingreso
            print(f"Tu nuevo saldo es de: $ {saldo:.2f}")
        elif opcion == 3:
            retiro = float(input("Cantidad a retirar: "))
            if saldo >= retiro:
                saldo = saldo - retiro
                print(f"Tu nuevo saldo es de: $ {saldo:.2f}")
            else:
                print("Saldo insuficiente.")
    else:
        print("Opción no válida.")
    print("-------------------------------\n")
print("Nos vemos.")
"""
#   Resultados en consola:
    ***   Bienvenido a tu cuenta de Banco Azteca   ***
    [1].- Consultar saldo.
    [2].- Ingresar dinero.
    [3].- Retirar dinero.
    [0].- Salir.
    
    Elige una opción del menú anterior: 1
    
    Tu saldo es de: $ 100.00
    -------------------------------
    
    ***   Bienvenido a tu cuenta de Banco Azteca   ***
    [1].- Consultar saldo.
    [2].- Ingresar dinero.
    [3].- Retirar dinero.
    [0].- Salir.
    
    Elige una opción del menú anterior: 2
    
    Cantidad a ingresar: 25
    Tu nuevo saldo es de: $ 125.00
    -------------------------------
    
    ***   Bienvenido a tu cuenta de Banco Azteca   ***
    [1].- Consultar saldo.
    [2].- Ingresar dinero.
    [3].- Retirar dinero.
    [0].- Salir.
    
    Elige una opción del menú anterior: 1
    
    Tu saldo es de: $ 125.00
    -------------------------------
    
    ***   Bienvenido a tu cuenta de Banco Azteca   ***
    [1].- Consultar saldo.
    [2].- Ingresar dinero.
    [3].- Retirar dinero.
    [0].- Salir.
    
    Elige una opción del menú anterior: 3
    
    Cantidad a retirar: 125
    Tu nuevo saldo es de: $ 0.00
    -------------------------------
    
    ***   Bienvenido a tu cuenta de Banco Azteca   ***
    [1].- Consultar saldo.
    [2].- Ingresar dinero.
    [3].- Retirar dinero.
    [0].- Salir.
    
    Elige una opción del menú anterior: 2
    
    Cantidad a ingresar: 125
    Tu nuevo saldo es de: $ 125.00
    -------------------------------
    
    ***   Bienvenido a tu cuenta de Banco Azteca   ***
    [1].- Consultar saldo.
    [2].- Ingresar dinero.
    [3].- Retirar dinero.
    [0].- Salir.
    
    Elige una opción del menú anterior: 3
    
    Cantidad a retirar: 130
    Saldo insuficiente.
    -------------------------------
    
    ***   Bienvenido  tu cuenta de Banco Azteca   ***
    [1].- Consultar saldo.
    [2].- Ingresar dinero.
    [3].- Retirar dinero.
    [0].- Salir.
    
    Elige una opción del menú anterior: 1
    
    Tu saldo es de: $ 125.00
    -------------------------------
    
    ***   Bienvenido a tu cuenta de Banco Azteca   ***
    [1].- Consultar saldo.
    [2].- Ingresar dinero.
    [3].- Retirar dinero.
    [0].- Salir.
    
    Elige una opción del menú anterior: 123
    
    Opción no válida.
    -------------------------------
    
    ***   Bienvenido a tu cuenta de Banco Azteca   ***
    [1].- Consultar saldo.
    [2].- Ingresar dinero.
    [3].- Retirar dinero.
    [0].- Salir.
    
    Elige una opción del menú anterior: 0
    
    -------------------------------
    
    Nos vemos.
"""