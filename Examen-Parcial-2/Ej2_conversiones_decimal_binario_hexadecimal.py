'''
Nombre: Rebeca Gregorio Espina.
Fecha: 8 de diciembre del 2024.
Descripción:
Este programa convierte números entre las bases decimal, binaria y hexadecimal.
Se debe mostrar el siguiente menú:
      ***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***
    1) Convertir de decimal a binario y hexadecimal.
    2) Convertir de binario a decimal y hexadecimal.
    3) Convertir de hexadecimal a decimal y binario.
    0) Salir.
    Cualquier otro caso -> Opción no válida.
Para ello:
    a) Utilice la lógica adecuada para mostrar las conversiones. No utilice funciones como bin() o hex().
    b) Asuma que el usuario siempre va a ingresar números en el formato adecuado. Por ejemplo: 1001 como número binario o 1F como hexadecimal, no 120 como número binario o 1Z como hexadecimal.
    c) Para considerar el ejercicio como completo, utilice funciones para mostrar el menú y para las conversiones entre bases, considerando que cada función devuelve una tupla. Por ejemplo, la función que recibe el número decimal debe devolver el valor en binario y en hexadecimal como una tupla.
'''

def menu():
    print(" ***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print("     [1].- Convertir de decimal a binario y hexadecimal.")
    print("     [2].- Convertir de binario a decimal y hexadecimal.")
    print("     [3].- Convertir de hexadecimal a decimal y binario.")
    print("     [0].- Salir.")
    opcion = int(input("Ingrese una de las opciones anteriores: "))
    return opcion

def decimal_binario(decimal):
    binario = str()
    if decimal == 0:
        binario = decimal
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario # Convertimos el residuo en una cadena y se concatena con la cadena "binario".
        decimal = decimal // 2
    print(f"La conversion a binaria es {binario}")

def decimal_hexadecimal(decimal):
    hexadecimal = str()
    while decimal >= 0:
        if decimal < 10:
            hexadecimal = decimal
        else:
            binario = str(residuo) + binario  # Convertimos el residuo en una cadena y se concatena con la cadena "binario".
        decimal = decimal // 2
    print(f"La conversion a binaria es {binario}")



opcion = menu()
if opcion == 1:
    decimal = int(input("Ingrese su número decimal: "))
    decimal_binario(decimal)
