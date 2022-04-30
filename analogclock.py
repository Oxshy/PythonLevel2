from PyQt5.QtWidgets import *#QApplication, QMainWindow
from PyQt5.QtGui import *#QPainter, QBrush, QPen 
from PyQt5.QtCore import *#Qt, QTime
import sys

class Clock(QMainWindow):
    def __init__(self):
        super().__init__()
        timer=QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)
        self.setWindowTitle("Clock")
        self.setGeometry(600,600,500,500)
        self.setStyleSheet("background:black")

        self.hpointer=QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-50)])
        self.mpointer=QPolygon([QPoint(6,7),QPoint(-6,7),QPoint(0,-70)])
        self.spointer=QPolygon([QPoint(2,2),QPoint(-2,2),QPoint(0,-90)])
        self.bcolour=Qt.green
        self.scolour=Qt.red



    def paintEvent(self,event):
        painter=QPainter(self)
        # painter.setPen(QPen(Qt.white,5,Qt.SolidLine))
        # painter.setBrush(QBrush(Qt.red,Qt.SolidPattern))
        # painter.drawRect(10,10,100,100)
        tick=QTime.currentTime()
        print(tick.hour(),tick.minute(),tick.second())
        def pdraw(colour,rotation,pointer):
            painter.setBrush(QBrush(colour))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()
        painter.translate(self.width()/2,self.height()/2)
        # pdraw(self.bcolour,90,self.hpointer)
        # pdraw(self.bcolour,90,self.mpointer)
        # pdraw(self.scolour,90,self.spointer)
        pdraw(self.bcolour,(30*(tick.hour()+tick.minute()/60)),self.hpointer)
        pdraw(self.bcolour,(6*(tick.minute()+tick.second()/60)),self.mpointer)
        pdraw(self.scolour,(6*tick.second()),self.spointer)

        painter.setPen(QPen(Qt.white))
        for i in range(0,60):
            if i%5==0:
                painter.drawLine(87,0,97,0)
            painter.rotate(6)
        painter.end()


app=QApplication(sys.argv)
print(sys.argv)
win=Clock()
win.show()
exit(app.exec_())