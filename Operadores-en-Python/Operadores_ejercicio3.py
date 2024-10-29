'''
Nombre: Rebeca Gregorio Espina.
Fecha: 28 de octubre de 2024.
Descripción:
Este programa determinará si un usuario se autentifica correctamente con su usuario y contraseña.

INSTRUCCIONES:
Escribe un programa de nombre Operadores_ejercicio3.py que realice lo siguiente:
    a) Internamente declare dos cadenas constantes, una para el usuario y otra para la contraseña.
    b) Pida al usuario una cadena con el usuario.
    c) Pida al usuario una cadena con la contraseña.
    d) Si ambas cadenas son iguales a las cadenas declaradas internamente, entonces el usuario se autenticó correctamente.
    e) Muestre el resultado en consola como valor booleano (True/False).

Nota: Las cadenas no tienen que ser convertidas a minúsculas.
'''
print("**   Sistema de autentificación  **")
# a) Internamente declare dos cadenas constantes, una para el usuario y otra para la contraseña.
# Constante para usuario.
usuario="Alumnos"
# Constante para contraseña.
contraseña="Python"
# b) Pida al usuario una cadena con el usuario.
usuario2=input("Ingresa tu usuario: ")
contraseña2=input("Ingresa tu contraseña: ")
print()
# d) Si ambas cadenas son iguales a las cadenas declaradas internamente, entonces el usuario se autenticó correctamente.
# Verificación de usuario y contraseña.
print(f"El acceso es correcto: {usuario == usuario2 and contraseña == contraseña2}.")
# e) Muestre el resultado en consola como valor booleano (True/False).
"""
Resultado en consola:
    # Prueba 1.
    **   Sistema de autentificación  **
    Ingresa tu usuario: alumnos
    Ingresa tu contraseña: python
    
    El acceso es correcto: False.
    
      # Prueba 2.
        **   Sistema de autentificación  **
    Ingresa tu usuario: Alumnos
    Ingresa tu contraseña: Python
    
    El acceso es correcto: True.
"""

