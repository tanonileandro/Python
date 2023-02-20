"""
Crea una funcion para multiplicar los valores recibidos de tipo numerico, utilizando argumentos variables *args como
parametro de la funcion y regresar como resultado la multiplicacion de todos los valores pasados como argumentos..
"""


def multiplicar_valores(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado


print(multiplicar_valores(5, 5, 5, 3, 4))
