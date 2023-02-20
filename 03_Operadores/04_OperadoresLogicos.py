"""
Operadores Logicos entre dos o mas valores.

and = todos los valores deben ser verdaderos para que el resultado sea verdadero
or = uno de los dos debe ser verdadero para que el resultado sea verdadero
not a = cambia el resultado, si la variable es verdadera, la cambia a falso, y viceversa

"""

# Operador AND

num = int(input('Ingrese un número: '))
numMinimo = 0
numMaximo = 10

dentroRango = (num >= numMinimo) and (num <= numMaximo)

if dentroRango:
    print(f'El número {num} está dentro del rango ')
else:
    print(f'El número {num} está fuera de rango')

# Operador OR

print('\nConsulta por vacaiones o dias libres')

vacacicones = True
diasDescanso = False

if vacacicones or diasDescanso:
    print('Puede relajarse unos días')
else:
    print('Tiene trabajo que hacer')

# Operador NOT

print('\nConsulta por vacaiones o dias libres')

vacacicones = False
diasDescanso = False

if not (vacacicones or diasDescanso): # Se intercambian las variables con el not
    print('Tiene trabajo que hacer')
else:
    print('Puede relajarse unos días')
