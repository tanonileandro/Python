"""
Con el metodo 'with' ademas de guardar automaticamente los datos ingresados, en caso de que haya algun error hace
'rollback' automaticamente...
"""

import psycopg2 as bd


conexion = bd.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Roxana', 'Fabrizzi', 'rf@gmail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Antonio', 'Tanoni', 'antoniotanoni@gmail.com', 14)
            cursor.execute(sentencia, valores)

            conexion.commit()

except Exception as e:
    print(f'Ocurrio un ERROR, se hizo un rollback de la transaccion: {e}')
finally:
    conexion.close()

print('Termina la transaccion, se hizo commit...')
