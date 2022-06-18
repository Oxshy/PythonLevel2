from PyQt5.QtWidgets import *#QApplication, QMainWindow, QPushButton, QLables
from PyQt5.QtGui import *
from PyQt5.QtCore import *#Qt, QTime
import sys

class StopWatchWindow(QMainWindow):
    def __init__(self):
       super().__init__()
       self.setWindowTitle("STOP WATCH")
       self.setGeometry(600,600,500,500)
       self.UIcomponents()
    def UIcomponents(self):
        self.count=0
        self.flag=False
        self.label=QLabel(self)
        self.label.setGeometry(115,100,250,70)
        self.label.setStyleSheet("border:4px solid black")
        self.label.setFont(QFont("arial",16))
        self.label.setAlignment(Qt.AlignCenter)

        start=QPushButton("start",self)
        start.setGeometry(105,175,270,50)
        start.pressed.connect(self.startfun)

        pause=QPushButton("pause",self)
        pause.setGeometry(105,225,270,50)
        pause.pressed.connect(self.pausefun)

        reset=QPushButton("reset",self)
        reset.setGeometry(105,275,270,50)
        reset.pressed.connect(self.resetfun)
        

        timer=QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(100)

    def startfun(self):
        print("pressing the start button")
        self.flag=True
    def pausefun(self):
        print("pressing pause button")
        self.flag=False
    def resetfun(self):
        print("pressing reset button")
        self.count=0
        self.flag=False
    def showtime(self):
        if self.flag:
            self.count+=1
        print(self.count)
        self.label.setText(str(self.count/10))



app=QApplication(sys.argv)
win=StopWatchWindow()
win.show()
exit(app.exec_())