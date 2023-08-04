# * desempaquetar
numeros = [1, 2, 3]
print(numeros)
print(*numeros)
print(*numeros, sep=' - ')

# -----------------------------------------------------------------------------------------
print('\n')


# Desempaquetando al momento de pasar un parámetro a una función
def sumar(a, b, c):
    print(f'Resultado suma: {a + b + c}')


sumar(*numeros)  # antes de pasar la lista como argumentos para la funcion y que realice el calculo,  hay que
# desempaquetarla porque sino tirara error
