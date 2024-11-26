'''
Nombre: Rebeca Gregorio Espina.
Fecha: 25 de noviembre del 2024.
Descripción:
Este programa es una lista de compras para el súper. La lista está conformada por varios productos. Cada producto
tiene un nombre y cantidad, por lo que también se sugiere utilizar una lista.

INSTRUCCIONES:
Escribe un programa de nombre Listas_ej2_compras.py que realice lo siguiente:
Se debe mostrar el siguiente menú:

       ***  Lista de compras para el súper  ***
    1) Ver lista de productos.
    2) Añadir producto a la lista.
    3) Eliminar producto de la lista.
    0) Salir.
    Cualquier otro caso -> Opción no válida.

Para ello:
    a) Utilice funciones para modular el código.
    b) Utilice una lista para los productos a añadir, en donde también se sugiere utilizar una lista para los productos,
    es decir, se va a utilizar una lista de listas.
'''
def menu ():    # Función para imprimir menú y devolver opción del usuario.
    print("***  Lista de compras para el súper  ***")
    print("     [1].- Ver lista de productos.")
    print("     [2].- Añadir producto a la lista.")
    print("     [3].- Eliminar producto de la lista.")
    print("     [0].- Salir.")
    opcion = int(input("\nIngresa una de las opciones: "))
    return opcion
def ver_lista (compras):     # Función para ver lista de productos.
    print()
    if len(compras) == 0:
        print("No hay productos para mostrar.")
    else:
        print("Lista de productos: ")
        numero_compra = 1
        for a in compras:
            print(f"{numero_compra}) {a[0]}..... {a[1]}")
            numero_compra += 1
def añadir_producto (compras):  # Función para añadir producto a la lista.
    nombre = input("\nIngresa el nombre del producto: ")
    cantidad = int(input("Ingresa la cantidad: "))
    compras.append([nombre, cantidad])
    print(f"El producto{[nombre, cantidad]} ha sido agregado con éxito!")
def eliminar_producto (compras):    # Función para eliminar producto de la lista.
    print()
    if len(compras) == 0:
        print("No hay productos para eliminar.")
    else:
        eliminar = int(input("Seleccione el índice del producto a eliminar: "))
        compras.pop(eliminar - 1)
        print("El producto ha sido eliminado correctamente.")

compras = [] # Lista de la lista: nombre de productos y cantidad de productos.
opcion = menu()
while opcion != 0:
    if opcion <= 6 and opcion >=0:
        if opcion == 1:
            ver_lista(compras)
        elif opcion == 2:
            añadir_producto(compras)
        elif opcion == 3:
            eliminar_producto(compras)
        print("---------------------------------\n")
    else:
        print("\nOpción no válida.")
        print("---------------------------------\n")
    opcion = menu()
print("\nFin del programa.")
print("---------------------------------\n")

"""
# Resultados en consola:
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 1
    
    No hay productos para mostrar.
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 3
    
    No hay productos para eliminar.
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 2
    
    Ingresa el nombre del producto: azúcar
    Ingresa la cantidad: 2
    El producto['azúcar', 2] ha sido agregado con éxito!
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 2
    
    Ingresa el nombre del producto: leche
    Ingresa la cantidad: 10
    El producto['leche', 10] ha sido agregado con éxito!
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 2
    
    Ingresa el nombre del producto: pan
    Ingresa la cantidad: 3
    El producto['pan', 3] ha sido agregado con éxito!
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 1
    
    Lista de productos: 
    1) azúcar..... 2
    2) leche..... 10
    3) pan..... 3
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 2
    
    Ingresa el nombre del producto: cereal
    Ingresa la cantidad: 1
    El producto['cereal', 1] ha sido agregado con éxito!
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 1
    
    Lista de productos: 
    1) azúcar..... 2
    2) leche..... 10
    3) pan..... 3
    4) cereal..... 1
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 3
    
    Seleccione el índice del producto a eliminar: 2
    El producto ha sido eliminado correctamente.
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 1
    
    Lista de productos: 
    1) azúcar..... 2
    2) pan..... 3
    3) cereal..... 1
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 3
    
    Seleccione el índice del producto a eliminar: 1
    El producto ha sido eliminado correctamente.
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 1
    
    Lista de productos: 
    1) pan..... 3
    2) cereal..... 1
    ---------------------------------
    
    ***  Lista de compras para el súper  ***
         [1].- Ver lista de productos.
         [2].- Añadir producto a la lista.
         [3].- Eliminar producto de la lista.
         [0].- Salir.
    
    Ingresa una de las opciones: 0
    
    Fin del programa.
    ---------------------------------
"""