"""
Todas las clases si no indicamos de cual heredan, van a heredar de la clase padre que es la "Object"
En este caso, clase "Persona" hereda de la clase "Object" y la clase "Empleado" de la clase "Persona"

Object = Padre de todos
Persona = Padre
Empleado = hijo
"""


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):  # Funciona para sobrescribir los datos en la clase padre y poderse imprimir en pantalla
        return f'Persona[Nombre: {self.nombre}, Edad: {self.edad}]'


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)  # "super" permite acceder a los atrib. y metodos definidos en la clase padre
        self.sueldo = sueldo

    def __str__(self):
        return f'Empleado: [Sueldo: {self.sueldo}]{super().__str__()}'
