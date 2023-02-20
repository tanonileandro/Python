"""
Importacion desde otros archivos:
    Para imprimir varios elementos de otro archivo se separa con una "," cada elemento,
    ej: from constantes import MI_CONSTANTE, Matematicas
    Para importar todos los elementos, Ej: from constantes import *
    Para modificar el nombre de una clase importada, ej: from constantes import Matematicas as Mate
"""

from constantes import MI_CONSTANTE
from constantes import Matematicas as Mate

print(MI_CONSTANTE)
print(Mate.PI)

# Esto no se debe hacer
# MI_CONSTANTE = 'Nuevo Valor'
# print(MI_CONSTANTE)  -> Como ven se puede modificar igual, pero ya sabemos que no debemos...