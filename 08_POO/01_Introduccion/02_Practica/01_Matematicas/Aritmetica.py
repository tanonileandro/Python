class Aritmetica:
    """
    Clase Aritmetica para realizar operaciones de suma, resta, etc.
    """

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def producto(self):
        return self.num1 * self.num2

    def cociente(self):
        return self.num1 / self.num2


aritmetica1 = Aritmetica(6, 5)
print(f'Suma: {aritmetica1.suma()}')
print(f'Resta: {aritmetica1.resta()}')
print(f'Producto: {aritmetica1.producto()}')
print(f'Cociente: {aritmetica1.cociente():.2f}')
