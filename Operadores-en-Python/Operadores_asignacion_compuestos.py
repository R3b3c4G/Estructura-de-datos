'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Ejemplos de uso de los operadores de asignación compuestos.
'''

"""
Los operadores de asignación compuestos son una forma abreviada de realizar una operación aritmética y una asignación
en una sola línea de código. Combinan un operador aritmético (como suma, resta, multiplicación, división, etc.) 
con el operador de asignación (=).
"""

# Se solicita un número para realizar diferentes operaciones de asignación compuestas.
numero = int(input("Ingresa un número: "))
print(f"Valor ingresado: {numero}.")
# Suma.
numero+=20      # Equivale a numero = numero + 20.
print(f"Nuevo valor (+20): {numero}.")
# Resta.
numero-=4       # Equivale a numero = numero - 4.
print(f"Nuevo valor (-4): {numero}.")
# Multiplicación.
numero*=2       # Equivale a numero = numero * 2.
print(f"Nuevo valor (*2): {numero}.")
# División.
numero/=5       # Equivale a numero = numero / 5.
print(f"Nuevo valor (/5): {numero:.2f}.")


# Ejemplo. ¿Qué se obtiene cuando los números ingresados son 8 y 7?
print()
numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa otro número: "))

numero1 += numero2
numero1 += 2
numero1 *= 5
numero2 -= 3
numero1 /= numero2

print(f"Resultado de las operaciones sobre el primer número: {numero1}.")
print(f"Resultado de las operaciones sobre el segundo número: {numero2}.")

"""
# Resultado en consola:
    Ingresa un número: 4
    Valor ingresado: 4.
    Nuevo valor (+20): 24.
    Nuevo valor (-4): 20.
    Nuevo valor (*2): 40.
    Nuevo valor (/5): 8.00.
    
    Ejemplo: 
    Resultado de cuando los números ingresados son 8 y 7.
    # 8.
    Resultado de las operaciones sobre el primer número: 21.25.
    # 7.
    Resultado de las operaciones sobre el segundo número: 4.
"""

'''
*NOTA: Los operadores de asignación compuestos se utilizan para asignar valores a variables, mientras 
       que los operadores aritméticos se usan para realizar operaciones matemáticas.
'''
