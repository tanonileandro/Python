import psycopg2

conexion = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', port='5432', database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (
                ('Juan', 'Perez', 'jperez@gmail.com', 3),
                ('Carla', 'Martinez', 'carla_m@gmail.com', 4)
            )
            cursor.executemany(sentencia, valores)
            registros_insertados = cursor.rowcount  # para saber la cantidad de registros que se agregaron
            print(f'Registros Actualizados: {registros_insertados}')
            print(valores)
except Exception as e:
    print(f'Ocurrio un ERROR: {e}')
finally:
    conexion.close()