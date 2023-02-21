"""
1) Al abrir un archivo con "with" este lo abre y tambien lo cierra automáticamente si necesidad de que nosotros lo
cerremos al finalizar de utilizarlo
    Ejecuta 2 metodos: __enter__
                       __exit__

2) Esto se conoce como Context Manager o Administrador de Recursos
"""
from Archivos.Leccion01.ManejoArchivos import ManejoArchivos

# with open('prueba.txt', 'r', encoding='utf8') as archivo:
with ManejoArchivos('prueba.txt') as archivo:
     print(archivo.read())