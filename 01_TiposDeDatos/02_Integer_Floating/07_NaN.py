import math
from decimal import Decimal
# NaN = Not a Number
# No es sensible a mayusculas/minusculas
# Es un tipo de dato numerico indefinido

a = float('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')

a = Decimal('NaN')
print(f'a: {a}')
print(f'Es NaN (not a number)?: {math.isnan(a)}')
