"""
1) Para potenciar el Metodo __init__ se le agrega en los parametros una tupla de valores *args o con otro nombre,
y se le agrega un diccionario **kwargs
Aunque, no es necesario agregarles a todos los objetos creados valores en la tupla o diccionario, ya que son valores
opcionales.

2) Por otra parte, para encapsular un elemento y que no se pueda modificar,  en los atributos se escribe un guion
bajo antes del mismo, eso significa que solo podremos acceder a ese atributo dentro de la misma clase. No se podra
acceder fuera, es una regla gramatical.

Ej:
class Persona():
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

    def mostrar_detalles(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')


persona1 = Persona('Leandro', 'Tanoni', 27, '3329330838', 5, 3, 4, b='Banana', m='Manzana')
persona1.mostrar_detalles()

persona1._nombre = 'Juan carlos'  ->  esto no se podra hacer, solo desde dentro de la clase como se indica arriba

3) Para seguir encapsulando un atriburto se hace uso del metodo get y set
    get = obtener/recuperar
    set = colocar/modificar

4) Para acceder y solo leer un atributo se usa el metodo read-only, eliminamos la parte de set, y la parte de
persona1.nombre = 'Juan', ya que al sacar la parte set, esto nos mandaria un error porque no se podria modificar...
"""


class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self.valores = valores
        self.terminos = terminos

    @property  # Este decorador modifica al metodo para que podamos acceder como si fuese un atributo
    def nombre(self):  # Metodo get, este solo toma el valor de set para enviarlo a imprimir en pantalla
        return self._nombre

    @nombre.setter  # Metodo set, este modifica el valor del atributo nombre
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Persona: {self._nombre} {self._apellido} {self._edad} {self.valores} {self.terminos}')


persona1 = Persona('Leandro', 'Tanoni', 27, '3329330838', 5, 3, 4, b='Banana', m='Manzana')
persona1.mostrar_detalles()

# Modificamos los valores para ver como funciona el metodo set y get
persona1.nombre = 'Juan'
persona1.apellido = 'Rodriguez'
persona1.edad = 35
persona1.mostrar_detalles()

