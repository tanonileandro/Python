class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self.valores = valores
        self.terminos = terminos

# Encapsulamiento
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
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

    def __del__(self):  # Metodo destructor, para eliminar
        print(f'Persona: {self._nombre} {self._apellido}')  # Podremos agregar mas datos del objeto eliminado


if __name__ == '__main__':  # validacion para que solo se imprima en este archivo y no en otros
    persona1 = Persona('Leandro', 'Tanoni', 27, '3329330838', 5, 3, 4, b='Banana', m='Manzana')
    persona1.mostrar_detalles()

    persona1.nombre = 'Juan'
    persona1.apellido = 'Rodriguez'
    persona1.edad = 35
    persona1.mostrar_detalles()

    print(__name__)  # Con esto podemos saber desde donde se ejecutan las cosas
