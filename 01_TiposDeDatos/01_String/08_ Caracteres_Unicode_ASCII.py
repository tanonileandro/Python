# Caracteres unicode
print('Hola\u0020Mundo')
print('Notación simple:', '\u0041')
print('Notación extendida:', '\U00000041')
print('Notación hexadecimal', '\x41')
print('Corazón:', '\u2665')
print('Cara sonriendo:', '\U0001f600')
print('Serpiente:', '\U0001F40D')

# Caracteres ASCII
caracter = chr(65)
print('A mayúscula:', caracter)

caracter = chr(64)
print('Símbolo @:', caracter)

caracter = chr(97)
print('a minúscula:', caracter)

# Ejemplo imprimir una palabra con tilde

# Unicode
print(f'Hola me llamo Leandro Mart\u00EDn Tanoni')
# ASCII
caracter = chr(237)
print(f'Hola me llamo Leandro Mart{caracter}n Tanoni')
