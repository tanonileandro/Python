"""
Formato a un str con parametros posicionales
"""

# Dar formato con "parametros posicionales"
# Variables
nombre = 'Juan'
edad = 28
menaje_con_formato = '\nMi nombre es %s y tengo %d' % (nombre, edad)
print(menaje_con_formato)

# Tupla
persona = ('Carla', 'Gomez', 5000.00)
mensaje_con_formato = 'Hola %s %s, tu sueldo sera de %.2f' % persona
print(mensaje_con_formato)

mensaje_con_formato = 'Hola %s %s, tu sueldo sera de %.2f'
print(mensaje_con_formato % persona)

# Dar formato con "format"
nombre = 'Juan'
edad = 28
sueldo = 3000
mensaje_con_formato = 'Nombre: {} - Edad: {} - Sueldo: {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

# Especificar valores con índice
# Cadena con indicadores de posicion en las llaves format para poder cambiar el orden
mensaje_con_formato = 'Nombre {0} - Edad {1} - Sueldo{2:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje_con_formato = 'Edad {1} - Nombre {0} - Sueldo{2:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

# Especificar valores con argumentos
mensaje = 'Nombre {n}, Edad {e}, Sueldo {s:.2f}'.format(e=edad, n=nombre, s=sueldo)
print(mensaje)

# Especificar valores con diccionario
diccionario = {'nombre': 'Leandro', 'edad': 27, 'sueldo': 8000.00}
mensaje = 'Nombre: {persona[nombre]} Edad: {persona[edad]} Sueldo: {persona[sueldo]:.2f}'.format(persona=diccionario)
print(mensaje)

# Dar formato "template literal"
mensaje_con_formato = f'Nombre: {nombre} - Edad: {edad} - Sueldo: {sueldo:.2f}'
print(mensaje_con_formato)

# Metodo "print"
print(nombre, edad, sueldo, sep=', ')