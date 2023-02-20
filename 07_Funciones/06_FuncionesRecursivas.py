"""
Ejemplo para el calculo de un factorial

5! = 5 * 4 * 3 * 2 * 1
5! = 5 * 4 * 3 * 2
5! = 5 * 4 * 6
5! = 5 * 24
5! = 120
"""


def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)


resultado = factorial(int(input('Por favor ingrese un numero y a continuacion calcularemos su factorial: ')))
print(f'El factorial del numero ingresado es: {resultado}')
