from Producto import Producto


class Orden:
    contador_orden = 0

    def __init__(self, productos):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._productos = list(productos)

    @property
    def id_orden(self):
        return self._id_orden

    @id_orden.setter
    def id_orden(self, id_orden):
        self._id_orden = id_orden

    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, productos):
        self._productos = productos

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + ' | '

        return f'Orden: {self._id_orden} \nProducto: {productos_str}'


if __name__ == '__main__':
    # Producto
    producto1 = Producto('Gaseosa', 345)
    producto2 = Producto('Harina', 156)
    producto3 = Producto('Pantalon', 7890)
    # Lista de Productos
    productos1 = [producto1, producto2]
    productos2 = [producto3]
    # Ordenes
    orden1 = Orden(productos1)
    orden2 = Orden(productos2)
    print(orden1)
    print(orden2)
