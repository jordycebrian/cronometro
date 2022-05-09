from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot, QTimer
from ui_cronometro import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnstart.clicked.connect(self.Start)
        self.ui.btnstop.clicked.connect(self.stopTime)
        self.ui.btnreset.clicked.connect(self.resetTime)
        self.cont=0
        self.flag = False
        self.timer = QTimer(self) 
        self.timer.timeout.connect(self.showTime) 
        self.timer.start(100)

    @Slot()
    def Start(self):
        self.flag = True

    @Slot()
    def showTime(self):
        if self.flag:
            self.cont+=1
        text = str(self.cont/10)
        self.ui.lblcrono.setText(text)

    @Slot()
    def stopTime(self):
        self.flag=False

    @Slot()
    def resetTime(self):
        self.flag = False
        self.cont = 0
