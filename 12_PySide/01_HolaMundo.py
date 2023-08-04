import sys

from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

# Clase base de Qt (PySide), Qt y PySide son similares, cambia solamente que Qt es la version de paga
# Se encarga de procesar los eventos (event loop)
app = QApplication()

# Crear un objeto ventana
# Cualquier componente puede ser una ventana en PySide
# ventana = QPushButton('Boton')
ventana = QMainWindow()

# Cambiar titulo de la ventana
ventana.setWindowTitle('Hola Mundo con PySide')

# Modificar tamaño de la ventana
ventana.resize(600, 400)

# Mostrar ventana
ventana.show()

# Para ejecutar la aplicacion
sys.exit(app.exec())
