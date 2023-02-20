"""
Se pueden crear excepciones personalizadas, este es un ejemplo, se crea una en la cual se activara cuando se
introdusca en el programa dos numeros identicos, aunque se podria crear con cualquier otro proposito...
"""


class NumerosIdenticosException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje
