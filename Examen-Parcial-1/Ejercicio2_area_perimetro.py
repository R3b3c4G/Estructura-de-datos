'''
Nombre: Rebeca Gregorio Espina.
Fecha: 3 de noviembre de 2024.
Descripción:
Este programa determina el área y el perímetro de un rectángulo o de un círculo.

INSTRUCCIONES:
Escribe un programa de nombre Ejercicio2_area_perimetro.py y sube el enlace de GitHub.
Muestre el siguiente menú:
    1) Calcular el área de un rectángulo.
    2) Calcular el perímetro de un rectángulo.
    3) Calcular el área de un círculo.
    4) Calcular el perímetro de un círculo.
    0) Salir.
Cualquier otro caso -> Mostrar un mensaje de "opción no válida".

Para ello:
    a) Muestre el menú anterior en consola.
    b) En caso de calcular un área o perímetro, solicite al usuario los valores requeridos (flotantes).
    c) Utilice la lógica adecuada para calcular lo solicitado. Asuma pi = 3.1416.
    d) Imprima el resultado en la consola. Nota: muestre únicamente 3 decimales en todos los casos.
    e) Repita el menú hasta salir.
'''
opcion = 1
pi = 3.1416 # Declarando a pi como un valor constante.
while opcion != 0 :
    # a) Muestre el menú anterior en consola.
    print("*** Programa que calcula el área y perímetro   ***")
    print("[1].- Calcular el área de un rectángulo.")
    print("[2].- Calcular el perímetro de un rectángulo.")
    print("[3].- Calcular el área de un círculo.")
    print("[4].- Calcular el perímetro de un círculo.")
    print("[0].- Salir.")
    opcion = int(input("Ingrese una de las opciones anteriores: "))
    if opcion != 0:
        print()
        # b) En caso de calcular un área o perímetro, solicite al usuario los valores requeridos (flotantes).
        # c) Utilice la lógica adecuada para calcular lo solicitado.
        if opcion == 1:     # Calcular el área de un rectángulo.
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            print(f"\nEl área es: {base * altura:.3f}")
        elif opcion == 2:       # Calcular el perímetro de un rectángulo.
            base = float(input("Ingrese la base: "))
            altura = float(input("Ingrese la altura: "))
            print(f"\nEl perímetro es: {(base * 2) + (altura * 2):.3f}")
        elif opcion == 3:       #  Calcular el área de un círculo.")
           radio= float(input("Ingrese el radio: "))
           print(f"\nEl área es: {pi * (radio **  2):.3f}")
        elif opcion == 4:  # Calcular el perímetro de un círculo.")
           radio = float(input("Ingrese el radio: "))
           print(f"\nEl perímetro es: {2 * pi * radio:.3f}")
        else:       # Cualquier otro caso -> Mostrar un mensaje de "opción no válida".
            print("Opción no válida")
        print("----------------------------------------------------")
    print()
print("Saliendo del programa...")

# d) Imprima el resultado en la consola. Nota: muestre únicamente 3 decimales en todos los casos.
# e) Repita el menú hasta salir.
""""
# Resultados en consola:
    *** Programa que calcula el área y perímetro   ***
    [1].- Calcular el área de un rectángulo.
    [2].- Calcular el perímetro de un rectángulo.
    [3].- Calcular el área de un círculo.
    [4].- Calcular el perímetro de un círculo.
    [0].- Salir.
    Ingrese una de las opciones anteriores: 1
    
    Ingrese la base: 12.3
    Ingrese la altura: 2.1
    
    El área es: 25.830
    ----------------------------------------------------
    
    *** Programa que calcula el área y perímetro   ***
    [1].- Calcular el área de un rectángulo.
    [2].- Calcular el perímetro de un rectángulo.
    [3].- Calcular el área de un círculo.
    [4].- Calcular el perímetro de un círculo.
    [0].- Salir.
    Ingrese una de las opciones anteriores: 2
    
    Ingrese la base: 11.1
    Ingrese la altura: 2.1
    
    El perímetro es: 26.400
    ----------------------------------------------------
    
    *** Programa que calcula el área y perímetro   ***
    [1].- Calcular el área de un rectángulo.
    [2].- Calcular el perímetro de un rectángulo.
    [3].- Calcular el área de un círculo.
    [4].- Calcular el perímetro de un círculo.
    [0].- Salir.
    Ingrese una de las opciones anteriores: 3
    
    Ingrese el radio: 1
    
    El área es: 3.142
    ----------------------------------------------------
    
    *** Programa que calcula el área y perímetro   ***
    [1].- Calcular el área de un rectángulo.
    [2].- Calcular el perímetro de un rectángulo.
    [3].- Calcular el área de un círculo.
    [4].- Calcular el perímetro de un círculo.
    [0].- Salir.
    Ingrese una de las opciones anteriores: 4
    
    Ingrese el radio: 1
    
    El perímetro es: 6.283
    ----------------------------------------------------
    
    *** Programa que calcula el área y perímetro   ***
    [1].- Calcular el área de un rectángulo.
    [2].- Calcular el perímetro de un rectángulo.
    [3].- Calcular el área de un círculo.
    [4].- Calcular el perímetro de un círculo.
    [0].- Salir.
    Ingrese una de las opciones anteriores: 3
    
    Ingrese el radio: 21.2
    
    El área es: 1411.961
    ----------------------------------------------------
    
    *** Programa que calcula el área y perímetro   ***
    [1].- Calcular el área de un rectángulo.
    [2].- Calcular el perímetro de un rectángulo.
    [3].- Calcular el área de un círculo.
    [4].- Calcular el perímetro de un círculo.
    [0].- Salir.
    Ingrese una de las opciones anteriores: 12345
    
    Opción no válida
    ----------------------------------------------------
    
    *** Programa que calcula el área y perímetro   ***
    [1].- Calcular el área de un rectángulo.
    [2].- Calcular el perímetro de un rectángulo.
    [3].- Calcular el área de un círculo.
    [4].- Calcular el perímetro de un círculo.
    [0].- Salir.
    Ingrese una de las opciones anteriores: 1
    
    Ingrese la base: 123.4
    Ingrese la altura: 1
    
    El área es: 123.400
    ----------------------------------------------------
    
    *** Programa que calcula el área y perímetro   ***
    [1].- Calcular el área de un rectángulo.
    [2].- Calcular el perímetro de un rectángulo.
    [3].- Calcular el área de un círculo.
    [4].- Calcular el perímetro de un círculo.
    [0].- Salir.
    Ingrese una de las opciones anteriores: 0
    
    Saliendo del programa...

"""