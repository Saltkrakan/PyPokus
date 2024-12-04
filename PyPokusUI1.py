# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyPokus1VRHKUB.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6 import QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(302, 155)
        self.actionClick = QAction(MainWindow)
        self.actionClick.setObjectName(u"actionClick")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 10, 75, 24))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 40, 113, 22))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 70, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 302, 22))
        self.menuApp = QMenu(self.menubar)
        self.menuApp.setObjectName(u"menuApp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuApp.menuAction())
        self.menuApp.addAction(self.actionClick)
        self.menuApp.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        #Definice akcí
        #=============
        self.actionExit.triggered.connect(app.exit)

        self.actionClick.triggered.connect(self.actionClickTriggered)

        self.pushButton.clicked.connect(self.pushButtonClicked)

       
        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionClick.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Click", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.menuApp.setTitle(QCoreApplication.translate("MainWindow", u"App", None))
    # retranslateUi



#Inicializace hlavního okna
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow): 
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #Definice funkcí
    #===============
    def pushButtonClicked (self):
        self.label.setMinimumWidth(100)
        self.label.setText("Stlačeno Click")

    def actionClickTriggered (self):
        self.label.setMinimumWidth(100)
        self.label.setText("Stlačeno Menu 1")
     

app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
