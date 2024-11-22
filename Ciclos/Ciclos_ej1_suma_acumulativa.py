'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa calculará la suma acumulativa del cero hasta un número ingresado por el usuario.

INSTRUCCIONES:
Escribe un programa de nombre Ciclos_ej1_suma_acumulativa.py que realice lo siguiente:
    a) Solicite al usuario un número mayor a cero que será el número hasta donde se realizará la suma.
    b) Calcule la suma acumulativa.
    c) Muestre el resultado de la suma.
'''
resultado = 0
contador = 0
print("***   Programa que calcula la suma acumulativa    ***")
numero=int(input("Ingresa el número final: "))  # a) Solicite al usuario un número mayor a cero que será el número hasta donde se realizará la suma.
if numero>0:
    while contador<=numero:
        resultado = resultado + contador    # b) Calcule la suma acumulativa.
        contador+=1
        print()
        print(f"La suma de 0 hasta {numero} es: {resultado}.")  # Muestre el resultado de la suma.
else:
    print("Valor no válida.")
print("\nFin del programa.")
"""
# Resultado en consola:
    ***   Programa que calcula la suma acumulativa    ***
    Ingresa el número final: 1
    
    La suma de 0 hasta 1 es: 1.
    
    Fin del programa.
    
    
    ***   Programa que calcula la suma acumulativa    ***
    Ingresa el número final: 2
    
    La suma de 0 hasta 2 es: 3.
    
    Fin del programa.
    
    
    ***   Programa que calcula la suma acumulativa    ***
    Ingresa el número final: 3
    
    La suma de 0 hasta 3 es: 6.
    
    Fin del programa.
    
    
    ***   Programa que calcula la suma acumulativa    ***
    Ingresa el número final: 5
    
    La suma de 0 hasta 5 es: 15.
    
    Fin del programa.
    
    
    ***   Programa que calcula la suma acumulativa    ***
    Ingresa el número final: 1000
    
    La suma de 0 hasta 1000 es: 500500.
    
    Fin del programa.
    

    ***   Programa que calcula la suma acumulativa    ***
    Ingresa el número final: 100
    
    La suma de 0 hasta 100 es: 5050.
    
    Fin del programa.
    
    
    ***   Programa que calcula la suma acumulativa    ***
    Ingresa el número final: -2
    Valor no válida.
    
    Fin del programa.
"""