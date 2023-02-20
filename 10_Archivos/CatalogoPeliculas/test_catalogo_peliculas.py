from Archivos.catalogo_peliculas.dominio.Pelicula import Pelicula
from Archivos.catalogo_peliculas.servicio.CatalogoPeliculas import CatalogoPeliculas

print('Bienvenidos'.center(50, '-'))

menu = None
while menu != 4:
    try:
        print('MENU')
        print('1. Agregar película')
        print('2. Listado de películas')
        print('3. Eliminar película')
        print('4. Salir\n')
        menu = int(input('Ingrese una opción: '))

        if menu == 1:
            nombre_pelicula = input('Ingrese el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
            print('\n')

        elif menu == 2:
            CatalogoPeliculas.lista_peliculas()

        elif menu == 3:
            CatalogoPeliculas.eliminar_pelicula()

    except Exception as e:
        print(f'Ocurrió un Error: {e}')
        print('Ingrese un valor entre (1-4)\n')
else:
    print('Salimos del programa...')
