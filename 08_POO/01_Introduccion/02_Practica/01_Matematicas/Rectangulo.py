# Ejercicio rectangulo

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


base = int(input('Ingrese la base: '))
altura = int(input('Ingrese la altura: '))

rectangulo1 = Rectangulo(base, altura)
print(f'El Area del Rectangulo es: {rectangulo1.area()}')
