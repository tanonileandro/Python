"""
1) Haremos uso del archivo creado anteriormente persona.py que es un modulo, en este archivo. Esto se puede hacer entre
archivos..

2) En este modulo que vamos a importar solo tenemos la clase Persona, pero puede haber mas clases en un modulo e
importar todas las que quisiésemos.
Si quisiesemos imporar todas las clases incluyendo sus funciones y demas deberiamos hacer Ej: "from Persona import *"

3) Para que NO se ejecute el print del modulo persona.py en este y solo se traiga la clase, se usara una validacion if
en el modulo
persona.py o en este mismo modulo tambien, es indistinto.
"""

from Persona import Persona

print('Creacion de Objetos'.center(50, '-'))
persona1 = Persona('Carla', 'Gomez', 29)
persona1.mostrar_detalles()

print('\n')

print('Eliminacion de Objetos'.center(50, '-'))
del persona1  # Forma no tan comun de eliminar un objeto
