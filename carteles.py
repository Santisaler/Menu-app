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
import win32com.client
from PySide6.QtCore import Signal
from style.styles_carteles import styles_carteles
from properties.carteles_classes import set_classes  

class carteles_individuales(QMainWindow):
    openMainSignal = Signal()
    
    def __init__(self):
        super().__init__()
        self.setStyleSheet(styles_carteles)
        self.ui = Ui_MainWindow() # Inicializo la pantalla creada en QtDesigner
        self.ui.setupUi(self)
        self.data = None  # <--- donde se guardará el diccionario
        self.templates = {} # diccionary that will be used later on


    def inicializarUI(self):
        self.setWindowTitle("Creación individual de carteles de precios")
        set_classes(self.ui) # I use classes for the style. Created in a different module (check properties)
        self.ui.load_file_1.clicked.connect(lambda: self.load_file_path("p22", self.ui.path_sign_1)) # path_sign_x are lineEdits!
        self.ui.load_file_2.clicked.connect(lambda: self.load_file_path("p28", self.ui.path_sign_2))
        self.ui.load_file_3.clicked.connect(lambda: self.load_file_path("p43", self.ui.path_sign_3))
        self.ui.load_file_4.clicked.connect(lambda: self.load_file_path("p37", self.ui.path_sign_4))
        self.ui.load_file_5.clicked.connect(lambda: self.load_file_path("p45", self.ui.path_sign_5))
        self.ui.load_file_6.clicked.connect(lambda: self.load_file_path("p1", self.ui.path_sign_6))
        #self.resize(500, 350) # EMPIEZA con este tamaño pero al agrandar, el tamaño lo ajusta el layout
        self.ui.generate_button.clicked.connect(self.generate_signs)

    def load_file_path(self, food_code, line_edit):
        """ set a path to a specific file  """
        path_file, _ = QFileDialog.getOpenFileName(
        self,
        "Seleccionar WORD",
        "",
        "WORD (*.docx)"
        )
        if path_file:   # if there is a valid path...
            #template_name = os.path.basename(path) # initial word name
            line_edit.setText(path_file)
            self.templates[food_code] = path_file  # <-----  Guardo EN EL DICCIONARIO
    
    
    def set_data(self, datos):  
        """ function that receives data from the other window.py (interconnection) """
        self.data = datos      
        print("Datos recibidos:", self.data)

    
    def generate_signs(self):
        """ Main function that generates all the files with data gathered from the menu """
        if not self.data:
            QMessageBox.warning(self, "Error", "No data received")
            return

        if not self.templates:
            QMessageBox.warning(self, "Error", "No templates selected")
            return

        folder_path = self.set_new_location()
        files_generated = 0

        for food_id, templates_path in self.templates.items():
            if food_id in self.data:
                doc = DocxTemplate(templates_path)
                doc.render(self.data)

                # nombre original
                original_name = os.path.basename(templates_path)

                # separar nombre y extensión
                name, ext = os.path.splitext(original_name)

                # agregar _generated
                new_filename = f"{name}_generated{ext}"

                # unir ubicacion carpeta nueva + nombre nuevo
                output_path = os.path.join(folder_path, new_filename)

                doc.save(output_path)
                files_generated+=1

        if files_generated>0:
            QMessageBox.information(self,"Info", f"Se han guardado {files_generated} archivos con éxito.")  
        else:
            QMessageBox.warning(self,"Aviso","No se generó ningún archivo.")

        
        if self.ui.pdf_checkBox.isChecked() == True:
            self.pdf_generation(folder_path)
            self.openMainSignal.emit() # with this signal, carteles.py knows that something must happen


    
    
    def set_new_location(self):
        """ A directory must be set in order to locate generated files """
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Seleccionar carpeta para guardar carteles"
        )

        if not folder_path:
            return None

        return folder_path


    def pdf_generation(self, folder_path):
        """
        Convierte todos los _generated.docx dentro de la carpeta a PDF.
        """

        try:
            word = win32com.client.Dispatch("Word.Application")
            word.Visible = False

            for file in os.listdir(folder_path):
                if file.endswith("_generated.docx"): # solo agarrar los .word previamente generados
                    
                    # Crear nombre PDF
                    docx_path = os.path.join(folder_path, file)
                    pdf_path = os.path.splitext(docx_path)[0] + ".pdf"

                    doc = word.Documents.Open(docx_path)
                    doc.SaveAs(pdf_path, FileFormat=17) # 17 = formato PDF
                    doc.Close()

            word.Quit()
            return True

        except Exception as e:
            print("Error generando PDFs:", e)
            return False
        
#if __name__ == '__main__':
#    app = QApplication(sys.argv) # Por consola puedo pasarle parámetros a la app
#    ventana = carteles_individuales()
#    ventana.inicializarUI() 
#    ventana.show() # Visualizar ventana
#    sys.exit(app.exec()) 
 
""" 
p22: Milanesa con ensalada y puré
p28: Pollo grillé
p37: Sandwich milanesa con lechuga y tomate
p43: Ravioles con estofado
p45: Tallarines con estofado
"""

