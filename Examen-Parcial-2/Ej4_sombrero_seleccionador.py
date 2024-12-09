'''
Nombre: Rebeca Gregorio Espina.
Fecha: 8 de diciembre del 2024.
Descripción:
Este programa es un test de la elección del sombrero seleccionador de Harry Potter para alguna de las casas: Gryffindor, Slytherin, Hufflepuff y Ravenclaw.
Al final este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que perteneces, de acuerdo a tus respuestas.
Ejemplos de preguntas:
    ¿Cuál de las siguientes opciones odiarías más que la gente te llamara?
        Gryffindor - Ordinario.
        Slytherin - Ignorante.
        Hufflepuff - Cobarde.
        Ravenclaw - Egoísta.

    Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?
        Gryffindor - Te extraña, pero sonríe.
        Slytherin - Pide más historias sobre tus aventuras.
        Hufflepuff - Piensa con admiración tus logros.
        Ravenclaw - No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta.

    Dada la opción, preferirías inventar una poción que garantizara:
        Gryffindor - Gloria.
        Slytherin - Sabiduría.
        Hufflepuff - Amor.
        Ravenclaw - Poder.

    ¿Cómo te definirías en una sola palabra?
        Gryffindor - Valiente.
        Slytherin - Ambicioso.
        Hufflepuff - Leal.
        Ravenclaw - Curioso.

    ¿Qué cualidad te describe mejor?
        Gryffindor - La fuerza.
        Slytherin - La astucia.
        Hufflepuff - La paciencia.
        Ravenclaw - La inteligencia.

    ¿Cuál es tu clase favorita?
        Gryffindor - Vuelo.
        Slytherin - Defensa contra las artes oscuras.
        Hufflepuff - Animales fantásticos.
        Ravenclaw - Pociones.

    ¿Cuál es tu lenguaje de programación favorito?
        Gryffindor - C.
        Slytherin - Python.
        Hufflepuff - C++.
        Ravenclaw - JavaScript.


Se debe mostrar la siguiente pantalla inicial:
      ***  Ejercicio 4. Test del sombrero seleccionador de Harry Potter.  ***
    Este programa determina la casa (Gryffindor, Slytherin, Hufflepuff y Ravenclaw) a la que perteneces, de acuerdo a tus respuestas.
    1) Iniciar test.
    0) Salir.
    Cualquier otro caso -> Opción no válida.

Para ello:
    a) Realice al menos 5 preguntas al usuario. Puede utilizar las 7 aquí presentadas.
    b) El orden de las respuestas presentadas no debe ser el mismo al repetir el test. Se recomienda combinar conjuntos, listas y diccionarios para este fin.
    c) Utilice la lógica adecuada para determinar la casa con base en las respuestas.
    d) Muestre la casa al final del test y finalice el programa.
Gryffindor = "Gryffindor."
Slytherin = "Slytherin."
Hufflepuff = "Hufflepuff"
Ravenclaw = "Ravenclaw"
'''
from random import choice


def menu():
    print("***  Ejercicio 4. Test del sombrero seleccionador de Harry Potter.  ***")
    print("     [1].- Iniciar test.")
    print("     [0].- Salir.")
    opcion = int(input("\nIngrese una de la opciones:"))
    return opcion
"""
def casa_perteneciente():
    casa = contador['Gryffindor']
    if casa < contador['Slytherin']:
        casa = contador ['Slytherin']
    elif casa < contador ['Hufflepuff']:
        casa = contador ['Hufflepuff']
    elif casa < contador ['Ravenclaw']:
    print(f"Perteneces a la casa: {casa}")

def pregunta(preguntas, contadpr):
    for a in preguntas:
        print(a['pregunta'])
        lista_opcion = list('opciones')
        print(choice(lista_opcion))

preguntas = [{'pregunta':'a) ¿Cuál de las siguientes opciones odiarías más que la gente te llamara?',
                  'opciones':{'Griffindor':'Ordinario.', 'Slytherin':'Ignorante.', 'Hufflepuff':'Cobarde', 'Ravenclaw':'Egoísta.'}
                  },
                 {'pregunta': 'b) ¿Después de tu muerte ¿qué es lo que más le gustaría que hiciera la gente cuando escuche su nombre?',
                  'opciones': {'Griffindor': 'Te extraña, pero sonríe.', 'Slytherin': 'Pide más historias sobre tus aventuras.',
                  'Hufflepuff':' Piensa con admiración tus logros.', 'Ravenclaw': 'No me importa lo que piensen de mí después de mi muerte, lo que piensen de mí ahora es lo que cuenta.'}
                  },
                 {'pregunta': 'c) Dada la opción, preferirías inventar una poción que garantizara:',
                  'opciones': {'Griffindor': 'Gloria.', 'Slytherin': 'Sabiduría.', 'Hufflepuff': ' Amor.', 'Ravenclaw': 'Poder.'}
                  },
                 {'pregunta': 'd) ¿Cómo te definirías en una sola palabra?',
                  'opciones': {'Griffindor': 'Valiente.', 'Slytherin': 'Ambicioso.', 'Hufflepuff': ' Leal.', 'Ravenclaw': 'Curioso.'}
                  }]
contador =  {'Gryffindor': 0,'Slytherin': 0,'Hufflepuff': 0,'Ravenclaw': 0}
opcion = menu()"""
