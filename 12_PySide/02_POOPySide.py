import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton


class VentanaPySide(QMainWindow):
    def __init__(self):
        # Llamamos al metodo init de la clase padre
        super().__init__()
        self.setWindowTitle('POO con PySide')
        # self.resize(600, 400)
        # Tamaño de la ventana pero de manera fija
        self.setFixedSize(QSize(600, 400))
        # Creamos componentes
        self._agregar_componentes()

    def _agregar_componentes(self):
        # Agregamos un menu
        menu = self.menuBar()
        menu_archivo = menu.addMenu('Archivo')
        menu_preferencias = menu.addMenu('Preferencias')
        # Agregamos algunas opciones al Menu
        accion_nuevo = QAction('Nuevo', self)
        accion_ventana = QAction('Tamaño de Ventana', self)
        menu_archivo.addAction(accion_nuevo)
        menu_preferencias.addAction(accion_ventana)
        # Agregamos un texto a la barra de estado
        accion_nuevo.setStatusTip('Nuevo Archivo')
        # Agregamos un mensaje en la barra de estado
        self.statusBar().showMessage('Informacion de la barra de estado')
        # Agregamos un boton
        boton = QPushButton('Nuevo Boton')
        # Publicamos el boton en la ventana
        self.setCentralWidget(boton)


if __name__ == '__main__':
    app = QApplication([])
    # Creamos un Objeto de tipo ventana
    ventana1 = VentanaPySide()
    ventana1.show()
    # Ejecutamos la ventana y le agregamos el modo exit para que se cierre exitosamente
    sys.exit(app.exec())

