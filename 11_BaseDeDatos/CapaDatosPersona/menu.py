from persona_dao import PersonaDAO
from persona import Persona
from logger_base import log


while True:
    print('-' * 50)
    print('Bienvenidos a la base de datos'.center(50, ' '))
    print('-' * 50)
    print('1. Ver todos los registros')
    print('2. Insertar registro persona')
    print('3. Actualizar registro')
    print('4. Eliminar registro')
    print('5. Exit\n')

    menu = input('Ingrese una Opcion: ')
    print('\n')

    if menu == '1':
        # Seleccionar Objetos
        personas = PersonaDAO.seleccionar()
        for persona in personas:
            log.debug(persona)

    elif menu == '2':
        # Insertar un Registro
        nombre = input('Ingrese nombre: ')
        apellido = input('Ingresar apellido: ')
        email = input('Ingresar email: ')
        persona = Persona(nombre=nombre, apellido=apellido, email=email)
        personas_insertadas = PersonaDAO.insertar(persona)
        log.debug(f'Personas insertadas: {personas_insertadas}')

    elif menu == '3':
        # Actualizar un registro
        id_persona = int(input('Ingrese el ID de la persona que desee actualizar: '))
        nombre = input('Ingrese nuevo nombre: ')
        apellido = input('Ingresar nuevo apellido: ')
        email = input('Ingresar nuevo email: ')
        persona = Persona(id_persona, nombre, apellido, email)
        personas_actualizadas = PersonaDAO.actualizar(persona)
        log.debug(f'Personas actualizadas: {personas_actualizadas}')

    elif menu == '4':
        # Eliminar un registro
        id_persona = int(input('Ingrese el ID del registro que desee eliminar: '))
        persona1 = Persona(id_persona=id_persona)
        personas_eliminadas = PersonaDAO.eliminar(persona1)
        log.debug(f'Personas eliminadas: {personas_eliminadas}')

    elif menu == '5':
        break

    else:
        print('Opcion ingresada invalida...')
