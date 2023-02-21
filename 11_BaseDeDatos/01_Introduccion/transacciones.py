"""
Renombramos la carpeta de importacion de "psycopg2"  a "bd" con la palabra reservada "as"
"""

import psycopg2 as bd


conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    conexion.autocommit = False  # este comando sirve para que no  se guarde el registro de forma automatica
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Claudia', 'Aguabarrena', 'mesparza@gmail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Anahi', 'Abella', 'anahi_abella@gmail.com', 16)
    cursor.execute(sentencia, valores)

    conexion.commit()
    print('Termina la transaccion, se hizo commit...')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un ERROR, se hizo un rollback de la transaccion: {e}')
finally:
    conexion.close()