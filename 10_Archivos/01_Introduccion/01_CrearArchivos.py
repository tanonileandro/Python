"""
1) Para crear un archivo txt o cualquier otro se utiliza la palabra reservada "open"
    En el mismo si queremos agregar informacion escribiendo algo, usamos ".write" seguido de lo que queremos agregar
    Cuando se agrega texto, no podemos escribir directamente palabras con asento, para eso tenemos que utilizar la
    palabra reservada "ecoding='utf8'"
2) Se suele encerrar dentro del metodo "try" por si el archivo genera algun error, esto evitara que la aplicacion
deje de funcionar...
"""

try:
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Se agrega información al archivo de Prueba\n')
    archivo.write('Saludos')
except Exception as e:
    print(e)
finally:
    archivo.close()
    print('Fin del archivo')
