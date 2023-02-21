from logger_base import log
from psycopg2 import pool


class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

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
                log.debug(f'Creacion de Pool exitosa: {cls._pool}')
                return cls._pool
            except Exception as e:
                log.debug(f'Ocurrio un error al obtener el Pool: {e}')
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        log.debug(f'Conexion obtenida del Pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        log.debug(f'Regresamos la Conexion al Pool: {conexion}')

    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()


if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    Conexion.liberarConexion(conexion2)
