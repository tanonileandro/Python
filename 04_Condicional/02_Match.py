# Anteriormente con if

serie = "N-02"

if serie == "N-01":
    print('Samsung')
elif serie == "N-02":
    print('Nokia')
elif serie == "N-03":
    print('Motorola')
elif serie == "N-04":
    print('Xiaomi')
else:
    print('No existe el producto')

# Con la actualizacion de python, se implementa match, seria como un switch de otros lenguajes

serie = "N-06"

match serie:
    case "N-01":
        print('Samsung')
    case "N-02":
        print('Nokia')
    case "N-03":
        print('Motorola')
    case "N-04":
        print('Xiaomi')
    case _:  # valor por defecto
        print('No existe el producto')

# -------------------------------------------------------------------------------------------
print('\n')

# Ejemplo mas complejo

cliente = {'nombre': 'Federico',
           'edad': 35,
           'ocupacion': 'Programador'}

pelicula = {'titulo': 'Rocky',
            'fiche_tecnica': {'protagonista': 'Silvester Stallone',
                              'director': 'Silvester Stallone'}}

elementos = [cliente, pelicula, 'libro']

for elemento in elementos:
    match elemento:
        case {'nombre': nombre,
              'edad': edad,
              'ocupacion': ocupacion}:
            print('Es un cliente')
            print(nombre, edad, ocupacion, '\n')

        case {'titulo': titulo,
              'fiche_tecnica': {'protagonista': protagonista,
                                'director': director}}:

            print('Esto es una pelicula')
            print(titulo, protagonista, director, '\n')

        case _:
            print('No se que es...')