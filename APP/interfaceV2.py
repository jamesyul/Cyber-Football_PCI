import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QLabel, QPushButton, QComboBox, 
                             QTableWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QFileDialog,
                             QMessageBox, QGridLayout, QSizePolicy, QTableWidgetItem)
from PyQt5.QtGui import QFont, QPixmap, QImageReader
from PyQt5.QtCore import Qt
import subprocess
import pandas as pd
import csv

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
        self.label_imagen.setFixedSize(500, 500)  # ancho, alto fijo
        self.label_imagen.setAlignment(Qt.AlignTop | Qt.AlignLeft)  # Alineación arriba y a la izquierda
        self.label_imagen.setContentsMargins(0, 0, 0, 0)  # Eliminar márgenes
        self.label_imagen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Cargar imagen
        imagen_path = "../APP/cyber_football.jpeg"
        if QImageReader(imagen_path).size().isValid():
            self.imagen = QPixmap(imagen_path)
            self.imagen = self.imagen.scaled(self.label_imagen.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label_imagen.setPixmap(self.imagen)

        layout.addWidget(self.label_imagen, 0, 0)


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
        self.imagen = QPixmap("../APP/Profile-PNG-Images.png")
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

        try:
            # Leer el archivo CSV
            equipo_df = pd.read_csv("D:/Users/Babag/trabajos/PC1/repositorio/Cyber-Football_PCI/ETL/scrap_equipo/equipo_fantasy.csv")

            # Limpiar la primera tabla
            self.team_table.setRowCount(0)

            # Mostrar los nombres y posiciones en la primera tabla
            for row_index, row_data in equipo_df.iterrows():
                self.team_table.insertRow(row_index)
                self.team_table.setItem(row_index, 0, QTableWidgetItem(str(row_data['Nombre'])))
                self.team_table.setItem(row_index, 1, QTableWidgetItem(str(row_data['posicion'])))

        except Exception as e:
            print(f"Error al cargar el archivo CSV: {e}")
    
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

        # Create layouts
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        mid_layout = QHBoxLayout()
        bot_layout = QHBoxLayout()

        # Create widgets
        self.model_combo = QComboBox()
        self.model_combo.currentTextChanged.connect(self.on_model_change)
        self.model_combo.addItems(['Random Forest(Recomendado)', 'Regresión Lineal', 'Red Neuronal'])

        self.position_combo = QComboBox()
        self.position_combo.addItems(['General', 'Delantero', 'Mediocentro', 'Portero', 'Defensa'])

        self.suggest_button = QPushButton('Sugerir')

        self.team_table = QTableWidget()
        self.team_table.setColumnCount(2)
        self.team_table.setHorizontalHeaderLabels(['Nombre', 'Posición'])
        
        # Call a method to populate the team_table with data from 'jugadores.csv'
        self.populate_team_table()

        self.suggestion_table = QTableWidget()
        self.suggestion_table.setColumnCount(2)
        self.suggestion_table.setHorizontalHeaderLabels(['Nombre', 'Posición'])

        # Add widgets to the layouts
        top_layout.addStretch()
        top_layout.addWidget(self.model_combo)
        top_layout.addWidget(self.position_combo)
        top_layout.addWidget(self.suggest_button)

        mid_layout.addWidget(self.team_table)
        mid_layout.addWidget(self.suggestion_table)

        bot_layout.addStretch()
        #suggest_button = QPushButton('Sugerir Equipo')
        #suggest_button.setFont(QFont('Arial', 15))
        #sbot_layout.addWidget(suggest_button)

        # Add layouts to the main layout
        layout.addLayout(top_layout)
        layout.addLayout(mid_layout)
        layout.addLayout(bot_layout)

        self.setLayout(layout)

    def populate_team_table(self):
        with open('../ETL/scrap_equipo/equipo_fantasy.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)  # Skip the header row
            row_count = 0
            for row in csv_reader:
                if row_count < 12:  # Display the first 5 rows
                    nombre = row[0]
                    posicion = row[4]
                    self.team_table.insertRow(row_count)
                    self.team_table.setItem(row_count, 0, QTableWidgetItem(nombre))
                    self.team_table.setItem(row_count, 1, QTableWidgetItem(posicion))
                    row_count += 1


    def on_model_change(self, text):
        if text == "Random Forest(Recomendado)":
            self.run_random_forest_and_update_table()

    def run_random_forest_and_update_table(self):
        # Ejecutar el notebook de Jupyter
        notebook_path = r'D:\Users\Babag\trabajos\PC1\repositorio\Cyber-Football_PCI\ML\Random Forest\RandomForest.ipynb'
        subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", notebook_path])

        # Cargar los resultados del CSV en la tabla
        csv_path = r'D:\Users\Babag\trabajos\PC1\repositorio\Cyber-Football_PCI\ML\Random Forest\sugerencia.csv'

        self.load_csv_to_table(csv_path)

    def load_csv_to_table(self, csv_path):
        try:
            with open(csv_path, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)
                self.suggestion_table.setRowCount(0) # Limpiar tabla actual
                for row_index, row in enumerate(csv_reader):
                    self.suggestion_table.insertRow(row_index)
                    for col_index, data in enumerate(row):
                        self.suggestion_table.setItem(row_index, col_index, QTableWidgetItem(data))
        except Exception as e:
            print(f"Error al cargar el archivo CSV: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())