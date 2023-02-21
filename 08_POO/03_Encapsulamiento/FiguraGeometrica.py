"""
Para convertir la clase a abstracta se importa el ABC = Abstract Base Class
"""
from abc import ABC, abstractmethod


class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        while (0 >= ancho or ancho > 10) or (0 >= alto or alto > 10):
            if 0 >= ancho or ancho > 10:
                print('Ancho ingresado invalido...')
                ancho = int(input('Ingrese nuevamente el ancho: '))
                self._ancho = ancho
            elif 0 >= alto or alto > 10:
                print('Alto ingresado invalido...')
                alto = int(input('Ingrese nuevamente el alto: '))
                self._alto = alto
        else:
            self._ancho = ancho
            self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            print(f'Valor erroneo de Ancho: {ancho}')

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valor(alto):
            self._alto = alto
        else:
            print(f'Valor erroneo de Alto: {alto}')

    @abstractmethod
    def calculo_area(self):
        pass

    def __str__(self):
        return f'Figura Geometrica[ancho: {self._ancho}, alto: {self._alto}]'

    def _validar_valor(self, valor):
        return True if 0 < valor <= 10 else False