edad = int(input('Ingrese su edad: '))
etapa = None

if 0 <= edad < 10:
    etapa = 'La infancia es increible...'
    print(f'Tu edad es {edad}: {etapa}')
elif 10 <= edad < 20:
    etapa = 'Muchos cambios y mucho estudio...'
    print(f'Tu edad es {edad}: {etapa}')
elif 20 <= edad < 30:
    etapa = 'Amor y comienza el trabajo...'
    print(f'Tu edad es {edad}: {etapa}')
else:
    print('Etapa de vida no reconocida...')