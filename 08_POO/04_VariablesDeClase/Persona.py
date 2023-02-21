class Persona:
    contador_persona = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona[{self.id_persona} {self.nombre} {self.edad}]'


persona1 = Persona('Leandro', 28)
persona2 = Persona('Carlos', 33)
persona3 = Persona('Joaquin', 48)
persona4 = Persona('Claudia', 24)
print(persona1)
print(persona2)
print(persona3)
print(persona4)
print(f'Cantidad de personas registradas: {Persona.contador_persona}')
