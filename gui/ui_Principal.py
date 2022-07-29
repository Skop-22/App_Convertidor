# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PrincipalZbzXjN.ui'
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
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(585, 249)
        MainWindow.setStyleSheet(u"QWidget#widget_Pading{\n"
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
"	font: 57 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgba(30,30,30,0.8);\n"
"	border:1px solid rgb(255,255,255);\n"
"	border-radius:4px;\n"
"	color:rgba(255,255,255,0.7);\n"
"	padding:2px;\n"
"}\n"
"QPushButton:pressed{\n"
"	font: 57 9pt \"MS Shell Dlg 2\";\n"
"	background"
                        "-color: rgb(30,30,30);\n"
"	border:1px solid rgb(255,255,255);\n"
"	border-radius:4px;\n"
"	color:#ffffff;\n"
"	padding:30px;\n"
"}\n"
"QPushButton#pushButton:hover,#pushButton_2:hover,#pushButton_3:hover{\n"
"	font: 57 15pt \"Marlett\";\n"
"	background-color:rgba(255,0,0,0.8);\n"
"	border: 1px solid rgb(255,255,255);\n"
"	border-radius:4px;\n"
"	color:rgba(255,255,255,0.74);\n"
"	padding:2px;\n"
"}\n"
"QPushButton#pushButton:pressed,#pushButton_2:pressed,#pushButton_3:pressed{\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_Pading = QWidget(self.centralwidget)
        self.widget_Pading.setObjectName(u"widget_Pading")
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
        self.label = QLabel(self.widget_5)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"MS Shell Dlg 2"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_5)

        self.widget_4 = QWidget(self.widget_3)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.pushButton_3 = QPushButton(self.widget_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font1 = QFont()
        font1.setFamilies([u"Marlett"])
        font1.setPointSize(17)
        self.pushButton_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.widget_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.widget_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pushButton)


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
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_13 = QPushButton(self.widget_2)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout_4.addWidget(self.pushButton_13, 4, 0, 1, 1)

        self.lineEdit = QLineEdit(self.widget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_4.addWidget(self.lineEdit, 0, 1, 1, 2)

        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_4.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.widget_2)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout_4.addWidget(self.pushButton_14, 4, 1, 1, 1)

        self.label_3 = QLabel(self.widget_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.widget_2)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_4.addWidget(self.pushButton_11, 3, 1, 1, 1)

        self.pushButton_15 = QPushButton(self.widget_2)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout_4.addWidget(self.pushButton_15, 4, 2, 1, 1)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_4.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_10 = QPushButton(self.widget_2)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout_4.addWidget(self.pushButton_10, 3, 0, 1, 1)

        self.pushButton_12 = QPushButton(self.widget_2)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.gridLayout_4.addWidget(self.pushButton_12, 3, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.gridLayout_4.addWidget(self.pushButton_8, 2, 1, 1, 1)

        self.pushButton_9 = QPushButton(self.widget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout_4.addWidget(self.pushButton_9, 2, 2, 1, 1)

        self.pushButton_5 = QPushButton(self.widget_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_4.addWidget(self.pushButton_5, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_4.addWidget(self.pushButton_4, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_2)


        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_Pading, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.close)
        self.pushButton_3.clicked.connect(MainWindow.showMinimized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Aplicaci\u00f3n de conversi\u00f3n", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"r", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Hexadecimal a Binario", None))
        self.lineEdit.setPlaceholderText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Binario a Hexadecimal", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Hexadecimal a Octal", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Entrada de Datos", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Octal a Decimal", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Hexadecimal a Decimal", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Binario a Octal", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Octal a Binario", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Octal a Hexadecimal", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Decimal a Octal", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Decimal a Hexadecimal", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Decimal a Binario", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Binario a Decimal", None))
    # retranslateUi

