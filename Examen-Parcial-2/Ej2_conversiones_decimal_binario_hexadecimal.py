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
    return binario
valores_hexadecimal ={'0':'0', '1':'1', '2':'2', '3':'3', '4':'4', '5':'5',
                      '6':'6', '7':'7', '8':'8', '9':'9', '10':'A', '11':'B',
                      '12':'C', '13':'D', '14':'E', '15':'F'
                     }
def decimal_hexadecimal(decimal):
    hexadecimal = str()
    while decimal >= 0:
            residuo = decimal % 16
            if residuo < 10:
                hexadecimal = str(residuo) + hexadecimal
            else:
                for residuo in valores_hexadecimal:
                    hexadecimal = valores_hexadecimal[residuo] + hexadecimal
            decimal = decimal // 16
    return hexadecimal

def binario_decimal (binario):
    decimal = 0
    for c in binario:
        if c == 1:
            decimal += 2 ** c
    return decimal

def binario_hexadecimal(binario):
    decimal = binario_decimal(binario)
    hexadecimal = decimal_hexadecimal(decimal)
    return hexadecimal

def hexadecimal_decimal (hexadecimal):

def hexadecimal_binario (hexadecimal):
    decimal = hexadecimal_decimal(hexadecimal)
    binario = decimal_binario(decimal)
    return binario



#.
opcion = menu()
if opcion == 1:
    decimal = int(input("Ingrese el número en base decimal: "))
    print(f" El número decimal {decimal} es {decimal_binario(decimal)} en binario y {decimal_hexadecimal(decimal)} en hexadecimal.")
if opcion == 2:
    binario = int(input("Ingrese el número en base binario: "))
    print(f" El número decimal {binario} es {binario_decimal(binario)} en decimal y {binario_hexadecimal(binario)} en hexadecimal.")
if opcion == 3:
    hexadecimal = int(input("Ingrese el número en base hexadecimal: "))
    print(f" El número hexadecimal {hexadecimal} es {hexadecimal_decimal(hexadecimal)} en decimal y {hexadecimal_binario(hexadecimal)} en binario.")


