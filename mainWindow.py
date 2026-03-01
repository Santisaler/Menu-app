import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from menu_data import ProyectoMenu
from carteles import  carteles_individuales


class my_mainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.proyecto4 = ProyectoMenu()
        self.carteles = carteles_individuales()
        self.proyecto4.inicializarUI()
        self.carteles.inicializarUI()
        self.proyecto4.show()
        self.carteles.hide()

        # conexión entre ventanas diseñanas 
        self.proyecto4.openCartelesSignal.connect(self.open_carteles) # open carteles.py
        self.carteles.openMainSignal.connect(self.open_main) # open main_project.py
     
    def open_carteles(self,data):
        """ when a signal is emitted, my_mainWindow knows that it is necessary to switch windows (to 'carteles') """
        self.carteles.set_data(data)
        self.proyecto4.hide()
        self.carteles.show()

    def open_main(self):
        self.proyecto4.show()
        self.carteles.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv) # Por consola puedo pasarle parámetros a la app
    ventana = my_mainWindow()
    #ventana.inicializarUI()  # No quiero UI al ser el main que controla OTRAS ventanas
    #ventana.show() # Al ser el main que controla las OTRAS ventanas, no quiero que me abra nada.
    sys.exit(app.exec()) 