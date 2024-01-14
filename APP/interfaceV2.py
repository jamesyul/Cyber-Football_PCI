import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QLabel, QPushButton, QComboBox, 
                             QTableWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QFileDialog,
                             QMessageBox, QGridLayout, QSizePolicy, )
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Cyber Football - Login')
        self.setFixedSize(1000, 500)
        self.setStyleSheet("background-color: dark;")

        # Crear layouts
        #layout = QVBoxLayout()
        layout_form = QFormLayout()
        form_layout = QFormLayout()
        layout = QGridLayout()

        # Sección izquierda
        self.label_imagen = QLabel()
        self.imagen = QPixmap("/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/APP/cyber_football.jpeg")
        self.label_imagen.setFixedSize(500, 500) # ancho, alto
        layout.addWidget(self.label_imagen, 0, 0)
        self.label_imagen.setPixmap(self.imagen)
        layout.addWidget(self.label_imagen, 0, 0, 2, 1)

        # Sección derecha 
        layout_form = QFormLayout()
        self.email_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
    
        layout_form.addRow('Usuario:', self.email_entry)
        layout_form.addRow('Contraseña:', self.password_entry)
    
        layout.addLayout(layout_form, 0, 1)
    
        # Botones inferiores
        self.btn_seleccionar = QPushButton('V')
        self.btn_seleccionar.clicked.connect(self.seleccionarImagen)
        self.setLayout(layout)

        self.label_imagen=QLabel(self)
        self.label_imagen.setAlignment(Qt.AlignCenter)
        self.imagen = QPixmap("/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/APP/Profile-PNG-Images.png")
        self.btn_seleccionar=QPushButton('V')  
        self.btn_seleccionar.clicked.connect(self.seleccionarImagen)
        
        # Crear widgets
        self.email_entry = QLineEdit()
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        #Crea una imagen
        layout.addWidget(self.label_imagen)
        self.btn_seleccionar.setFixedSize(20, 20)
        layout.addWidget(self.btn_seleccionar,0,0,1,1)#0,0

        # Añadir widgets al layout
        form_layout.addRow('Usuario:', self.email_entry)
        form_layout.addRow('Contraseña:', self.password_entry)
        
        # Añadir form layout al main layout
        layout.addLayout(form_layout, 0, 1)

        # Crear botón login
        login_button = QPushButton('Iniciar Sesión')
        login_button.setFixedSize(120,30)
        login_button.setStyleSheet("background-color: dark")
        login_button.clicked.connect(self.login)
        layout.addWidget(login_button,2,1)#2,1

        # Crear espacio flexible para centrar el botón
        #spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        #layout.addItem(spacer, 2, 0)  # Antes del botón  
        #layout.addWidget(login_button, 2, 1)
        #layout.addItem(spacer, 2, 2)  # Después del botón

        login_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        layout.setAlignment(login_button, Qt.AlignVCenter)

        button_info = QPushButton('?')
        button_info.setFixedSize(30, 30) 
        button_info.clicked.connect(self.mostrarInstrucciones)
        layout.addWidget(button_info)

        
        self.setLayout(layout)
        
    def login(self):
        print('Hacer login con:', self.email_entry.text(), self.password_entry.text())
        
        # Aquí iría la lógica para validar los datos
        
        self.window2 = MainWindow() 
        self.close()
        self.window2.show()

    def seleccionarImagen(self):
        ruta_imagen, _ = QFileDialog.getOpenFileName(self, "Seleccionar imagen", "", "Image Files (*.png *.jpg *jpeg *.bmp)")
        if ruta_imagen:
            self.imagen=QPixmap(ruta_imagen) 
            self.label_imagen.setPixmap(self.imagen) 

    def mostrarInstrucciones(self):
        mensaje = QMessageBox()
        mensaje.setText('Aquí están las instrucciones')
        mensaje.exec_() 

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mi Aplicación')
        self.setFixedSize(600, 400)
        
        # Crear layouts
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        mid_layout = QHBoxLayout()
        bot_layout = QHBoxLayout()
        
        # Crear widgets
        self.model_combo = QComboBox()
        self.model_combo.addItems(['Random Forest(Recomendado)', 'Regresión Lineal', 'Red Neuronal'])
        
        self.position_combo = QComboBox()
        self.position_combo.addItems(['General', 'Delantero', 'Mediocentro', 'Portero', 'Defensa'])
        
        self.suggest_button = QPushButton('Sugerir')
        
        self.team_table = QTableWidget()
        self.team_table.setColumnCount(2)
        self.team_table.setHorizontalHeaderLabels(['Nombre', 'Posición']) 
        self.team_table.setRowCount(3)
        
        self.suggestion_table = QTableWidget()
        self.suggestion_table.setColumnCount(2)
        self.suggestion_table.setHorizontalHeaderLabels(['Nombre', 'Posición'])
        
        # Añadir widgets a los layouts
        top_layout.addStretch()
        top_layout.addWidget(self.model_combo)
        top_layout.addWidget(self.position_combo)
        top_layout.addWidget(self.suggest_button)
        
        mid_layout.addWidget(self.team_table)
        mid_layout.addWidget(self.suggestion_table)
        
        bot_layout.addStretch()
        suggest_button = QPushButton('Sugerir Equipo')
        suggest_button.setFont(QFont('Arial', 15)) 
        bot_layout.addWidget(suggest_button)
        
        # Añadir layouts al main layout
        layout.addLayout(top_layout)
        layout.addLayout(mid_layout)
        layout.addLayout(bot_layout)
        
        self.setLayout(layout)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())