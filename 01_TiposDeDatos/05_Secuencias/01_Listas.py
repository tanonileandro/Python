# lista de nombres
nombres = ['Juan', 'Carlos', 'Leandro', 'Pedro']

# imprimir lista de nombres
print(nombres)

# acceder a los elementos de la lista
print(nombres[0])
print(nombres[3])

# acceder a los elementos de manera inversa
print(nombres[-1])  # igual que print(nombres[3])
print(nombres[-4])

# imprimir un rango
print(nombres[0:2])  # no incluye el indice 2, imprime 0 y 1

# imprimir del inicio de la lista a otro indice (Sin incluirlo)
print(nombres[:3])  # es igual a print(nombres[0:3])

# recorrer lista desde el indice indicado al final
print(nombres[2:])  # es igual a print(nombres[2:3])

# Cambiar un valor
nombres[2] = 'Pepe'
print(nombres)

# Iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista\n')

# Preguntar el largo de una lista
print(len(nombres))  # saber la cantidad de elementos que contiene
print(nombres)

# Agregar un nuevo elemento a la lista sin una posicion especifica
nombres.append('Ricardo')
print(nombres)

# Insertar un elemento en una posicion especifico
nombres.insert(1, 'Octavio')
print(nombres)

# Remover un elemento de la lista
nombres.remove('Octavio')
print(nombres)

# Remover el ultimo elemento agregado de la lista
nombres.pop()
print(nombres)\

# Removever un elemento en una posicion indicada
del nombres[0]
print(nombres)

# Eliminar elementos de la lista y dejarla vacia
nombres.clear()
print(nombres)

# Borrar por completo la lista
del nombres  # Si se manda a imprimir la lista despues de esto saldra un error porque ya fue eliminada por completo