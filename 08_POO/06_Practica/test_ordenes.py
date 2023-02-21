# Producto
from POO.Leccion05.Orden import Orden
from POO.Leccion05.Producto import Producto

producto1 = Producto('Gaseosa', 345.00)
producto2 = Producto('Harina', 156.50)
producto3 = Producto('Pantalon', 7890.00)
producto4 = Producto('Carne', 2300.99)
# Lista de Productos
productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
# Ordenes
orden1 = Orden(productos1)
orden2 = Orden(productos2)
# Agregar productos  a una Orden
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print(orden2)
# Calcular el total de una orden
print(f'\nTotal de la Orden 1: {orden1.calcular_total()}')
print(f'Total de la Orden 2: {orden2.calcular_total()}')