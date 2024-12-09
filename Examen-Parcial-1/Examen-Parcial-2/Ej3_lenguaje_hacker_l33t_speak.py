'''
Nombre: Rebeca Gregorio Espina.
Fecha: 8 de diciembre del 2024.
Descripción:
Este programa convierte un texto al lenguaje hacker (lenguaje leet o 1337). Esta escritura se caracteriza por reemplazar las letras por números y símbolos.
Lenguaje básico:
En el lenguaje básico se sustituye cada vocal por un número.
La A se convierte en un 4, la E en un 3, la I en un 1 y la O en un cero.
La letra U es una excepción, ya que no hay un número obvio, por lo que se sustituye por (_).

Lenguaje intermedio:
En el lenguaje intermedio también se sustituyen las consonantes por números o signos de puntuación.
Por ejemplo, la B se convierte en I3, la C en [, la D en ), la L en 1.
Revisa la "Leet speak alphabet" de la página anterior y toma la primera de las opciones para el lenguaje.
Nota que no hay caracteres acentuados, por lo que no se deben de convertir.


Se debe mostrar el siguiente menú:
      ***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***
    1) Convertir un texto a lenguaje básico.
    2) Convertir un texto a lenguaje intermedio.
    0) Salir.
    Cualquier otro caso -> Opción no válida.

Para ello:
    a) Utilice la lógica adecuada para convertir el texto al lenguaje hacker básico o intermedio, según sea el caso.
    b) Se debe convertir los caracteres sin importar si son mayúsculas o minúsculas, sin modificar los caracteres que no se convirtieron. Ejemplos con el lenguaje básico: hola -> h0l4, Hola -> H0l4, HOLA -> H0L4.
'''

def menu(): # Función que imprime el menú y regresa la opción del usuario.
    print("***  Ejercicio 3. Lenguaje hacker (l33t sp34k).  ***")
    print("     [1].- Convertir un texto a lenguaje básico.")
    print("     [2].- Convertir un texto a lenguaje intermedio.")
    print("     [0].- Salir.")
    opcion = int(input("\nIngrese una de la opciones: "))
    return opcion
lenguaje_basico = {'A':'4', 'E':'3', 'I':'1', 'O':'0', 'U':'()',    # Diccionario del lenguaje hacker básico.
               'a':'4', 'e':'3', 'i':'1', 'o':'0', 'u':'()'
               }
lenguaje_intermedio = {'B':'I3', 'C':'[', 'D':')', 'F':'|=', 'G':'&', 'H':'#', 'J':',_|',   # Diccionario del lenguaje hacker intermedio.
                   'K':'>|', 'L':'1', 'M':'/\/\\', 'N':'^/','P':'|*', 'Q':'(_,)',
                   'R':'I2', 'S':'5', 'T':'7', 'V':'\/','W':'\/\/', 'X':'><', 'Y':'j', 'Z':'2',

                   'b':'I3', 'c':'[', 'd':')', 'f':'|=', 'g':'&', 'h':'#', 'j':',_|',
                   'k':'>|', 'l':'1', 'm':'/\/\\', 'n':'^/','p':'|*', 'q':'(_,)',
                   'r':'I2', 's':'5', 't':'7', 'v':'\/','w':'\/\/', 'x':'><', 'y':'j', 'z':'2',

                   'A':'4', 'E':'3', 'I':'1', 'O':'0', 'U':'()',
                   'a':'4', 'e':'3', 'i':'1', 'o':'0', 'u':'()'
                   }
conversion = str()# Inicializar una cadena vacía (será un auxiliar para guardar las conversiones).
opcion = menu()
while opcion != 0:
    if opcion == 1:
        mi_texto = input("\nIngresa el texto a convertir a lenguaje l33t básico: ")
        # Crear una nueva cadena en lenguaje hacker básico del texto ingresado.
        for a in mi_texto:
            if a in lenguaje_basico:
                conversion += lenguaje_basico[a]    # Si el caracter de "mi_texto" es igual a alguna de las claves del diccionario "lenguaje_basico", ese caracter se sustituye por el valor de la clave y se agrega a la cadena.
            else:
                conversion += a # Si el caracter de "mi_texto" no es igual a alguna de las claves del diccionario "lenguaje_basico", se deja igual y se agrega a la cadena.
        print(f"\nEl texto convertido es: {conversion}")
    elif opcion == 2:
        mi_texto = input("\nIngresa el texto a convertir a lenguaje l33t intermedio: ")
        # Crear una nueva cadena en lenguaje hacker intermedio del texto ingresado.
        for b in mi_texto:
            if b in lenguaje_intermedio:
                conversion += lenguaje_intermedio[b]     # Si el caracter de "mi_texto" es igual a alguna de las claves del diccionario "lenguaje_intermedio", ese caracter se sustituye por el valor de la clave y se agrega a la cadena.
            else:
                conversion += b # Si el caracter de "mi_texto" no es igual a alguna de las claves del diccionario "lenguaje_intermedio", se deja igual y se agrega a la cadena.
        print(f"\nEl texto convertido es: {conversion}")
    else:
        print("\nOpción no válida.")
    print("--------------------------------\n")
    conversion = str()  # La variable se vuelve a dejar vacío en caso de que el usuario vuelva a ingresar otra cadena de texto.
    opcion = menu()
print("\nFin del programa.")
print("--------------------------------")

