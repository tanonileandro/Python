# Es similar a una lista, conserva un orden, pero no se puede eliminar ni agregar elementos como en una lista

# Definicion de Tupla
frutas = ('Naranja', 'Frutilla', 'Banana', 'Manzana')
print(frutas)

# Para formar una tupla de un solo elemento se debe escribir con una coma al final del mismo porque sino se toma como
# una cadena, ejemplo - frutas = ('Naranja',)

# Saber el largo
print(len(frutas))

# Acceder a un elemento
print(frutas[0])
print(frutas[-1])  # para acceder de forma inversa

# Acceder a un rango de valores
print(frutas[1:3])  # No incluye el ultimo valor
print('\n')

# Recorrer elemenos
for fruta in frutas:
    print(fruta)

for fruta in frutas:
    print(fruta, end=' ')
    # Es igual a lo anterior pero el 'end' permite que no haga salto de linea despues de cada elemento, en una
    #  misma fila

print('\n')

# Cambiar un valor de la tupla
# Como la tupla no se puede modificar, se debe hacer lo siguiente
frutasLista = list(frutas)  # Se transforma la tupla en lista
frutasLista[0] = 'Pera'  # Se asigna el nuevo valor en la posicion deseada
frutas = tuple(frutasLista)  # Se vuelve a convertir en tupla una vez modificada
print(frutas)

# Eliminar la tupla por completo
del frutas
