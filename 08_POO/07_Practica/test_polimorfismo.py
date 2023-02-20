"""
Para que aplique el polimorfismo definimos un metodo que imprimira un de los metodos str de cada clase. Se crea
una variable, en este caso llamada objeto, el cual elejira el metodo str de cualquier clase creada.

Metodo "isintance": validacion para saber si, cierto objeto corresponde a una instancia/atributo de cierta clase...
    No es recomendable a veces porque realizar tantas validaciones no es lo correcto, se busca que los datos sean lo
    mas generico posible 
"""
from POO.Leccion07.Empleado import Empleado
from POO.Leccion07.Gerente import Gerente


def imprimir_detalles(objeto):
    # print(objeto)
    print(type(objeto))  # Para saber que clase esta usando en la ejecucion
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)


# Se crea una variable llamada empleado la cual apunta a un objeto de clase Empleado y ejecutara el metodo str
empleado = Empleado('Leandro', 230000)
imprimir_detalles(empleado)
gerente = Gerente('Martin', 245000, 'Desarrollador')
imprimir_detalles(gerente)
