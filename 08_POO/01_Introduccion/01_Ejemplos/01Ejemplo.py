"""
# La palabra reservada "pass", sirve cuando no queremos agregar contenido a una funcion o clase,
# lo dejamos pasar por alto en el momento para agregarlo mas tarde..

class Persona:

    # Metodo inicializador para agregar atributos en una clase, self es un parametro al objeto que se va a agregar
    # El metodo __init__ se lo conoce como "double underscore = dunder" por sus doble guin bajo
    def __init__(self):

        # Ahora se agregaran atributos para nuestros objetos, "Atributos de instancia"
        # Esta no es la manera correcta, la correcta es por medio de parametros..
        self.nombre = 'Leandro'
        self.apellido = 'Tanoni'
        self.edad = 27

# Crear un objeto de la clase
# Se declara una variable que almacene la referencia a nuestro objeto
persona1 = Persona()
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
"""


# Forma correcta de escribir una clase

class Persona:
    def __init__(self, nombre, apellido, edad):  # Se colocan los parametros que van a igual a los atributos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad  # "self.atributo = parametro" llevan por lo general el mismo nombre..


# Se crea el primer objeto:
persona1 = Persona('Juan', 'Perez', 33)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
# Otra forma de imprimirlo en pantalla en una sola linea:
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad} \n')

# Para crear un segundo objeto:
persona2 = Persona('Leandro', 'Tanoni', 28)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad} \n')

# Reasignacion de valores
# Se pueden reasignar uno o todos los valores..
persona1.nombre = 'Juan Carlos'
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad} \n')

