# Cualquier calculo que involucre un float, se promueve a float
a = 1 + 10.54
print(a)
print(type(a))

num1 = 7.5
num2 = 2.5
print(type(num1 + num2))

# Profundización tipo float

# Cntidad de numeros después de la coma que deseemos
a = 3.0
print(f'a: {a:.2f}')

# Constructor float puede recibir int y str
a = float(10)
a = float('10')
print(f'a: {a:.2f}')

num2 = 10
num1 = float(num2)
print(type(num1))

num1 = "7.5"
num2 = "10"
num1 = float(num1)
num2 = int(num2)
print(num1 + num2)

# Notacion exponecial (valores positivos o negativos)
a = 3e-5
print(f'a: {a:.5f}')
a = 3e5
print(f'a: {a:.2f}')
# Los dos puntos dentro de las llaves son para dar formato, en este caso se indica la cantidad de num despues de la
# coma en el num flotante


