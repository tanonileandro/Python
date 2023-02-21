"""
Esto sirve para insertar un registro solamente
"""

import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Carlos', 'Radamel', 'crada@gmail.com')
            cursor.execute(sentencia, valores)
            # conexion.commit() -> esto no hace falta porque usamos with,  lo hace de manera automatica
            registros_insertados = cursor.rowcount  # para saber la cantidad de registros que se agregaron
            print(f'Registros insertados: {registros_insertados}')
            print(valores)
except Exception as e:
    print(f'Ocurrio un ERROR: {e}')
finally:
    conexion.close()