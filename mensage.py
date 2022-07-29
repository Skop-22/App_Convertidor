from gui.ui_untitled import *
from PySide6.QtCore import QPropertyAnimation
from PySide6 import QtCore


class MensageAn(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.Mens = Ui_MensD()
        self.Mens.setupUi(self)
        # Quita barra de maximisar minimizar y cerrar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Quita Widget_central

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.Mens.widget_3.mouseMoveEvent = moveWindow
        # -------Fin de mover ventana

    # -----metodo para mover la ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def TituLO(self, Titulo, Conte, Conten2):
        Contenido = Conte+"\nR="+Conten2
        if Conten2 != "0":
            self.Mens.Tema.setText("Resultado De la convercion "+Titulo)
            self.Mens.Contenido.setText(Contenido)
        else:
            self.Mens.Tema.setText("ERROR")
            self.Mens.Contenido.setText(
                "Hubo un error al introducir los datos")

    def AnimacionBenta(self):
        self.Animacion = QPropertyAnimation(
            self, b'geometry')
        self.Animacion.setDuration(100)
        self.Animacion.setStartValue(QRect(400, 100, 566, 72))
        self.Animacion.setEndValue(QRect(400, 300, 566, 176))
        self.Animacion.start()
        pass
