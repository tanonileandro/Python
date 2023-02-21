"""
1) Importar "psycopg"
2) Crear Objeto conexion
3) Crear Objeto cursor, sirve para crear sentencias en SQL
4) Definir sentencia que queremos ejecutar
5) Llamar al metodo "execute" con el objeto cursor
6) Con el Objeto cursor podemos solicitar y mandar a llamar todos los registros con el metodo ".fetchall"
7) Mandamos a imprimir el registro
8) Por ultimo cerramos los Objetos cusor y conexion, aunque existe una manera automatica de que se cierren solos
"""
import psycopg2


conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            print(registros)
except Exception as e:
    print(f'Ocurrio un ERROR: {e}')
finally:
    conexion.close()
