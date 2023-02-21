# Similar a la lista y tupla, pero no conserva un orden ni tiene un indice, se pueden agregar elementos pero no
# duplicados, no se pueden modificar los elementos, y se puede eliminar elementos

planetas = {'Marte', 'Tierra', 'Jupiter', 'Pluton'}
print(planetas)  # se imprime siempre con un orden aleatorio

# Cantidad de elementos
print(len(planetas))

# Revisar si un elemento esta dentro del set
print('Tierra' in planetas)

# Agregar un elemento al set
planetas.add('Venus')
print(planetas)

# No se pueden duplicar elementos
planetas.add('Venus')  # por lo tanto este elemento no se va a agregar
print(planetas)

# Eliminar elementos
planetas.remove('Venus')  # si el elemento a borrar se escribe mal nos va a saltar un error "keyError"
print(planetas)
planetas.discard('Pluton')  # sirve tambien para eliminar un elemento, pero no tira error en caso de equivocarnos
print(planetas)

# Limpair set
planetas.clear()
print(planetas)

# Eliminar set
del planetas
