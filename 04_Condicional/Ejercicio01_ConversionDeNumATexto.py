numero = int(input('Proporcione un valor entre 1 y 3: '))
numeroTexto = ''

if numero == 1:
    numeroTexto = 'Numero uno'
elif numero == 2:
    numeroTexto = 'Numero dos'
elif numero == 3:
    numeroTexto = 'Numero tres'
else:
    numeroTexto = 'Valor fuera de rango'

print(f'Numero proporcionado: {numero} - {numeroTexto}')

