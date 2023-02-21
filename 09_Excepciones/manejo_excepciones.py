"""
1) Para que un programa no finalice bruscamente por un error, se pueden agregar excepciones para que si ocurre algun
error el programa nos de un aviso de lo que paso y siga ejecutandose...

2) Se declara la variable "resultado" por fuera del bloque try-except porque despues se vuelve a utilizar, si se declara
por dentro del mismo seria una variable local y no se podria volver a utilizar por fuera del bloque...

3) La palabra reservada "raise" sirve para arrojar cualquier tipo de excepcion
"""
from NumerosIdenticosException import NumerosIdenticosException

print('Bienvenidos'.center(40, '-'))

while True:
    print('\nMENU')
    print('1. Realizar una division entre dos numeros')
    print('2. Salir del programa\n')

    resultado = None
    menu = input('Ingrese una opcion: ')

    if menu == '1':
        try:
            a = int(input('Ingrese el primer numero: '))
            b = int(input('Ingrese el segundo numero: '))

            if a == b:
                raise NumerosIdenticosException('Numeros Identicos')

            resultado = a / b

        except ZeroDivisionError as e:
            print(f'\nOcurrio un error | Se activo "ZeroDivisionError": {e}, {type(e)}')  # Clase hija
        except TypeError as e:
            print(f'\nOcurrio un error | Se activo "TypeError": {e}, {type(e)}')  # Clase hija
        except ValueError as e:
            print(f'\nOcurrio un error | Se activo "ValueError": {e}, {type(e)}')  # Clase hija
        except Exception as e:
            print(f'\nOcurrio un error | Se activo "Exception": {e}, {type(e)}')  # Clase generica
        else:  # Este bloque es opcional, y se va a ejecutar cuando no se ejecute ninguna exception
            print('\nNo se ejecuto ningun error...')
        finally:  # Se ejecuta siempre al finalizar independientemente si hay error o no..
            print('Ejecucion del bloque \"finally\"')

        print(f'Resultado: {resultado}')
        print('Continuamos...\n')

    elif menu == '2':
        break
    else:
        print('Opcion ingresada inexistente...')
