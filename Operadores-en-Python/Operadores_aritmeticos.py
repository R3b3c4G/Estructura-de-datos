'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Ejemplos de uso de los operadores aritméticos.
'''

"""
Los operadores aritméticos en Python son los siguientes:
- Suma (+).
- Resta (-).
- Multiplicación (*).
- División (/).
- División entera (//).
- Módulo (%).
- Exponenciación (**).
"""

# Se solicitan dos números enteros al usuario.
numero1 = int(input("Ingresa un número entero: "))
# Para el segundo valor se evita el cero, ya que matemáticamente no es válido una división entre cero.
# El cero como divisor causaría un error en el programa al momento de hacer la división.
numero2 = int(input("Ingresa otro número entero diferente de 0: "))

# Se realizan las operaciones aritméticas.
print()
print("  ***   Ejemplos de uso de los operadores aritméticos   ***")
print(f"La suma de ({numero1} + {numero2}) es: {numero1 + numero2}.")
print(f"La resta de ({numero1} - {numero2}) es: {numero1 - numero2}.")
print(f"La multiplicación de ({numero1} * {numero2}) es: {numero1 * numero2}.")
# La división (/) retorna un resultado con decimal.
print(f"La división de ({numero1} / {numero2}) es: {(numero1 / numero2):.2f}.")    # Notar la forma para mostrar dos decimales.
# La división entera (//) retorna solo la parte entera del resultado.
print(f"La división entera de ({numero1} // {numero2}) es: {numero1 // numero2}.")
# El módulo da como resultado el residuo de la división entera.
print(f"El módulo de ({numero1} % {numero2}) es: {numero1 % numero2}.")
print(f"La exponenciación  de ({numero1} ** {numero2}) es: {numero1 ** numero2}.")

"""
# Resultado en consola:

    Ingresa un número entero: 10
    Ingresa otro número entero diferente de 0: 7
    
      ***   Ejemplos de uso de los operadores aritméticos   ***
    La suma de (10 + 7) es: 17.
    La resta de (10 - 7) es: 3.
    La multiplicación de (10 * 7) es: 70.
    La división de (10 / 7) es: 1.43.
    La división entera de (10 // 7) es: 1.
    El módulo de (10 % 7) es: 3.
    La exponenciación  de (10 ** 7) es: 10000000.
    
      ***   Ejemplos de uso de los operadores aritméticos   ***
    La suma de (0 + 10) es: 10.
    La resta de (0 - 10) es: -10.
    La multiplicación de (0 * 10) es: 0.
    La división de (0 / 10) es: 0.00.
    La división entera de (0 // 10) es: 0.
    El módulo de (0 % 10) es: 0.
    La exponenciación  de (0 ** 10) es: 0.
"""
