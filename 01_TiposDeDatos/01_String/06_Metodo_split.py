"""
Metodo "split"
Regresa una lista de plabras encontradas en un string y se utiliza un delimitador. Es la inversa del metodo "join"
"""

help(str.split)

cursos = 'Java Python JavaScript Angular Spring'
lista_cursos = cursos.split()
print(f'Lista Cursos: {lista_cursos}')
print(type(lista_cursos))

cursos_separados_coma = 'Java,Python,JavaScript,Angular,Spring'
lista_cursos = cursos_separados_coma.split(',')  # Se especifica el separador, ya que si no no lo detecta por la coma
print(f'Lista Cursos: {lista_cursos}')
print(len(lista_cursos))

# Para indicar el número maximo en el que se separa la cadena, se le otorga un número, ese sirve para delimitar la
# cantidad maxima de elementos que tendra esa lista
lista_cursos = cursos_separados_coma.split(',', 10)
print(f'Lista Cursos: {lista_cursos}')
print(len(lista_cursos))