print('\n\"Bienbenido a nuestro sistema de calificaciones\"\n')

calificacion = None
nota = float(input('Ingrese una nota entre 0-10: '))

while nota < 0 or nota > 10:
    print('Valor ingresado incorrecto...\n')
    nota = float(input('Ingrese nuevamente una nota entre 0-10: '))

if 0 <= nota < 4:
    calificacion = 'F'
    print(f'\nNota ingresada ({nota}) Su calificacion es: {calificacion}')
elif 4 <= nota < 6:
    calificacion = 'D'
    print(f'\nNota ingresada ({nota}) Su calificacion es: {calificacion}')
elif 6 <= nota < 8:
    calificacion = 'C'
    print(f'\nNota ingresada ({nota}) Su calificacion es: {calificacion}')
elif 8 <= nota < 9:
    calificacion = 'B'
    print(f'\nNota ingresada ({nota}) Su calificacion es: {calificacion}')
elif 9 <= nota <= 10:
    calificacion = 'A'
    print(f'\nNota ingresada ({nota}) Su calificacion es: {calificacion}')