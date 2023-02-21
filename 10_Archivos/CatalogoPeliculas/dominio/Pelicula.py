class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Peliculas: {self._nombre}'


if __name__ == '__main__':
    pelicula = Pelicula('Rocky I')
    print(pelicula)
