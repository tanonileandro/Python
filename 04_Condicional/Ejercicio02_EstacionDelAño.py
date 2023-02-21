print('Bienvenidos\n')
print('A continuacion Mes y Dia para saber a que estacion del año correspode')

mes = int(input('Ingrese un mes (1-12): '))
dia = int(input('Ingrese un dia del mes: '))
estacion = None # Para indicar que todavia esta variable no tiene ningun valor

if 1 <= mes <= 3:
    if mes == 3:
        if 1 <= dia <= 20:
            estacion = 'Verano'
            print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
        else:
            estacion = 'Otoño'
            print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
    else:
        estacion = 'Verano'
        print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
elif 3 < mes <= 6:
    if mes == 6:
        if 1 <= dia <= 20:
            estacion = 'Otoño'
            print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
        else:
            estacion = 'Invierno'
            print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
    else:
        estacion = 'Otoño'
        print(f'El Dia {dia} del Mes {mes} corresponde a la estacion: {estacion}')
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
    print('Valores ingresados no validos')

