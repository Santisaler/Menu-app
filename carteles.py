import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import * 
from ui.ui_carteles import Ui_MainWindow   # Extraigo del archivo generado por QtDesigner
from PySide6.QtGui import QStandardItemModel  # 
from PySide6.QtWidgets import QFileDialog     # Para abrir archivos de mi PC
from PySide6.QtGui import QStandardItem
from PySide6.QtGui import QIcon
import os
import pymupdf
from docxtpl import DocxTemplate
from properties.classes import set_classes
import win32com.client


class carteles_individuales(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() # Inicializo la pantalla creada en QtDesigner
        self.ui.setupUi(self)

    def inicializarUI(self):
        self.setWindowTitle("Mi primera ventana")
        #self.resize(500, 350) # EMPIEZA con este tamaño pero al agrandar, el tamaño lo ajusta el layout
        #self.ui.pushButton.clicked.connect(self.clickeoBoton1)

        

    
    
if __name__ == '__main__':
    app = QApplication(sys.argv) # Por consola puedo pasarle parámetros a la app
    ventana = carteles_individuales()
    ventana.inicializarUI()
    ventana.show() # Visualizar ventana
    sys.exit(app.exec()) 