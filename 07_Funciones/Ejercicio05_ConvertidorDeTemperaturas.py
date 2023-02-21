"""
Convertidor de temperatura
Realizar dos funciones para convertir de grados celcius a fahrenheit y viceversa..
"""

# °C = (°F - 32) x 5 ÷ 9
# °F = °C x 9 ÷ 5 + 32


def fahrenheit_celsius(grados):
    conversion_celsius = (grados - 32) * 5 / 9
    return conversion_celsius


def celsius_fahrenheit(grados):
    conversion_fahrenheit = grados * 9 / 5 + 32
    return conversion_fahrenheit


while True:
    print('*** Bienvenidos a nuestro convertidor de temperaturas ***')
    print('1. Convertir de grados Fahrenheit a Celsius')
    print('2. Convertir de grados Celsius a Fahrenheit')
    print('3. Exit\n')

    menu = input('Ingrese una opcion: ')
    if menu == '1':
        grados = float(input('Ingrese los °F a convertir: '))
        print(f'\n{grados} °F son: ', fahrenheit_celsius(grados), '°C\n')
    elif menu == '2':
        grados = float(input('Ingrese los °C a convertir: '))
        print(f'\n{grados} °C son: ', celsius_fahrenheit(grados), '°F\n')
    elif menu == '3':
        break
    else:
        print('Opcion incorrecta...\n')
