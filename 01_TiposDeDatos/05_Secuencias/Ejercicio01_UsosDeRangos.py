# Ejercicio 1: Iterar un rango de 0 a 10 e imprimir numeros divicibles por 3.

print('Rango de 0 a 10 con numeros divisibles entre 3')

for i in range(11):
    if i % 3 == 0:
        print(i)
else:
    print('Fin de la iteracion..\n')

# Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimirlos.

print('Rango con valores de inicio = 2 y fin = 6')

for i in range(2, 7):  # El primer numero indica el inicio, segundo el final
    print(i)
else:
    print('Fin de la iteracion...\n')

# Ejercico 3: Crear un rango de 3 a 10 pero con incremento de 2 en 2, en lugar de 1 en 1

print('Rango con valores de inicio = 3, fin = 10, incremento = 2')

for i in range(3, 11, 2):  # El primer numero indica el inicio, segundo el final, tercero el incremento.
    print(i)
else:
    print('Fin de la iteracion...\n')
