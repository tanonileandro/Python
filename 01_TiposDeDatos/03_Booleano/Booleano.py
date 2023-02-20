# Tipos de Datos

# Booleano con validacion if
variable = 2 > 1
print(variable)
print(type(variable))

if variable:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Tipos numericos, False para 0, True demas valores
valor = 0
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')
valor = 23
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Tipo str, False para '' (cadena vacia, sin espacio), True para demas valores.
valor = ''
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = ' '
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = 'a'
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Tipo colecciones, False para colecciones vacias, True para todas las demas colecciones.
#Lista
valor = []
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = [2, 3, 4]
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Tupla
valor = ()
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = (2, 3, 4)
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Diccionario
valor = {}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

valor = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
resultado = bool(valor)
print(f'Valor {valor}, resultado: {resultado}')

# Ejemplos if:
if bool(''):
    print('Regreso Verdadero')
else:
    print('Regreso Falso')

if 0:  # Con esto se pregunta el valor Booleano (verdadero/falso) es igual a: if bool(''):
    print('Regreso Verdadero')
else:
    print('Regreso Falso')

variable = 5
if variable:
    print('Regreso Verdadero')
else:
    print('Regreso Falso')

# Ejemplos while:
variable = 0
while variable:
    print('Ejecucion ciclo while')
    break
else:
    print('Fin ciclo while')