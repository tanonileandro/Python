letra = None

for letra in 'Holanda':
    if letra == 'a':
        print(f'Letras a encontrada: {letra}\n')
        break # Sirve para romper el ciclo al encontrar la primera letra 'a'
else:
    print('Fin ciclo for...')

# ----------------------------------------------------------------------

for i in range(10):
    if i % 2 == 0:
        print(f'Valor: {i}')

print("\n")

# igual que el caso anterior se buscan los numeros pares, aplicado de distinta manera con la palabra continue
i = None
for i in range(10):
    if i % 2 != 0:
        continue # se ejecuta solo cuando la el if es verdadero, de lo contrario no se ejecuta y salta directo al print
    print(f'Valor: {i}')