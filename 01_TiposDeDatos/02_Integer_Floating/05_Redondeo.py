resultado = round(90/7)
print(resultado)

valor = 95.564444456
resultado = round(valor, 3)
print(resultado)

# Redondeo por fuera del print modifica la variable y si se redondea y queda entero pasa a ser un int
resultado = round(valor)
print(resultado)
print(type(resultado))

# Redondeo por dentro del print queda el valor como float aunque no tenga decimales porque no se modifica la variable
# sino la impresion del mismo.
print(round(valor))
print(type(valor))
print(valor)

valor = round(10/3, 2)
print(valor)

valor = 10.676767
print(round(valor))

valor = 5**0.5
print(f'La raiz cuadrada de {5} es igual a {round(valor, 4)}')