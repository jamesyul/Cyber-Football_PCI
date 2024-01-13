from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QGridLayout
from PyQt5.QtGui import QPixmap, QPainter, QBitmap
from PyQt5.QtCore import Qt, QSize  # Agregada la importación de QSize
import re

class VentanaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setGeometry(200, 200, 300, 250)

        layout = QGridLayout()

        # Colocar el QLabel para la imagen en la fila 0, columna 0
        self.label_imagen = QLabel(self)
        self.label_imagen.setAlignment(Qt.AlignCenter)
        imagen = QPixmap("/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/Profile-PNG-Images.png")
        imagen = imagen.scaled(80, 80, Qt.KeepAspectRatio)
        self.label_imagen.setPixmap(imagen)
        self.label_imagen.setScaledContents(True)  # Ajustar el contenido automáticamente al tamaño del QLabel
        layout.addWidget(self.label_imagen, 0, 0, 1, 2)  # Span 1 fila y 2 columnas

        label_usuario = QLabel('Usuario:')
        layout.addWidget(label_usuario, 1, 0)  # Fila 1, columna 0
        self.input_usuario = QLineEdit()
        layout.addWidget(self.input_usuario, 1, 1)  # Fila 1, columna 1

        label_contrasena = QLabel('Contraseña:')
        layout.addWidget(label_contrasena, 2, 0)  # Fila 2, columna 0
        self.input_contrasena = QLineEdit()
        layout.addWidget(self.input_contrasena, 2, 1)  # Fila 2, columna 1
        self.input_contrasena.setEchoMode(QLineEdit.Password)  # Mostrar asteriscos para la contraseña

        # Colocar el botón '?' en la esquina superior derecha (fila 0, columna 2)
        button_info = QPushButton('?')
        button_info.setFixedSize(30, 30)
        button_info.clicked.connect(self.mostrarInstrucciones)
        layout.addWidget(button_info, 0, 2)  # Fila 0, columna 2

        button_login = QPushButton('Iniciar sesión')
        layout.addWidget(button_login, 3, 0, 1, 3)  # Span 1 fila y 3 columnas

        self.setLayout(layout)

    
    def crearImagenCircular(self, imagen, tamanio=(100, 100)):
        # Crear una máscara circular
        ancho, alto = tamanio
        mascara = QBitmap(QSize(ancho, alto))

        # Crear un QPainter para dibujar la máscara
        painter = QPainter(mascara)
        painter.setBrush(Qt.color1)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawEllipse(0, 0, ancho, alto)
        painter.end()

        # Aplicar la máscara a la imagen
        imagen.setMask(mascara)

        return imagen


    def mostrarInstrucciones(self):
        mensaje = QMessageBox()
        mensaje.setText('Aquí están las instrucciones')
        mensaje.exec_()

    def validarLogin(self):
        usuario = self.input_usuario.text()
        contrasena = self.input_contrasena.text()

        if not re.match(r"[^@]+@[^@]+\.[^@]+", usuario):
            mensaje_error = QMessageBox()
            mensaje_error.setText('Por favor, ingresa un correo electrónico válido.')
            mensaje_error.exec_()
            return
        

        self.input_contrasena.setEchoMode(QLineEdit.Password)
    
        if usuario == 'usuario' and contrasena == 'contrasena':
            self.abrirSegundaVentana()
        else:
            mensaje_error = QMessageBox()
            mensaje_error.setText('Usuario o contraseña incorrectos')
            mensaje_error.exec_()

    def abrirSegundaVentana(self):
        self.segunda_ventana = VentanaOpciones()
        self.segunda_ventana.show()
        self.close()

class VentanaOpciones(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Selecciona una opción')
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        textbox = QLineEdit()
        textbox.setReadOnly(True)
        layout.addWidget(textbox)

        opciones = ['Opción A', 'Opción B', 'Opción C']
        for opcion in opciones:
            button = QPushButton(opcion)
            button.clicked.connect(lambda _, opt=opcion: self.mostrarResultado(opt, textbox))
            layout.addWidget(button)

        self.resultado = QLabel('Elige una opción...')
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def mostrarResultado(self, opcion, textbox):
        # Aquí deberías tener tu lógica para mostrar el resultado según la opción seleccionada
        if opcion == 'Opción A':
            resultado = 'Resultado para la opción A'
        elif opcion == 'Opción B':
            resultado = 'Resultado para la opción B'
        else:
            resultado = 'Resultado para la opción C'
        textbox.setText(resultado)

if __name__ == '__main__':
    app = QApplication([])
    ventana_login = VentanaLogin()
    ventana_login.show()
    app.exec_()
