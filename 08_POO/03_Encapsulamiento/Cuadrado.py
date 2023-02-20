from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #  super().__init__() -*-
        while 0 >= lado or lado > 10:
            print('Lado ingresado invalido...')
            lado = int(input('Ingrese nuevamente el valor de los lados: '))
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calculo_area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} - {Color.__str__(self)} - Area[area: {self.calculo_area()}]'

# ----------------------------------------------------------------------------------
# (*) Para ejecutar las clases padres como es herencia multiple, este codigo no es recomendable porque tenemos dos
# clases
# padres y es mas complicado distingir cual nos trae en primer lugar...
# -Para que sea mas simple se declara cada clase por separado...
# -Se decalran los parametros "lado" porque al ser cuadrado no hace falta poner ancho y alto, van a ser iguales...
# ----------------------------------------------------------------------------------
