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
def menu(): # Función que imprime el menú y regresa la opción del usuario.
    print(" ***  Ejercicio 2. Conversión entre las bases decimal, binaria y hexadecimal.  ***")
    print("     [1].- Convertir de decimal a binario y hexadecimal.")
    print("     [2].- Convertir de binario a decimal y hexadecimal.")
    print("     [3].- Convertir de hexadecimal a decimal y binario.")
    print("     [0].- Salir.")
    opcion = int(input("Ingrese una de las opciones anteriores: "))
    return opcion
###
def decimal_a_binario_y_hexadecimal(decimal):   # Función para convertir un número decimal a binario y hexadecimal.
    tupla1 = (decimal_binario(decimal),decimal_hexadecimal(decimal))
    return tupla1 # Devuelve el valor en binario y en hexadecimal como una tupla.

def decimal_binario(decimal):   # Función para convertir un número decimal a binario.
    binario = str()
    while decimal // 2 != 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def decimal_hexadecimal(decimal):   # Función para convertir un número decimal a hexadecimal.
    hexadecimal = str() # Inicializar una cadena vacía.
    while decimal // 16 != 0:
        residuo = decimal % 16
        conversion = valores_hexadecimal(residuo)
        hexadecimal = conversion + hexadecimal
        decimal = decimal // 16
    conversion = valores_hexadecimal(decimal)
    return str (conversion) + hexadecimal

def valores_hexadecimal(residuo):   # Diccionario para establecer los valores del sistema hexadecimal.
    residuo = str(residuo)
    diccionario_valores = {'0': '0', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
                           '6': '6', '7': '7', '8': '8', '9': '9', '10': 'A', '11': 'B',
                           '12': 'C', '13': 'D', '14': 'E', '15': 'F'
                           }
    residuo = str(diccionario_valores.get(residuo)) # Regresa el valor hexadecimal al que pertenece el residuo.
    return residuo

####
def binario_a_decimal_y_hexadecimal(binario):   # Función para convertir un número binaro a decimal y hexadecimal.
    binario = str(binario)
    decimal = binario_decimal(binario)
    tupla2 = (decimal,decimal_hexadecimal(decimal))
    return tupla2   # Devuelve el valor en decimal y en hexadecimal como una tupla.

def binario_decimal (binario):  # Función para convertir un número binario a decimal.
    decimal = 0
    cantidad_binario= (len(binario)) - 1    # Calcula la cantidad de dígitos del binario.
    for i in binario:
        decimal = (2 ** cantidad_binario) * int(i) + decimal    # Calcula el valor decimal del dígito perteneciente a la iteración.
        cantidad_binario -= 1
    return decimal


####
def hexadecimal_a_decimal_y_binario(hexadecimal):   # Función para convertir un número hexadecimal a decimal y binario.
    hexadecimal = str(hexadecimal)
    decimal = 0
    cantidad_hexadecimal = (len(hexadecimal)) - 1   # Calcula la cantidad de dígitos del hexadecimal.
    for i in hexadecimal:
        decimal = (16 ** cantidad_hexadecimal) * int(valores_hexadecimal(i))+ decimal
        cantidad_hexadecimal -= 1
    tupla3 = decimal,decimal_binario(decimal)
    return tupla3   # Devuelve el valor en decimal y en binario como una tupla.

opcion = menu()
while opcion != 0:  # Mientras el usuario no quiera salir.
    print()
    if opcion == 1:
        decimal = int(input("Ingrese el número en base decimal: "))
        binario,hexadecimal = decimal_a_binario_y_hexadecimal(decimal)
        print(f"El número decimal {decimal} es {binario} en binario y {hexadecimal} en hexadecimal.")
    elif opcion  == 2:
        binario = int(input("Ingrese el número en base binaria: "))
        decimal, hexadecimal = binario_a_decimal_y_hexadecimal(binario)
        print(f"El número binario {binario} es {decimal} en decimal y {hexadecimal} en hexadecimal.")
    elif opcion == 3:
        hexadecimal = input("Ingrese el número en base hexadecimal: ")
        decimal, binario = hexadecimal_a_decimal_y_binario(hexadecimal)
        print(f"El número hexadecimal {hexadecimal} es {decimal} en decimal y {binario} en binario.")
    else:
        print("Opción no válida.")
    print("___________________________________________")
    opcion = menu()
print("\nFin del programa.")
print("___________________________________________")
