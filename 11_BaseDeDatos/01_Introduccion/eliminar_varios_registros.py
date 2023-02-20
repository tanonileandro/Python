import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporcione los id_persona que desee eliminar (separados por coma): ')
            valores = (tuple(entrada.split(',')),)  # Siempre se pone una coma para que lo tome como una tupla de
            # valores
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount  # para saber la cantidad de registros que se agregaron
            print(f'Registros Eliminados: {registros_eliminados}')
            print(valores)
except Exception as e:
    print(f'Ocurrio un ERROR: {e}')
finally:
    conexion.close()