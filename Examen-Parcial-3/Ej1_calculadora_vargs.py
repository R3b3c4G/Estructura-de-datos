def menu() -> int:
    print("[1]  Suma.")
    print("[2]  Multiplicación.")
    print("[0]  Salir")
    opcion = input("Seleccione una opción: ")
    numero = validar_opcion(opcion)
    print(numero)
    while numero != 0 and numero != 1 and numero != 2:
        opcion = input("Valor fuera de rango, ingresa nuevamente: ")
        numero = validar_opcion(opcion)
    return numero

def validar_opcion(opcion:str)-> int:
    while not opcion.isnumeric():
        print("Opción no válida.")
        opcion = input("Intenta nuevamente: ")
    return int(opcion)

def cadena_a_flotante(cadena: str)->float:
    no_puntos = cadena.count(".")
    no_guiones = cadena.count("-")
    revisar_cadena =cadena.lstrip('-').replace(".","")
    if revisar_cadena.isnumeric() and no_guiones in (0, 1) and no_puntos in (0, 1):
        return float(cadena)
    else:
        return None

def sumar(*vargs)-> float:
    resultado = 0
    for i in vargs:
        resultado += i
    return resultado

def multiplicar(*vargs)-> float:
    if not vargs:  # Para tupla vacia
        return 0
    resultado = 1
    for i in vargs:
        resultado *= i
    return resultado

lista_numeros = []
opcion = menu()
print("Para salir en cualquier momento, ingrese '2005'")

if opcion != 0:
    while True:
        num_cadena = input("Ingresa un número: ")
        if num_cadena == "2005":
            break
        numero = cadena_a_flotante(num_cadena)
        if numero is not None:
            lista_numeros.append(numero)
        else:
            print("Opción no válida, intenta nuevamente.")

    tupla = tuple(lista_numeros)
    if opcion == 1:
        resultado = sumar(*tupla)
        print("El resultado de la suma es: ", resultado)
    elif opcion == 2:
        resultado = multiplicar(*tupla)
        print("El resultado de la multiplicación es:", resultado)
print("\nFin del programa.")