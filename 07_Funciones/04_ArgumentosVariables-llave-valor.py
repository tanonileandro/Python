def listaTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')


listaTerminos(IDE='Integrated Development Environment', PK='Primary Key')
listaTerminos(DBMS='Database Management System')
