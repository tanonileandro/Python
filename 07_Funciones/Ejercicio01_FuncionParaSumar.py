"""
Crear una funcion para sumar los valores recibidos de tipo numerico, utilizando argumentos variables *arg como
parametro de la funcion y regresar como resultado la suma de todos los valores pasados como argumentos
"""


# Definimos la funcion para sumar valores
def sumar_valores(*args):
    resultado = 0
    for valor in args:  # Iteramos cada elemento
        resultado += valor  # es lo mismo que "resultado = resultado + valor"
    return resultado


# Llamamos a la funcion
print(sumar_valores(5, 5, 3, 5))
print(sumar_valores(6, 3, 5, 6))
