"""
- Si queremos solicitar informacion de algun registro en particular debemos hacer lo siguiente.
- Para que nos devuelva una tupla de valores, en "cursor.execute(sentencia, (id_persona,))", despues de "id_persona"
ponemos una coma para que tome que es una tupla, sino la toma como una variable.
- Como se le esta ordenando en la "sentencia = 'SELECT * FROM persona WHERE id_persona = %s'" que queremos
saver los datos de una sola persona, podemos recuperar los registros con "cursor.fetchone()" en vez de ".fetchall"
"""
import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input('Proporcione el id_persona que desee consultar: ')
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
    print(f'Ocurrio un ERROR: {e}')
finally:
    conexion.close()
