# Rebeca Gregorio Espina.
# 8 de octubre de 2024.
# En este archivo se ejemplifica el uso de variables en Python.

# Notas:
# En Python todo es un objeto.
# Variable - Una variable es un nombre que almacena un valor guardado en la memoria temporal.

# Toda variable requiere un valor inicial
semestre = 3        # Es una variable que apunta a un objeto de tipo int con valor de 3
print(semestre)     # Imprime el valor de la variable
semestre = 4        # La variable ya no apunta al objeto anterior, sino a uno nuevo, por lo que se pierde la referencia
print(semestre)
#Este programa imprimirá el valor de la variable semestre.
"""
Inicialmente en la primera línea imprimirá 3, pero en como dentro del código la variable semestre
se reasigna con otro valor, esta causa que al volver a imprimir la variable semestre arroje otro valor en la pantalla.

#Resultado en pantalla:
#3
#4
"""