print('\n\"Bienbenido a nuestro sistema de calificaciones\"\n')

nota = float(input('Ingrese una nota entre 0-10: '))
calificacion = None

if 0 <= nota < 4:
    calificacion = 'F'
    print(f'Nota ingresada ({nota}) Su calificacion es: {calificacion}')
elif 4 <= nota < 6:
    calificacion = 'D'
    print(f'Nota ingresada ({nota}) Su calificacion es: {calificacion}')
elif 6 <= nota < 8:
    calificacion = 'C'
    print(f'Nota ingresada ({nota}) Su calificacion es: {calificacion}')
elif 8 <= nota < 9:
    calificacion = 'B'
    print(f'Nota ingresada ({nota}) Su calificacion es: {calificacion}')
elif 9 <= nota <= 10:
    calificacion = 'A'
    print(f'Nota ingresada ({nota}) Su calificacion es: {calificacion}')
else:
    print('Valor ingresado incorrecto...')
