# Creacion de objetos

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Crear metodos de instancia
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


persona1 = Persona('Leandro', 'Tanoni', 27)
persona2 = Persona('Cristian', 'Tanoni', 30)
# print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}') - se elimina esta forma de
# imprimir y se llama a imprimir el metodo

persona1.mostrar_detalle()
persona2.mostrar_detalle()

# Otra manera de imprimir no tan comun:
Persona.mostrar_detalle(persona2)

# Se puede agregar un nuevo atributo en cualquier momento, aunque de esta forma no se comparte entre todos los objetos
persona1.telefono = 3329330838
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad} {persona1.telefono}')
