"""
Procesar varios registros utilizando otra sentencia
"""

import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # llaves_primarias = ((1, 2, 3),)
            entrada = input('Proporcione los id\' a buscar (separados por comas): ')
            llaves_primarias = (tuple(entrada.split(',')),)  # Este comando elimina las comas y forma una tupla
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'Ocurrio un ERROR: {e}')
finally:
    conexion.close()
