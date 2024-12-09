# lista-> contenido heterogenea
'''
-> Conjuntos. Desordenado e inmutables.
No tienen indice pero pueden
no se repitan
'''
"""
lista->[]
tupla->()
diccionario->{{}
"""
print("***  Ejmplo de usos de los conjuntos ***")
# crear un conjunto vacio
conjunto_nombres = set()
# Diccionario vacio
# conjunto_noombres = {}
print(f"Conjunto vacio: {conjunto_nombres}")
# Se añaden valores al conjunto.
print()
conjunto_nombres.add("Rebeca")
conjunto_nombres.add("Juan")
conjunto_nombres.add("Bryan")
conjunto_nombres.add("Yamileth")
conjunto_nombres.add("Héctor")
conjunto_nombres.add("Tania")
conjunto_nombres.add("Jenni")
conjunto_nombres.add("Rosa")
conjunto_nombres.add("Gali")
conjunto_nombres.add("Addi")

print(f"Conjunto 303: {conjunto_nombres}")
print()
# Añadiendo elementos repetidos
conjunto_nombres.add("Rebeca")
print(f"Conjunto 303: {conjunto_nombres}")
# Eliminar elementos de un conjunto
# en la lista se busca el elemento
## Se eliminan elementos del conjunto
print()
conjunto_nombres.remove("Rebeca")
print(f"Conjunto 303: {conjunto_nombres}")
# Mostrar todos los elementos
# nombre elemento individual
print()
for nombre in conjunto_nombres:
    print(nombre, end=", ")
print(f"Conjunto 303: {conjunto_nombres}")
# verificar si un elemento pertenece a un conjunto.
# print ("Elemento nombre pertenece al conjunto? {nombre in conjunto_nombres}
print()
print (f"Elemento Addi pertenece al conjunto? {"Addi" in conjunto_nombres}")
print (f"Elemento Sam pertenece al conjunto? {"Sam" in conjunto_nombres}")
# Nuevo conjunto de números
conjunto_numeros = {12.1,1.2,3.2,-2.3,4,1}
# Funciones básicas
print(f"Tamaño del conjunto: {len(conjunto_numeros)}")
print(f"Suma de todos los elementos: {sum(conjunto_numeros)}")