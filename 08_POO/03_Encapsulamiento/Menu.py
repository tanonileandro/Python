"""
Para saber en el orden en que se ejecutan las cosas, se puede ejecutar el metodo MRO - Method Resolution Order
Ej: "print(Cuadrado.mro())"
"""
# ----------------------------------------------------------------------------------
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo

# Menu:
while True:
    print('-' * 50)
    print('Bienvenidos a Creacion de Objetos'.center(50, ' '))
    print('-' * 50)
    print('1. Creacion de un Cuadrado')
    print('2. Creacion de un Rectangulo')
    print('3. Exit\n')

    menu = input('Ingrese una Opcion: ')
    if menu == '1':
        print('\n')
        print(' Creacion Objeto Cuadrado '.center(50, '-'))
        lado = int(input('Ingrese el valor de los lados: '))
        color = input('Ingrese el color: ')

        cuadrado1 = Cuadrado(lado, color)
        print(cuadrado1)
        print(Cuadrado.mro())
        print('\n')
    elif menu == '2':
        print('\n')
        print(' Creacion Objeto Rectangulo '.center(50, '-'))
        ancho = int(input('Ingrese el ancho: '))
        alto = int(input('Ingrese el alto: '))
        color = input('Ingrese el color: ')

        rectangulo1 = Rectangulo(ancho, alto, color)
        print(rectangulo1)
        print(Rectangulo.mro())
        print('\n')
    elif menu == '3':
        break
    else:
        print('Opcion incorrecta...\n')

# ----------------------------------------------------------------------------------
# Forma de Acceder a los datos y cambiarlos individualmente:
print('-' * 50)
print('Ejecucion prueba de los datos por fuera del Menu'.center(50, ' '))
print('-' * 50)

cuadrado2 = Cuadrado(5, 'Rojo')
cuadrado2.ancho = -15
print(f'Calculo del Area de la Figura: {cuadrado2.calculo_area()}')
print(cuadrado2)
# Al tener validacion la encapsulacion setter, el valor -15 no se le puede asignar, automaticamente toma el valor
# asignado anteriormente..

rectangulo2 = Rectangulo(5, 6, 'Verde')
rectangulo2.ancho = 0
print(f'Calculo del Area de la Figura: {cuadrado2.calculo_area()}')
print(rectangulo2)
# ----------------------------------------------------------------------------------

# cuadrado1 = Cuadrado(5, 'Rojo')
# print(f'Ancho de la Figura: {cuadrado1._ancho}')
# print(f'Alto de la Figura: {cuadrado1._alto}')
# print(f'Color de la Figura: {cuadrado1._color}')
# print(f'Calculo del Area de la Figura: {cuadrado1.area_cuadrado()}')
