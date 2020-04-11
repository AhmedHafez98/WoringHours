import sys
from PyQt5.Qt import QCommandLinkButton,QAction,QApplication,QWidget,QHBoxLayout,Qt
from PyQt5.QtWidgets import QMenu
from Designs import Widbu
class mywid(QWidget,Widbu.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Button(QCommandLinkButton):
    def __init__(self, name, parent = None):
        super(Button, self).__init__(name)
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.addMenuActions();
        self.setMaximumHeight(45)
        self.setStatusTip('Right Click to Edit')
        self.q=mywid()
    def addMenuActions(self):
        delete = QAction(self)
        delete.setText("Delete")
        delete.triggered.connect(self.removeButton)
        self.addAction(delete)
    def removeButton(self):
        self.q.deleteLater()
        self.deleteLater()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = QWidget()
    test.resize(250, 150)
    layout = QHBoxLayout()
    b=Button("Test Btn")
    menu = QMenu()
    menuItem1 = menu.addAction('Menu Item1')
    menuItem2 = menu.addAction('Menu Item2')
    b.setMenu(menu)
    layout.addWidget(b)
    test.setLayout(layout)
    test.show()
    app.exec_()