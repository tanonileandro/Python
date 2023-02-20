"""
Un Byte es un conjunto de 8 bits y constituye el minimo elemento de memoria direccionable en una computadora
"""

# Caracteres bytes

caracteres_en_bytes = b'Hola Mundo'
print(caracteres_en_bytes)

mensaje = b'Universidad Python'
print(mensaje[1])  # Nos brinda el valor ASCII de la letra en esa posicion con un valor en BYTE
print(chr(mensaje[1]))  # Podemos imprimir que caracter ASCII es

lista_caracteres = mensaje.split()  # Para generar una lista de literales de tipo BYTE
print(lista_caracteres)

# Convertir de str a Byte
string = 'Programacion con Python'
print('string original:', string)

