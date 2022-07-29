# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledEHvdor.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MensD(object):
    def setupUi(self, MensD):
        if not MensD.objectName():
            MensD.setObjectName(u"MensD")
        MensD.resize(566, 176)
        MensD.setMaximumSize(QSize(16777215, 16777215))
        MensD.setStyleSheet(u"QWidget#widget_Pading{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.585, y2:0.66, stop:0.505682 rgba(0, 248, 255, 255), stop:1 rgba(0, 0, 0, 0));\n"
"}\n"
"QWidget#widget{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.943191, y2:0.984, stop:0.685393 rgba(30, 30, 40, 250), stop:1 rgba(0, 0, 0, 210));	\n"
"}\n"
"QWidget#widget_2{\n"
"	background-color:qlineargradient(spread:pad, x1:0.40713, y1:0.511, x2:1, y2:1, stop:0 rgba(30,30,40, 237), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"/* Botones */\n"
"QPushButton{\n"
"	background-color: rgb(30,30,30);\n"
"	border:1px solid rgb(255,255,255);\n"
"	border-radius:4px;\n"
"	color:rgba(255,255,255,0.9);\n"
"	padding:4px;\n"
"}\n"
"QPushButton:hover{\n"
"	font: 57 15pt \"Marlett\";\n"
"	background-color: rgba(30,30,30,0.8);\n"
"	border:1px solid rgb(255,255,255);\n"
"	border-radius:4px;\n"
"	color:rgba(255,255,255,0.7);\n"
"	padding:2px;\n"
"}\n"
"QPushButton:pressed{\n"
"	font: 57 13pt \"Marlett\";\n"
"	background-color: rgb(3"
                        "0,30,30);\n"
"	border:1px solid rgb(255,255,255);\n"
"	border-radius:4px;\n"
"	color:#ffffff;\n"
"	padding:30px;\n"
"}\n"
"QPushButton#Cerrar:hover{\n"
"	font: 57 15pt \"Marlett\";\n"
"	background-color:rgba(255,0,0,0.8);\n"
"	border: 1px solid rgb(255,255,255);\n"
"	border-radius:4px;\n"
"	color:rgba(255,255,255,0.74);\n"
"	padding:2px;\n"
"}\n"
"QPushButton#Cerrar:pressed{\n"
"	font: 57 10pt \"Marlett\";\n"
"	background-color:rgba(255,0,0,1);\n"
"	border: 1px solid rgb(255,255,255);\n"
"	border-radius:4px;\n"
"	color:#ffffff;\n"
"	padding:2px;\n"
"}\n"
"QLineEdit{\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(255,255,255);\n"
"	border-radius: 2px;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"/*   Modificacion de los labes*/\n"
"QLabel{\n"
"	background: transparent;\n"
"	color:#ffffff;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.gridLayout = QGridLayout(MensD)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_Pading = QWidget(MensD)
        self.widget_Pading.setObjectName(u"widget_Pading")
        self.widget_Pading.setEnabled(True)
        self.gridLayout_2 = QGridLayout(self.widget_Pading)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.widget = QWidget(self.widget_Pading)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_3)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy)
        self.gridLayout_3 = QGridLayout(self.widget_5)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Tema = QLabel(self.widget_5)
        self.Tema.setObjectName(u"Tema")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.Tema.setFont(font)

        self.gridLayout_3.addWidget(self.Tema, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.Minimizar = QPushButton(self.widget_4)
        self.Minimizar.setObjectName(u"Minimizar")
        font1 = QFont()
        font1.setFamilies([u"Marlett"])
        font1.setPointSize(17)
        self.Minimizar.setFont(font1)

        self.horizontalLayout_2.addWidget(self.Minimizar)

        self.Cerrar = QPushButton(self.widget_4)
        self.Cerrar.setObjectName(u"Cerrar")
        self.Cerrar.setFont(font1)

        self.horizontalLayout_2.addWidget(self.Cerrar)


        self.horizontalLayout.addWidget(self.widget_4, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.widget_3, 0, Qt.AlignTop)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy1)
        self.gridLayout_4 = QGridLayout(self.widget_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.Contenido = QLabel(self.widget_2)
        self.Contenido.setObjectName(u"Contenido")

        self.gridLayout_4.addWidget(self.Contenido, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_Pading, 0, 0, 1, 1)


        self.retranslateUi(MensD)
        self.Minimizar.clicked.connect(MensD.showMinimized)
        self.Cerrar.clicked.connect(MensD.close)

        QMetaObject.connectSlotsByName(MensD)
    # setupUi

    def retranslateUi(self, MensD):
        MensD.setWindowTitle(QCoreApplication.translate("MensD", u"Form", None))
        self.Tema.setText(QCoreApplication.translate("MensD", u"Tema", None))
        self.Minimizar.setText(QCoreApplication.translate("MensD", u"0", None))
        self.Cerrar.setText(QCoreApplication.translate("MensD", u"r", None))
        self.Contenido.setText(QCoreApplication.translate("MensD", u"Contenido", None))
    # retranslateUi

