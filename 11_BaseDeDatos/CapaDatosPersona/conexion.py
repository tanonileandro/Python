"""
Se modifica el codigo para crear un pool de conexiones..
"""
from logger_base import log
from psycopg2 import pool


class Conexion:
    # Atributos de clase
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    # Metodos de clase
    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Creacion del pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrio un error al obtener el pool {e}')
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la conexion al pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion1)
    Conexion.cerrarConexiones()

    # @classmethod
    # def obtenerConexion(cls):
    #     pass
    #     if cls._conexion is None:
    #         try:
    #             cls._conexion = bd.connect(host=cls._HOST,
    #                                        user=cls._USERNAME,
    #                                        password=cls._PASSWORD,
    #                                        port=cls._DB_PORT,
    #                                        database=cls._DATABASE)
    #             log.debug(f'Conexion exitosa: {cls._conexion}')
    #             return cls._conexion
    #         except Exception as e:
    #             log.debug(f'Ocurrió una excepcion al obtener la conexion: {e}')
    #             sys.exit()
    #     else:
    #         return cls._conexion

    # @classmethod
    # def obtenerCursor(cls):
    #     pass
    #     if cls._cursor is None:
    #         try:
    #             cls._cursor = cls.obtenerConexion().cursor()
    #             log.debug(f'Se abrio correctamente el cursor: {cls._cursor}')
    #             return cls._cursor
    #         except Exception as e:
    #             log.error(f'Ocurrió una excepcion al obtener el cursor: {e}')
    #             sys.exit()  # Si tenemos un error se ejecuta este comando para cerrar nuestra aplicacion
    #     else:
    #         return cls._cursor
