from PySide6 import QtCore
from gui.ui_Principal import *
from Funcionalidad.funccion import *
from mensage import *
import sys


class Principal(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.prin = Ui_MainWindow()
        self.prin.setupUi(self)
        self.MensaD = MensageAn()
        # Quita barra de maximisar minimizar y cerrar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Quita Widget_central
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.prin.pushButton_2.clicked.connect(lambda: self.Maximizar())

        def moveWindow(e):
            if self.isMaximized() == False:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        self.prin.widget_3.mouseMoveEvent = moveWindow
        self.prin.pushButton_4.clicked.connect(lambda: self.BinarioDecimal())
        self.prin.pushButton_6.clicked.connect(lambda: self.BinarioOctal())
        self.prin.pushButton_7.clicked.connect(lambda: self.BinAHexa())
        self.prin.pushButton_5.clicked.connect(lambda: self.DeciMBina())
        self.prin.pushButton_8.clicked.connect(lambda: self.DecIOctal())
        self.prin.pushButton_9.clicked.connect(lambda: self.DecIHexad())
        self.prin.pushButton_10.clicked.connect(lambda: self.OctalBin())
        self.prin.pushButton_11.clicked.connect(lambda: self.OctalDeCi())
        self.prin.pushButton_12.clicked.connect(lambda: self.OctalHexad())
        self.prin.pushButton_13.clicked.connect(lambda: self.HexaDBina())
        self.prin.pushButton_14.clicked.connect(lambda: self.HexaDOctal())
        self.prin.pushButton_15.clicked.connect(lambda: self.HexaDDecimal())
        self.show()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def Maximizar(self):
        if self.isMaximized():
            self.prin.pushButton_2.setStyleSheet(u"font: 57 20pt 'Marlett';")
            self.prin.pushButton_2.setText(
                QCoreApplication.translate("MainWindow", u"1", None))
            self.showNormal()
        else:
            self.prin.pushButton_2.setStyleSheet(u"font: 57 20pt 'Marlett';")
            self.prin.pushButton_2.setText(
                QCoreApplication.translate("MainWindow", u"2", None))
            self.showMaximized()

    def BinarioDecimal(self):
        self.MensaD.AnimacionBenta()
        self.dato = self.prin.lineEdit.text()
        resul = str(BinDec(self.dato))
        self.MensaD.TituLO("Binario a Decimal", self.dato, resul)
        self.MensaD.show()

    def BinarioOctal(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        self.MensaD.TituLO("Binario a Octal", cadena, BinOct(cadena))
        self.MensaD.show()

    def BinAHexa(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        resul = BinHexa(cadena)
        self.MensaD.TituLO("Binario a Hexadecimal", cadena, resul)
        self.MensaD.show()

    def DeciMBina(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        resul = DeciBin(cadena)
        self.MensaD.TituLO("Decimal a Binario", cadena, resul)
        self.MensaD.show()

    def DecIOctal(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        resul = DecOct(cadena)
        self.MensaD.TituLO("Decimal a Octal", cadena, resul)
        self.MensaD.show()

    def DecIHexad(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        resul = DecHexa(cadena)
        self.MensaD.TituLO("Decimal a Hexadecimal", cadena, resul)
        self.MensaD.show()

    def OctalBin(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        resul = OctBin(cadena)
        self.MensaD.TituLO("Octal a Binario", cadena, resul)
        self.MensaD.show()

    def OctalDeCi(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        resul = OctDeci(cadena)
        self.MensaD.TituLO("Octal a Decimal", cadena, resul)
        self.MensaD.show()

    def OctalHexad(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        resul = OctHexa(cadena)
        self.MensaD.TituLO("Octal a Hexadecimal", cadena, resul)
        self.MensaD.show()

    def HexaDBina(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        resul = HexaBin(cadena)
        self.MensaD.TituLO("Hexadecmal a Binario", cadena, resul)
        self.MensaD.show()

    def HexaDOctal(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        resul = HexaOct(cadena)
        self.MensaD.TituLO("Hexadecmal a Octal", cadena, resul)
        self.MensaD.show()

    def HexaDDecimal(self):
        self.MensaD.AnimacionBenta()
        cadena = self.prin.lineEdit.text()
        resul = HexaDeci(cadena)
        self.MensaD.TituLO("Hexadecmal a Decimal", cadena, resul)
        self.MensaD.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    sys.exit(app.exec())
