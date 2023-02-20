nombre = input(f'Ingrese su nombre: ')
ventas = float(input(f'Ingrese cuanto genero con las ventas: '))

comision = round(ventas * 13 / 100, 2)
print(f'{nombre} su comision de este mes es de: ${comision}')
