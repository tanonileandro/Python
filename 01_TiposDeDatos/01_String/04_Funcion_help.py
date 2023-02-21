import math
from Docstring import MiClase


# Funcion help: Sirve para obtener informacion de un modulo, o un metodo en partucular.
# help()

# Uso de funcion Help en str: nos brinda toda la informacion de la clase str
help(str)
help(str.capitalize)  # Para tener la ayuda de un metodo especifico de str, lo mandamos a llamar.

# Información de la clase math
help(math)
help(math.isnan)
# ----------------------------------------------------------------------------------

# Funcion help para una clase

help(MiClase)
# Sirve para acceder a la documentacion que se fue agregando a nuestra clase, sirve para funciones, constantes, etc.

print(MiClase.__doc__)
# Este metodo manda a llamar solamente al docstring de la clase, no de toda la documentacion (metodos, atributos, etc)

print(MiClase.__init__.__doc__)
# Para acceder a la documentacion del metodo init

print(MiClase.mi_metodo.__doc__)
# Para acceder a la documentacion de nuestro metodo

print(MiClase.mi_metodo)
print(type(MiClase.mi_metodo))
# Nos muestra que nuestro metodo es una funcion, pero tambien es un Objeto