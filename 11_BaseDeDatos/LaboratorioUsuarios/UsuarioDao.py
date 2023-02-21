"""
DAO = Data Access Object - es un patron de diseño, para conectarnos a la base de datos
CRUD = Create-Read-Update-Delete
"""

from logger_base import log
from CursorDelPool import CursorDelPool
from Usuario import Usuario


# noinspection PyShadowingNames
class UsuarioDAO:
    _SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario agregado: {usuario}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, usuario):
        try:
            with CursorDelPool() as cursor:
                valores = (usuario.username, usuario.password, usuario.id_usuario)
                cursor.execute(cls._ACTUALIZAR, valores)
                log.debug(f'Usuario actualizado: {usuario}')
                return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un ERROR: {e}')

    @classmethod
    def eliminar(cls, usuario):
        try:
            with CursorDelPool() as cursor:
                valores = (usuario.id_usuario,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Usuario eliminado: {valores}')
                return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un ERROR: {e}')


if __name__ == '__main__':
    # usuario1 = Usuario(username='Ccarlos', password=0000)
    # usuario_insertado = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Usuario insertado: {usuario_insertado}')

    # usuario1 = Usuario(id_usuario=3)
    # usuario_eliminado = UsuarioDAO.eliminar(usuario1)
    # log.debug(f'Usuario eliminado: {usuario_eliminado}')

    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
