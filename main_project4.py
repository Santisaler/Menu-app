import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import * 
from ui_project4 import Ui_MainWindow   # Extraigo del archivo generado por QtDesigner
from PySide6.QtGui import QStandardItemModel  # 
from PySide6.QtWidgets import QFileDialog     # Para abrir archivos de mi PC
from PySide6.QtGui import QStandardItem
from PySide6.QtGui import QIcon
import os
import pymupdf
from docxtpl import DocxTemplate
from style.styles import background_style
from properties.classes import set_classes
import win32com.client

class Proyecto4Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow() # Inicializo la pantalla creada en QtDesigner
        self.ui.setupUi(self)
        self.setStyleSheet(background_style)

    def inicializarUI(self):
        self.setWindowTitle("PDF application")
        set_classes(self.ui) # created in a different module (check properties)
        self.ui.pushButton.clicked.connect(self.load_initial_file)
        self.ui.generateFile.clicked.connect(self.generate_menu)
        self.ui.tabWidget.setTabText(0, "Postres y bebidas")
        self.ui.tabWidget.setTabText(1, "Cafetería")
        self.ui.tabWidget.setTabText(2, "Minutas")
        self.ui.tabWidget.setTabText(3, "Sandwichería")
        self.ui.tabWidget.setTabText(4, "Pastas")


    def load_initial_file(self):
        '''
        select an initial word file (template) from PC 
        '''
        path, _ = QFileDialog.getOpenFileName(
        self,
        "Seleccionar WORD",
        "",
        "WORD (*.docx)"
        )
        if path:   # if there is a valid path...
            #template_name = os.path.basename(path)     # initial word name
            self.ui.template_path.setText(path)


    def load_data_from_app(self):
        '''
        Take all data from inputs on the app and I return a dictionary
        '''
        cents = ",00"
        return{         ## PRICES ##
                "p1": self.ui.input_1.text() + cents,
                "p2": self.ui.input_2.text() + cents,
                "p3": self.ui.input_3.text() + cents,
                "p4": self.ui.input_4.text() + cents,
                "p5": self.ui.input_5.text() + cents,
                "p6": self.ui.input_6.text() + cents,
                "p7": self.ui.input_7.text() + cents,
                "p8": self.ui.input_8.text() + cents,
                "p9": self.ui.input_9.text() + cents,
                "p10": self.ui.input_10.text() + cents,
                "p11": self.ui.input_11.text() + cents,
                "p12": self.ui.input_12.text() + cents,
                "p13": self.ui.input_13.text() + cents,
                "p14": self.ui.input_14.text() + cents,
                "p15": self.ui.input_15.text() + cents,
                "p16": self.ui.input_16.text() + cents,
                "p17": self.ui.input_17.text() + cents,
                "p18": self.ui.input_18.text() + cents,
                "p19": self.ui.input_19.text() + cents,
                "p20": self.ui.input_20.text() + cents,
                "p21": self.ui.input_21.text() + cents,
                "p22": self.ui.input_22.text() + cents,
                "p23": self.ui.input_23.text() + cents,
                "p24": self.ui.input_24.text() + cents,
                "p25": self.ui.input_25.text() + cents,
                "p26": self.ui.input_26.text() + cents,
                "p27": self.ui.input_27.text() + cents,
                "p28": self.ui.input_28.text() + cents,
                "p29": self.ui.input_29.text() + cents,
                "p30": self.ui.input_30.text() + cents,
                "p31": self.ui.input_31.text() + cents,
                "p32": self.ui.input_32.text() + cents,
                "p33": self.ui.input_33.text() + cents,
                "p34": self.ui.input_34.text() + cents,
                "p35": self.ui.input_35.text() + cents,
                "p36": self.ui.input_36.text() + cents,
                "p37": self.ui.input_37.text() + cents,
                "p38": self.ui.input_38.text() + cents,
                "p39": self.ui.input_39.text() + cents,
                "p40": self.ui.input_40.text() + cents,
                "p41": self.ui.input_41.text() + cents,
                "p42": self.ui.input_42.text() + cents,
                "p43": self.ui.input_43.text() + cents,
                "p44": self.ui.input_44.text() + cents,
                "p45": self.ui.input_45.text() + cents,
        }
    
    def new_menu_location(self):
        new_path, _ = QFileDialog.getSaveFileName(
        self,
        "Guardar menú",
        "menu.docx",
        "Word (*.docx)"
        )

        if not new_path:
            return None

        if not new_path.endswith(".docx"):
            new_path += ".docx"

        return new_path

    def generate_menu(self):
        template_path = self.ui.template_path.text()
        if not template_path:
            QMessageBox.warning(
                self,
                "Template not selected",
                "Please select a Word template before generating the menu."
            )
            return


        datos = self.load_data_from_app() # dictionary full of data (menu's prices)
        doc = DocxTemplate(template_path)
        
        doc.render(datos)  # inserting data from dictionary to new Word file 
        new_file_path = self.new_menu_location()
        if not new_file_path:
            return
        doc.save(new_file_path)

        if self.ui.pdf_checkBox.isChecked() == True:
            self.pdf_generation(new_file_path)


    def pdf_generation(self,docx_path):
        """ When the checkbox is checked, a pdf is generated along with the word file """
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        doc = word.Documents.Open(os.path.abspath(docx_path))

        ruta_pdf = docx_path.replace(".docx", ".pdf") # docx to pdf

        #doc.SaveAs(ruta_pdf, FileFormat=17)  # 17 = PDF -- The whole document is exported to pdf
        doc.ExportAsFixedFormat(
            OutputFileName=ruta_pdf,
            ExportFormat=17,   # PDF
            OpenAfterExport=False,
            OptimizeFor=0,
            Range=3,           # 0=custom range, 1=All, 2=Selection, 3=FromTo 
            From=1,
            To=2,              # only page 1 and 2 (first and second one)
            Item=0,
            IncludeDocProps=True,
            KeepIRM=True,
            CreateBookmarks=1,
            DocStructureTags=True,
            BitmapMissingFonts=True,
            UseISO19005_1=False
        )
        doc.Close()
        word.Quit()

    
        
if __name__ == '__main__':
    app = QApplication(sys.argv) # Por consola puedo pasarle parámetros a la app
    ventana = Proyecto4Window()
    ventana.inicializarUI() 
    ventana.show() # Visualizar ventana
    sys.exit(app.exec()) 