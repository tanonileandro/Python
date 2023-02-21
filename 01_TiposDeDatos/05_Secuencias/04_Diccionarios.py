# Diccionarios (key, value)

diccionario = {
    'IDE': 'Integrated Development Environment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
print(diccionario)

# Candidad de elementos
print(len(diccionario))

# Acceder a un elemento (key)
print(diccionario['IDE'])
# Otra forma de acceder a un elemento
print(diccionario.get('OOP'))

# Modificar elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario, '\n')

# Recorrer los elementos de un diccionario
for termino in diccionario:
    print(termino)
# Para poder recorrer a los elementos con su valor
for termino, valor in diccionario.items():
    print(termino, valor)
# Otra forma
for termino in diccionario.keys():
    print(termino)
for valor in diccionario.values():
    print(valor)
print('\n')

# Comprobar existencia de un elemento
print('IDE' in diccionario)

# Agregrar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Remover un elemento
diccionario.pop('PK')
print(diccionario)

# Limpiar diccionario
diccionario.clear()
print(diccionario)

# Borrar por completo el diccionario
del diccionario
