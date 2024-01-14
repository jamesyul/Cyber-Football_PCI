import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QLabel, QPushButton, QComboBox, 
                             QTableWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QFileDialog,
                             QMessageBox, QGridLayout, QSizePolicy, QTableWidgetItem)
from PyQt5.QtGui import QFont, QPixmap, QImageReader
from PyQt5.QtCore import Qt
import subprocess
import pandas as pd
import csv
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

class LoginWindow(QWidget):
    def _init_(self):
        super()._init_()
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
        imagen_path = "/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/APP/cyber_football.jpeg"
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

        # Crear tabla team_table
        self.team_table = QTableWidget()
        self.team_table.setColumnCount(2)
        self.team_table.setHorizontalHeaderLabels(['Nombre', 'Posición'])
        
        self.setLayout(layout)
        
    def login(self):
        print('Hacer login con:', self.email_entry.text(), self.password_entry.text())
        
        # Aquí iría la lógica para validar los datos

        try:
            # Leer el archivo CSV
            equipo_df = pd.read_csv("/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/ETL/scrap_equipo/equipo_fantasy.csv")

            # Crear la tabla team_table antes de acceder a ella
            self.team_table = QTableWidget()
            self.team_table.setColumnCount(2)
            self.team_table.setHorizontalHeaderLabels(['Nombre', 'Posición'])

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
    def _init_(self):
        super()._init_()
        self.setWindowTitle('Mi Aplicación')
        self.setFixedSize(800, 400)

        # Create layouts
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        mid_layout = QHBoxLayout()
        bot_layout = QHBoxLayout()

        # Create widgets
        self.model_combo = QComboBox()
        self.model_combo.addItems(['Random Forest(Recomendado)', 'Regresión Lineal', 'Red Neuronal'])


        self.position_combo = QComboBox()
        self.position_combo.addItems(['General', 'Delantero', 'Mediocentro', 'Portero', 'Defensa'])

        self.suggest_button = QPushButton('Sugerir')
        self.suggest_button.clicked.connect(self.sugerirEquipo)

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
        with open('/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/ETL/scrap_equipo/equipo_fantasy.csv', 'r') as csvfile:
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
    
    def sugerirEquipo(self):
        # Obtener la opción seleccionada en el QComboBox
        selected_model = self.model_combo.currentText()
<<<<<<< HEAD

        # Verificar si la opción seleccionada es 'Random Forest(Recomendado)'
        if selected_model == 'Random Forest(Recomendado)':
            # Ruta del archivo .ipynb
            notebook_path = '/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/ML/Random Forest/RandomForest.ipynb'

            # Ejecutar el archivo .ipynb
            try:
                with open(notebook_path, 'r') as f:
                    notebook = nbformat.read(f, as_version=4)

                # Configurar el ejecutor
                executor = ExecutePreprocessor(timeout=600, kernel_name='python3')

                # Ejecutar el notebook
                executor.preprocess(notebook, {'metadata': {'path': '/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/ML/Random Forest/'}})

                # Guardar el resultado en un archivo CSV
                resultado_csv = '/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/ML/Random Forest/sugerencia.csv'

                # Leer el archivo CSV y mostrar los resultados en la tabla de sugerencias
                self.mostrarResultadosEnTabla(resultado_csv)

            except Exception as e:
                print(f"Error al ejecutar el notebook: {e}")

    def mostrarResultadosEnTabla(self, csv_path):
        # Limpiar la tabla de sugerencias
        self.suggestion_table.setRowCount(0)

        # Leer el archivo CSV y mostrar los resultados en la tabla
        try:
            sugerencia_df = pd.read_csv(csv_path)
            for row_index, row_data in sugerencia_df.iterrows():
                self.suggestion_table.insertRow(row_index)
                self.suggestion_table.setItem(row_index, 0, QTableWidgetItem(str(row_data['Nombre'])))
                #self.suggestion_table.setItem(row_index, 1, QTableWidgetItem(str(row_data['Posición'])))

        except Exception as e:
            print(f"Error al leer el archivo CSV de sugerencias: {e}")
=======
>>>>>>> a53c626a82aff1cad43cd26d1016a8498c74ae95

        # Verificar si la opción seleccionada es 'Random Forest(Recomendado)'
        if selected_model == 'Random Forest(Recomendado)':
            # Ruta del archivo .ipynb
            notebook_path = '/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/ML/Random Forest/RandomForest.ipynb'

            # Ejecutar el archivo .ipynb
            try:
                with open(notebook_path, 'r') as f:
                    notebook = nbformat.read(f, as_version=4)

                # Configurar el ejecutor
                executor = ExecutePreprocessor(timeout=600, kernel_name='python3')

                # Ejecutar el notebook
                executor.preprocess(notebook, {'metadata': {'path': '/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/ML/Random Forest/'}})

                # Guardar el resultado en un archivo CSV
                resultado_csv = '/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/ML/Random Forest/sugerencia.csv'

                # Leer el archivo CSV y mostrar los resultados en la tabla de sugerencias
                self.mostrarResultadosEnTabla(resultado_csv)

            except Exception as e:
                print(f"Error al ejecutar el notebook: {e}")

    def mostrarResultadosEnTabla(self, csv_path):
        # Limpiar la tabla de sugerencias
        self.suggestion_table.setRowCount(0)

        # Leer el archivo CSV y mostrar los resultados en la tabla
        try:
            sugerencia_df = pd.read_csv(csv_path)
            for row_index, row_data in sugerencia_df.iterrows():
                self.suggestion_table.insertRow(row_index)
                self.suggestion_table.setItem(row_index, 0, QTableWidgetItem(str(row_data['Nombre'])))
                #self.suggestion_table.setItem(row_index, 1, QTableWidgetItem(str(row_data['Posición'])))

        except Exception as e:
            print(f"Error al leer el archivo CSV de sugerencias: {e}")

if _name_ == '_main_':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())