# Ejercicio Cubo

class Cubo:
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo

    def volumen(self):
        return self.ancho * self.alto * self.profundo


print('Bienvenidos')
print('A continuacion proporcione los datos para calcular el volumen de un CUBO\n')
ancho = int(input('Ingrese el ancho: '))
alto = int(input('Ingrese el alto: '))
profundo = int(input('Ingrese la profundidad: '))

cubo1 = Cubo(ancho, alto, profundo)
print(f'El Volumen del Cubo es: {cubo1.volumen()}')
