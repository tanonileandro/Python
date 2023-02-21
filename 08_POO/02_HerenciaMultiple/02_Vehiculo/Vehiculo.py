"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""


class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return 'Color: ' + self.color + ', Cantidad de Ruedas: ' + str(self.ruedas)


class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + ', Velocidad (Km/h): ' + str(self.velocidad)


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ', Tipo de Bicicleta: ' + self.tipo


if __name__ == '__main__':
    print(__name__)

    # PRESTAR ATENCION A COMO ESTA PUESTO EL ORDEN DE LOS PARAMETROS PARAMETROS AL MOMENTO DE IMPRIMIR EN PANTALLA !!!

    # Prueba: se crea un objeto Vehiculo
    vehiculo = Vehiculo('Rojo', 4)
    print(vehiculo)

    # Prueba: se crea un objeto clase hija Coche
    coche = Coche('Rojo', 4, 240)
    print(coche)

    # Prueba: se crea un objeto clase hija Bicicleta
    bicicleta1 = Bicicleta('Negra', 2, 'Carrera')
    print(bicicleta1)
