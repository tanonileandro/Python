"""
Metodo 'join'
Recibe dos parametros, la cadena en si misma y un iterablie (lista, tupla, diccionario, etc) -> join(self, iterable, /)
Puede concatenar cualquier numero de string

Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
"""

help(str.join)

tupla_str = ('Hola', 'Mundo', 'Universidad', 'Python')
cadena_str = ' '.join(tupla_str)
print(f'Mensaje: {cadena_str} \n')

lista_cursos = ['Java', 'Python', 'Angular', 'Spring']
cadena_cursos = ', '.join(lista_cursos)
print(f'Lista de Cursos: {cadena_cursos} \n')

cadena = 'HolaMundo'
mensaje = '.'.join(cadena)
print(f'Mensaje: {mensaje} \n')

diccionario = {'Nombre': 'Juan', 'Apellido': 'Perez', 'Edad': '20'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'Llaves: {llaves}, type: {type(llaves)}')
print(f'Valores: {valores}, type: {type(valores)}')
