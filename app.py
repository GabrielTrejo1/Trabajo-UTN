from PyQt5.QtWidgets import QApplication
from gui.cliente import Clientes

class App():
    def __init__(self):
        self.App = QApplication([])
        self.cliente = Clientes()
        self.App.exec()