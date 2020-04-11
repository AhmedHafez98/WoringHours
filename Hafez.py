import sys
from PyQt5.Qt import QCommandLinkButton,QAction,QApplication,QWidget,QHBoxLayout,QLineEdit,Qt

from PyQt5.QtWidgets import QMenu
from Designs import Widbu
class mywid(QWidget,Widbu.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class pushButton(QCommandLinkButton):
    def __init__(self, name, parent = None):
        super().__init__(name)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.addMenuActions();
        self.setMaximumHeight(45)
        self.setStatusTip('Right Click to Edit')
        self.q=mywid()
        self.par=parent
    def addMenuActions(self):
        delete = QAction(self)
        delete.setText("Delete")
        delete.triggered.connect(self.removeButton)
        rename=QAction(self)
        rename.setText('Rename')
        rename.triggered.connect(self.renameButton)
        self.addAction(rename)
        self.addAction(delete)
    def removeButton(self):
        self.q.deleteLater()
        self.deleteLater()
    def renameButton(self):
        self.hide()
        self.par.show()
        self.par.setFocus()


class line(QLineEdit):
    def __init__(self):
        QLineEdit.__init__(self)
        self.setMaximumHeight(45)
        self.setStatusTip('To Finish Press Enter')
        self.par=QCommandLinkButton()
        self.returnPressed.connect(self.EnterPressed)
    def pushpar(self,But):
        self.par=But
        self.setText(But.text())
        self.setSelection(0,len(self.text()))
        self.setPlaceholderText('Enter New Name')

    def EnterPressed(self):
        self.hide()
        self.par.setText(self.text())
        self.par.show()
class Button(QHBoxLayout):
    def __init__(self,name):
        QHBoxLayout.__init__(self)
        self.t=line()
        self.t.hide()
        self.b=pushButton(name,self.t)
        self.t.pushpar(self.b)
        self.addWidget(self.t)
        self.addWidget(self.b)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = QWidget()
    test.resize(250, 150)
    layout = Button('hafez')
    test.setLayout(layout)
    test.show()
    app.exec_()