# Dada la siguiente tupla
# Crear una lista que solo iuncluya los numeros menores a 5

tupla = (13, 1, 8, 3, 2, 5, 8)  # Tupla
print(tupla)

lista = []  # Creo una lista vacia para desspues poder agregarle elementos
for i in tupla:
    if i < 5:
        lista.append(i)  # Agrego los elementos menores a 5 de la tupla a la lista creada anteriormente
print(lista)
