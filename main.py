import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QWidget,QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.Qt import *
import Designs.GUI
import qdarkstyle


class Main(QMainWindow,Designs.GUI.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit_2.returnPressed.connect(self.fu)
        self.btns=list()
        self.vbox=QVBoxLayout()
        self.tabWidget.tabBar().hide()
        self.bdel.clicked.connect(self.fun)
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    def fu(self):
        try:
           nbtb=QCommandLinkButton(self.lineEdit_2.text())
        except Exception as ex:print(ex)
        self.vbox.addWidget(nbtb)
        self.verticalLayout_4.addLayout(self.vbox)
        nbtb.setMaximumHeight(50)
    def fun(self):
        self.vbox.itemAt(0).widget().deleteLater()





if __name__=='__main__':
    app=QApplication(sys.argv)
    win=Main()
    win.show()
    sys.exit(app.exec_())

