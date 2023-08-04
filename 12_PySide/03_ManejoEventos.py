# Signals y Slots
import sys

from PySide6.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit, QVBoxLayout


class VentanaPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Signals and Slots')
        self.resize(400, 200)
        # Definimos la etiqueta y linea de edicion
        self.etiqueta = QLabel()
        self.entrada_texto = QLineEdit()
        # Conectar el widget de entrada_texto con la etiqueta
        # la señal es textChanged, el slot es setText
        self.entrada_texto.textChanged.connect(self.etiqueta.setText)
        # Publicamos los componentes usando un layout
        disposicion = QVBoxLayout()
        disposicion.addWidget(self.entrada_texto)
        disposicion.addWidget(self.etiqueta)


if __name__ == '__main__':
    # Creamos el objeto aplicacion
    app = QApplication([])
    # Creamos una instancia de nuestra clase
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())
