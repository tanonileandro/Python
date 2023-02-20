"""
Imprimir numeros de manera descendentes usando funciones recursivas.
Puede ser caulquier valor positivo, ejemplo, si el valor es 5 debera imprimir:
5
4
3
2
1
"""


def num_descendientes(numero):
    numMin = 1
    while 0 > numero:
        print('Valor ingresado incorrecto, ingrese numeros positivos..\n')
        num_descendientes(int(input('Ingrese nuevamente un valor: ')))
    else:
        if numero >= numMin:
            print(numero)
            num_descendientes(numero - 1)


num_descendientes(int(input('Ingrese un valor: ')))
