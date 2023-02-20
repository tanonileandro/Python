print('Bienvenidos')
print('A continuacion escriba Mes y Dia para saber a que estacion del año correspode\n')

estacion = None  # None: se utiliza para indicar que todavia esta variable no tiene ningun valor

mes = int(input('Ingrese un mes (1-12): '))

while 0 > mes or mes > 12:
    print(f'El mes ingresado {mes} no existe...\n')
    mes = int(input('Ingrese nuevamente un mes: '))

dia = int(input('Ingrese un dia del mes: '))

if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
    while 0 > dia or dia > 31:
        print(f'El mes ingresado {mes} tiene 31 dias...\n')
        dia = int(input('Ingrese nuevamente un dia del mes: '))

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
    while 0 > dia or dia > 31:
        print(f'El mes ingresado {mes} tiene 30 dias...\n')
        dia = int(input('Ingrese nuevamente un dia del mes: '))

if mes == 2:
    while 0 > dia or dia > 28:
        print(f'El mes ingresado {mes} tiene 28 dias...')
        dia = int(input('Ingrese nuevamente un dia del mes: '))

if 1 <= mes <= 3:
    if mes == 3:
        if 1 <= dia <= 20:
            estacion = 'Verano'
            print(f'\nEl Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
        else:
            estacion = 'Otoño'
            print(f'\nEl Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
    else:
        estacion = 'Verano'
        print(f'\nEl Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
elif 3 < mes <= 6:
    if mes == 6:
        if 1 <= dia <= 20:
            estacion = 'Otoño'
            print(f'\nEl Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
        else:
            estacion = 'Invierno'
            print(f'\nEl Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
    else:
        estacion = 'Otoño'
        print(f'\nEl Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
elif 6 < mes <= 9:
    if mes == 9:
        if 1 <= dia <= 20:
            estacion = 'Invierno'
            print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
        else:
            estacion = 'Primavera'
            print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
    else:
        estacion = 'Invierno'
        print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
elif 9 < mes <= 12:
    if mes == 12:
        if 1 <= dia <= 20:
            estacion = 'Primavera'
            print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
        else:
            estacion = 'Verano'
            print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
    else:
        estacion = 'Primavera'
        print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
else:
    print('Valores ingresados no validos...')