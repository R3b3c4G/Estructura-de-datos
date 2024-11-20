# def -> palabra reservada para crear funciones.
# def hola(nombre):
# tabulador print(f"Hola{nombre})
# Fuera de la función
# hola como nombre de la función
def hola(nombre):
    print(f"Hola {nombre}")

##  DEpuración
# bichito
def menu ():
    print("[1].- Suma")
    print("[2].- Resta")
    print("[3].- Multiplicación")
    print("[4].- División")
    print("[5].- División entera")
    print("[6].- Módulo")
    print("[7].-Potenciación")

def calculadora (opcion, numero1, numero2):
    if opcion == 1:
        resultado = numero1 + numero2
    if opcion == 2:
        resultado= numero1 - numero2
    if opcion == 3:
        resultado = numero1 * numero2
    if opcion == 4:
        resultado = numero1 / numero2
    if opcion == 5:
        resultado = numero1 // numero2
    if opcion == 6:
        resultado = numero1 % numero2
    if opcion == 7:
        resultado = numero1 ** numero2
    return resultado
nombre = input("Ingresa nombre: ")
hola(nombre) # mando a llamar a la función con el argumento nombre
print("Adiós")
menu()
opcion = int(input("Elige una opción: "))
numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa otro número: "))
print(calculadora(opcion, numero1, numero2))