# Cadena de texto
# Ejemplos
print('''Linea 1
Linea 2
Linea 3\n''')

# Caracter \
print('A\tB\tC\nD\tE\tF\nG\tH\tI\n')

print('''Barra Normal: /
Barra Invertida: \\''')

resultado = 'Hola \' Mundo'
print(f'Resultado: {resultado}')

resultado = 'Se va a eliminar el punto.\b\b\b'  # Elimina el caracter que tenga a la izquierda, en este caso elimina 3
print(f'Resultado: {resultado}')

resultado = 'c:\\nuevo\\juan'
print(f'Resultado: {resultado}')

# raw string
# Los caracteres de diagonal inversa se prosesan como un caracter normal
resultado = r'Cadena con \n salto de línea'
print(f'Resultado: {resultado}')

resultado = R'c:\nuevo\juan'
print(f'Resultado: {resultado}')

# ----------------------------------------------------------------------------------
# Las string son inmutables

# La cadena original no se va a modificar por mas que se le aplique el metodo capitalize en el ejemplo
mensaje1 = 'hola mundo'
mensaje2 = mensaje1.capitalize()  # Hace mayuscula la primer letra del string
print(f'mensaje1: {mensaje1} ID: {hex(id(mensaje1))}')  # El mensaje1 no se modifica
print(f'mensaje2: {mensaje2} ID: {hex(id(mensaje2))}')
mensaje1 += ' Adios'
print(mensaje1)
# Se modifica el mensaje y tambien modifica su id, porque ocupa un objeto diferente
# Como las cadenas son inmutables se genera un nuevo objeto

# ----------------------------------------------------------------------------------
# Multiplicacion de cadenas
# str
resultado = 3*'Hola'
print(f'Resultado: {resultado}')

# Tuplas
resultado = 5*('Hola', 'Mundo')
print(f'Resultado: {resultado}')

# Listas
resultado = 10*[0]
print(f'Resultado: {resultado}, largo: {len(resultado)}')