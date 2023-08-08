# Compresion de listas

# forma larga
palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

# forma corta
lista = [letra for letra in 'python']
print(lista)

lista = [n for n in range(0, 21, 2)]
print(lista)


# forma corta con condiciones y calculos
lista = [n / 2 for n in range(0, 21, 2)]  # modificar antes de que se itere la variable
print(lista)

lista = [n for n in range(0, 21, 2) if n * 2 > 10]
print(lista)

# Para agregar un else al if y que funcione, se le aplica despues de la primer variable
lista = [n if n * 2 > 10 else 'no' for n in range(0, 21, 2)]
print(lista)

# -------------------------------------------------------------------------------------

# Ejemplo practico

medidas_en_pies = [10, 20, 30, 40, 50, 60]

medidas_en_metros = [pies * 3.281 for pies in medidas_en_pies]
print(medidas_en_metros)

# -------------------------------------------------------------------------------------

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [n ** 2 for n in valores]
print(valores_cuadrado)

# -------------------------------------------------------------------------------------

valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [n for n in valores if n % 2 == 0]
print(valores_pares)

# -------------------------------------------------------------------------------------

temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(grados_fahrenheit-32)*(5/9) for grados_fahrenheit in temperatura_fahrenheit]
print(grados_celsius)

