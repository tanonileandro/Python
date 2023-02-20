edad = int(input('Introdusca su edad: '))

# Forma no correcta y mas larga:
# veinte = edad >= 20 and edad < 30
# treinta = edad >= 30 and edad < 40
# print(veinte)
# print(treinta)

# Forma corrrecta de pregunrar el rango:
if (20 <= edad < 30) or (30 <= edad < 40):
    if 20 <= edad < 30:
        print(f'Usted tiene {edad} años, esta dentro del rango de los 20\'s')
    else:
        print(f'Usted tiene {edad} años, esta dentro del rango de los 30\'s')
else:
    print(f'Usted tiene {edad} años, no esta dentro del rango de los 20`s ni 30\'s')