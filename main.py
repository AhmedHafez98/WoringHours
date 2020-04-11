import sys
import qdarkstyle
from PyQt5.QtWidgets import QApplication,QMainWindow,QVBoxLayout,QWidget
from PyQt5.uic import loadUiType
from Designs.WidButton import Button
from Designs import Home,WidButton


class Main(QMainWindow,Home.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addwid.returnPressed.connect(self.Enterpressed)
        self.vbox = QVBoxLayout()
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        self.frame.tabBar().hide()
        self.bhome.clicked.connect(self.homebuttonclicked)
    def homebuttonclicked(self):
        self.frame.setCurrentIndex(0)
    def Enterpressed(self):
        if self.addwid.text()=='':return
        b=Button(self.addwid.text())
        self.vbox.addLayout(b)
        self.frame.addTab(b.b.q,self.addwid.text())
        self.frame.setCurrentWidget(b.b.q)
        b.b.clicked.connect(lambda :self.frame.setCurrentWidget(b.b.q))
        self.verticalLayout_4.addLayout(self.vbox)
        self.addwid.setText('')
if __name__=='__main__':
    app=QApplication(sys.argv)
    win=Main()
    win.show()
    sys.exit(app.exec_())