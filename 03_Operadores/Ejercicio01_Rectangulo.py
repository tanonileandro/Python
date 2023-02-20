"""
Instrucciones de la tarea:

-Se solicita calcular el area y el perimetro de un Rectangulo, para el ejemplp deberemos crear las sig. variables:
alto (int)
ancho (int)

-El resultado debe proporcionar los valores de largo y ancho, despues se debe imprimir el resultado del area y el
perimetro

"""

print('Bienvenidos')
print('Aquí podrá calcular el Area y Perímetro de un rectángulo \n')

alto = int(input('Ingrese el alto: '))
ancho = int(input('Ingrese el ancho: '))

area = alto * ancho
perimetro = (alto + ancho) * 2

print(f'Area: {area}')
print(f'Perímetro: {perimetro}')
