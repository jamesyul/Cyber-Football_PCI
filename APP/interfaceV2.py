# -*- coding: utf-8 -*-
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
        imagen_path = "/Users/yulcardenas/Desktop/2023_24/PCI_EXTRA/Cyber-Football_PCI/APP/cyber_football.jpeg"
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
        self.imagen = QPixmap("/Users/yulcardenas/Desktop/2023_24/PCI_EXTRA/Cyber-Football_PCI/APP/Profile-PNG-Images.png")
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

        # Crear tabla team_table
        self.team_table = QTableWidget()
        self.team_table.setColumnCount(2)
        self.team_table.setHorizontalHeaderLabels(['Nombre', 'Precio'])
        
        self.setLayout(layout)
        
    def login(self):
        print('Hacer login con:', self.email_entry.text(), self.password_entry.text())
        
        # Aquí iría la lógica para validar los datos

        # Ejecutar notebook
        #notebook_path = '/Users/yulcardaso/Desktop/NUEVO_CURSO/PCI/Cyber-Football_PCI/ETL/scrap_equipo/Scrapper_equipo.ipynb'
        #with open(notebook_path) as f:
        #    notebook = nbformat.read(f, as_version=4)

        #executor = ExecutePreprocessor(timeout=600, kernel_name='python3')  
        #executor.preprocess(notebook)

        # Pasar a ventana principal
        self.window2 = MainWindow()
        self.close()
        self.window2.show()

        try:
            # Leer el archivo CSV
            equipo_df = pd.read_csv("/Users/yulcardenas/Desktop/2023_24/PCI_EXTRA/Cyber-Football_PCI/ETL/scrap_equipo/equipo_fantasy.csv")

            # Crear la tabla team_table antes de acceder a ella
            self.team_table = QTableWidget()
            self.team_table.setColumnCount(2)
            self.team_table.setHorizontalHeaderLabels(['Nombre', 'Precio'])

            # Limpiar la primera tabla
            self.team_table.setRowCount(0)

            # Mostrar los nombres y posiciones en la primera tabla
            for row_index, row_data in equipo_df.iterrows():
                self.team_table.insertRow(row_index)
                self.team_table.setItem(row_index, 0, QTableWidgetItem(str(row_data['Nombre'])))
                self.team_table.setItem(row_index, 1, QTableWidgetItem(str(row_data['Precio'])))

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

    

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mi Aplicación')
        self.setFixedSize(930, 400)

        # Create layouts
        layout = QVBoxLayout()
        top_layout = QHBoxLayout()
        mid_layout = QHBoxLayout()
        bot_layout = QHBoxLayout()

        # Create widgets
        self.model_combo = QComboBox()
        self.model_combo.addItems(['Regresión Lineal(Recomendado)','Random Forest', 'Red Neuronal'])


        self.position_combo = QComboBox()
        self.position_combo.addItems(['General', 'Delantero', 'Mediocentro', 'Portero', 'Defensa'])

        self.suggest_button = QPushButton('Sugerir')
        self.suggest_button.clicked.connect(self.sugerirEquipo)

        self.team_table = QTableWidget()
        self.team_table.setColumnCount(4)
        self.team_table.setHorizontalHeaderLabels(['Nombre', 'Puntos', 'Posición', 'Precio'])
        
        # Call a method to populate the team_table with data from 'jugadores.csv'
        self.populate_team_table()

        self.suggestion_table = QTableWidget()
        self.suggestion_table.setColumnCount(4)
        self.suggestion_table.setHorizontalHeaderLabels(['Nombre', 'Puntos', 'Posición', 'Precio'])

        button_info = QPushButton('?')
        button_info.setFixedSize(30, 30) 
        button_info.clicked.connect(self.mostrarInstrucciones)
        layout.addWidget(button_info)

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

    def mostrarInstrucciones(self):
        mensaje = QMessageBox()
        mensaje.setText('CYBER FOOTBALL\n'
                        '\n'
                        'Bienvenido a Cyber Football, la aplicación que te \n'
                        'ayudará a ganar la Liga en Mr Fantasy. \n'
                        '\n'
                        '1) Selecciona el modelo de inteligencia artificial\n'
                        'que deseas utilizar para sugerir tu equipo.\n'
                        '\n'
                        '\tPrecisión de puntos: \n'
                        '\n'
                        '\tA)Regresión Lineal - más preciso\n'
                        '\tB)Random Forest\n'
                        '\tC)Redes Neuronales - menos preciso\n'
                        '\n'
                        '2) Selecciona la posición de los jugadores que deseas\n'
                        'sugerir.\n'
                        '3) Pulsa el botón "Sugerir" para obtener tu equipo\n'
                        'ideal. \n')
        mensaje.exec_() 

    # Funcion de creacion de tabla y enseñar el equipo
    def populate_team_table(self):
        with open('/Users/yulcardenas/Desktop/2023_24/PCI_EXTRA/Cyber-Football_PCI/ETL/scrap_equipo/equipo_fantasy.csv', 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            header = next(csv_reader)  # Skip the header row
            row_count = 0
            for row in csv_reader:
                if row_count < 12:  # Display the first 5 rows
                    nombre = row[0]
                    precio = row[1]
                    puntos=row[4]
                    posicion=row[3]
                    self.team_table.insertRow(row_count)
                    self.team_table.setItem(row_count, 0, QTableWidgetItem(nombre))
                    self.team_table.setItem(row_count, 2, QTableWidgetItem(puntos))
                    self.team_table.setItem(row_count, 1, QTableWidgetItem(posicion))
                    self.team_table.setItem(row_count, 3, QTableWidgetItem(precio))
                    row_count += 1
    
    def sugerirEquipo(self):
        # Obtener la opción seleccionada en el QComboBox
        selected_model = self.model_combo.currentText()
        selected_position = self.position_combo.currentText()

        base_path = '/Users/yulcardenas/Desktop/2023_24/PCI_EXTRA/Cyber-Football_PCI/ML/'

        if selected_model == 'Random Forest':
            model_path = base_path + 'Random Forest/'
            notebook_path = model_path + 'RandomForest.ipynb'   
            try:
                with open(notebook_path, 'r') as f:
                    notebook = nbformat.read(f, as_version=4)
                
                # Configurar el ejecutor
                executor = ExecutePreprocessor(timeout=600, kernel_name='python3')
                
                executor.preprocess(notebook, {'metadata': {'path': model_path}})
                
                # Seleccionar el archivo CSV basado en la posición
                if selected_position == 'General':
                    resultado_csv = model_path + 'sugerencia.csv'
                elif selected_position == 'Delantero':
                    resultado_csv = model_path + 'sugerencia_delanteros.csv'
                elif selected_position == 'Mediocentro':
                    resultado_csv = model_path + 'sugerencia_mediocentros.csv'
                elif selected_position == 'Defensa':
                    resultado_csv = model_path + 'sugerencia_defensas.csv'
                elif selected_position == 'Portero':
                    resultado_csv = model_path + 'sugerencia_porteros.csv'
                else:
                    resultado_csv = model_path + 'sugerencia.csv'        
                # Leer el archivo CSV y mostrar los resultados en la tabla de sugerencias
                self.mostrarResultadosEnTabla(resultado_csv)
        
            except Exception as e:
                print(f"Error al ejecutar el notebook de Random Forest: {e}")

        # Verificar si la opción seleccionada es 'Red Neuronal'
        elif selected_model == 'Red Neuronal':
            model_path = base_path + 'Red Neuronales/'
            notebook_path = model_path + 'ML_Redes Neuronales.ipynb'   
            try:
                with open(notebook_path, 'r') as f:
                    notebook = nbformat.read(f, as_version=4)
                
                # Configurar el ejecutor
                executor = ExecutePreprocessor(timeout=600, kernel_name='python3')
                
                executor.preprocess(notebook, {'metadata': {'path': model_path}})
                
                # Seleccionar el archivo CSV basado en la posición
                if selected_position == 'General':
                    resultado_csv = model_path + 'general_prediccion.csv'
                elif selected_position == 'Delantero':
                    resultado_csv = model_path + 'delantero_prediccion.csv'
                elif selected_position == 'Mediocentro':
                    resultado_csv = model_path + 'mediocentro_prediccion.csv'
                elif selected_position == 'Defensa':
                    resultado_csv = model_path + 'defensa_prediccion.csv'
                elif selected_position == 'Portero':
                    resultado_csv = model_path + 'portero_prediccion.csv'
                else:
                    resultado_csv = model_path + 'general_prediccion.csv'        
                # Leer el archivo CSV y mostrar los resultados en la tabla de sugerencias
                self.mostrarResultadosEnTabla(resultado_csv)
        
            except Exception as e:
                print(f"Error al ejecutar el notebook de Red Neuronales: {e}")


        elif selected_model == 'Regresión Lineal(Recomendado)':
            model_path = base_path + 'Regresion_lineal/'
            notebook_path = model_path + 'Regresion_lineal_final.ipynb'   
            try:
                with open(notebook_path, 'r') as f:
                    notebook = nbformat.read(f, as_version=4)
                
                # Configurar el ejecutor
                executor = ExecutePreprocessor(timeout=600, kernel_name='python3')
                
                executor.preprocess(notebook, {'metadata': {'path': model_path}})
                
                # Seleccionar el archivo CSV basado en la posición
                if selected_position == 'General':
                    resultado_csv = model_path + 'jugadores_top_general_puntos_predicciones.csv'
                elif selected_position == 'Delantero':
                    resultado_csv = model_path + 'jugadores_top_delantero_puntos_predicciones.csv'
                elif selected_position == 'Mediocentro':
                    resultado_csv = model_path + 'jugadores_top_mediocentro_puntos_predicciones.csv'
                elif selected_position == 'Defensa':
                    resultado_csv = model_path + 'jugadores_top_defensa_puntos_predicciones.csv'
                elif selected_position == 'Portero':
                    resultado_csv = model_path + 'jugadores_top_portero_puntos_predicciones.csv'
                else:
                    resultado_csv = model_path + 'jugadores_top_general_puntos_predicciones.csv'        
                # Leer el archivo CSV y mostrar los resultados en la tabla de sugerencias
                self.mostrarResultadosEnTabla(resultado_csv)
        
            except Exception as e:
                print(f"Error al ejecutar el notebook de Regresion Lineal: {e}")

    def mostrarResultadosEnTabla(self, csv_path):
        # Limpiar la tabla de sugerencias
        self.suggestion_table.setRowCount(0)
        #selected_model = self.position_combo.currentText()

        # Leer el archivo CSV y mostrar los resultados en la tabla
        try:
            sugerencia_df = pd.read_csv(csv_path)
            
            # Imprimir los nombres de las columnas en el DataFrame
            print("Nombres de columnas en sugerencia_df:", sugerencia_df.columns)
            
            # Verificar si las columnas 'Nombre' y 'Precio' están presentes en el DataFrame
            if 'Nombre' in sugerencia_df.columns and 'Puntos' in sugerencia_df.columns and 'Posicion' in sugerencia_df.columns and 'Precio' in sugerencia_df.columns:
                for row_index, row_data in sugerencia_df[['Nombre', 'Puntos', 'Posicion', 'Precio']].iterrows():
                    self.suggestion_table.insertRow(row_index)
                    self.suggestion_table.setItem(row_index, 0, QTableWidgetItem(str(row_data['Nombre'])))
                    self.suggestion_table.setItem(row_index, 1, QTableWidgetItem(str(row_data['Puntos'])))
                    self.suggestion_table.setItem(row_index, 2, QTableWidgetItem(str(row_data['Posicion'])))
                    self.suggestion_table.setItem(row_index, 3, QTableWidgetItem(str(row_data['Precio'])))
            else:
                print("Las columnas 'Nombre' y 'Precio' no están presentes en el DataFrame.")

        except Exception as e:
            print(f"Error al leer el archivo CSV de sugerencias: {e}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())