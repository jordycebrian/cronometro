# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cronometro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(318, 268)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-20, 0, 361, 241))
        self.widget.setStyleSheet(u"QObject{\n"
"	background-color: #090d09;\n"
"}")
        self.lblcrono = QLabel(self.widget)
        self.lblcrono.setObjectName(u"lblcrono")
        self.lblcrono.setGeometry(QRect(50, 50, 231, 71))
        self.lblcrono.setStyleSheet(u"QObject{\n"
"	font: 75 56pt \"Arial\";\n"
"	color: white;\n"
"}	\n"
"\n"
"")
        self.btnstart = QPushButton(self.widget)
        self.btnstart.setObjectName(u"btnstart")
        self.btnstart.setGeometry(QRect(40, 160, 75, 23))
        self.btnstart.setStyleSheet(u"QObject{\n"
"	background-color: white;\n"
"	border: 2px solid #ccc;\n"
"	color: black;\n"
"	font: 75 12pt \"Arial\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnstop = QPushButton(self.widget)
        self.btnstop.setObjectName(u"btnstop")
        self.btnstop.setGeometry(QRect(240, 160, 75, 23))
        self.btnstop.setStyleSheet(u"QObject{\n"
"	background-color: white;\n"
"	border: 2px solid #ccc;\n"
"	color: black;\n"
"	font: 75 12pt \"Arial\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        self.btnreset = QPushButton(self.widget)
        self.btnreset.setObjectName(u"btnreset")
        self.btnreset.setGeometry(QRect(140, 160, 75, 23))
        self.btnreset.setStyleSheet(u"QObject{\n"
"	background-color: white;\n"
"	border: 2px solid #ccc;\n"
"	color: black;\n"
"	font: 75 12pt \"Arial\";\n"
"}\n"
"QObject:hover{\n"
"	background-color: #ccc;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 318, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cronometro", None))
        self.lblcrono.setText(QCoreApplication.translate("MainWindow", u"0.0", None))
        self.btnstart.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btnstop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btnreset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
    # retranslateUi

