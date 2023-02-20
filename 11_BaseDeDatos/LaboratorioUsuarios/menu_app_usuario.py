from logger_base import log
from Usuario import Usuario
from UsuarioDao import UsuarioDAO

while True:
    print('-' * 50)
    print('Bienvenidos a la base de datos'.center(50, ' '))
    print('-' * 50)
    print('1. Listar usuarios')
    print('2. Agregar usuario')
    print('3. Actualizar usuario')
    print('4. Eliminar usuario')
    print('5. Salir\n')

    opcion = input('Ingrese una opción del MENU (1-5):\n')

    if opcion == '1':
        # Listar usuarios
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            print(usuario)

    elif opcion == '2':
        # Agregar usuario
        username = input('Ingrese su username: ')
        password = input('Ingrese su password: ')
        usuario = Usuario(username=username, password=password)
        usuario_insertado = UsuarioDAO.insertar(usuario)
        print(f'Usuario insertado: {usuario_insertado}')

    elif opcion == '3':
        # Actualizar usuario
        id_usuario = int(input('Ingrese el ID del Usuario que quiere actualizar: '))
        username = input('Ingrese el nuevo username: ')
        password = input('Ingresar el nuevo password: ')
        usuario = Usuario(id_usuario, username, password)
        usuario_actualizado = UsuarioDAO.actualizar(usuario)
        print(f'Usuario actualizado: {usuario_actualizado}')

    elif opcion == '4':
        # Eliminar usuario
        id_usuario = int(input('Ingrese el ID del del usuario que desee eliminar: '))
        usuario = Usuario(id_usuario=id_usuario)
        usuario_eliminado = UsuarioDAO.eliminar(usuario)
        print(f'Usuario eliminado: {usuario_eliminado}')

    elif opcion == '5':
        print('Salimos de la aplicación')
        break

    else:
        print('Opción ingresada invalida...')
