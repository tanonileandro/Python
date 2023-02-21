"""
1) Al momento de abrir un archivo, si esta ubicado por fuera de la carpeta, debemos indicar exacto donde se encuentra
    ejemplo: 'C:\\Users\\Tanoni\\Documents\\Archivos\\Cursos\\Python\\Archivos\\Leccion01\\Prueba.txt'
    En este caso al estar los dos archivos en el mismo lugar no hace falta..
2) En windows todas las diagonales tienen que ser doble diagonal inversa, ya que una sola es un salto
"""

archivo = open('prueba.txt', 'r', encoding='utf8')
print(archivo.read())  # Cuando se ejecuta esta linea finaliza la ejecucion del archivo

archivo.close()  # Siempre se recomienda cerrar los archivos
