"""
Variables de clase:
    Para acceder a ella no hace falta crear un objeto, ya que esta ligada a la clase en si
    Se puede crear una variable de clase al vuelo, es decir en cualquier momento, aunque no es tan comun
Variable de instancia:
    Para acceder a las variables de instancia si se necesita crear un objeto
    Desde los objetos creados tambien se puede acceder a la variable de clase
Metodos:
    Metodos estaticos: se asocian a la clase en si misma y no con los objetos, tampoco pueden acceder a las variables
    ni a los metodos de instancia..
    Sirve para asociar de manera logica algun metodo que no tenga que ver con los atributos de una clase..
    Metodos de clase: sirven para acceder a las variables de clase directamente
    Metodos instancia: corresponde a los metodos dinamicos, pueden acceder al contexto estatico, metodos de clase,
    variables de clase y de instancia
Contexto:
    Estatico: Se refiere a cuando estamos trabajando con una clase en si misma.
    Dinamico: Cuando ya se crean objetos de cierta clase
"""


class MiClase:
    variable_clase = 'Valor variable clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod  # Decorador que modifica al metodo
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):  # Corresponde a un metodo dinamico
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_instancia)
        print(self.variable_clase)


MiClase.metodo_estatico()
MiClase.metodo_clase()
print(MiClase.variable_clase)
objetoMiClase = MiClase('Valor variable instancia')
objetoMiClase.metodo_instancia()
print(objetoMiClase.variable_instancia)
print(objetoMiClase.variable_clase)  # Desde el objeto podemos acceder a la variable de clase
objetoMiClase.metodo_clase()

MiClase.variable_clase2 = 'Valor variable clase 2'

objetoMiClase2 = MiClase('Valor variable instancia 2')
print(objetoMiClase2.variable_instancia)
print(objetoMiClase2.variable_clase)
print(MiClase.variable_clase2)
print(objetoMiClase2.variable_clase2)
