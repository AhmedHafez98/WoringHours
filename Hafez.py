import sys
from PyQt5.Qt import QCommandLinkButton,QAction,QApplication,QWidget,QHBoxLayout,QLineEdit,Qt

from PyQt5 import QtCore
from Designs import Widbu


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = QWidget()
    test.resize(250, 150)
    ui=Widbu.Ui_Form()
    ui.setupUi(test)
    test.show()
    app.exec_()