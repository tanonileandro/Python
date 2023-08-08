from random import *

# Imprime un numero aleatorio en el rango que le indiques cada vez que se ejecute
aleatorio = randint(1, 50)
print(aleatorio)

# Imprime un numero aleatorio en el rango que le indiques pero con decimal
# Con round lo redondeo a la cantidad de decimales que quiero
aleatorio = round(uniform(1, 10), 2)
print(aleatorio)

# Elige un numero aleatorio entre 0 y 1 solamente, no se le pasa parametros
aleatorio = random()
print(aleatorio)

# Permite trabajar con una seleccion aleatoria dentro de una lista o cualquier otro coleccionable
colores = ['azul', 'rojo', 'violeta', 'blanco', 'negro']
aleatorio = choice(colores)
print(aleatorio)

# Mezcla la lista en un orden aleatorio, generan una modificacion in situ, no se puede utilizar con string c
numeros = list(range(5, 50, 5))

shuffle(numeros)

print(numeros)