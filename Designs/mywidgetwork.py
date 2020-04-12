from PyQt5.Qt import QWidget,QGridLayout
from PyQt5.uic import loadUiType
from Designs.Widbu import Ui_Form
from Designs.Note import Button
class mywid(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #   Notes
        self.row=0
        self.col=0
        self.notelineEdit.returnPressed.connect(self.Enterpressed)
    #   Notes
    def Enterpressed(self):
        if self.notelineEdit.text()=='':return
        b=Button(self.notelineEdit.text())
        self.noteoutgridLayout.addLayout(b,self.row,self.col)
        self.col+=1
        if self.col==6:
            self.col=0
            self.row+=1
        b.b.clicked.connect(self.noteclickedevet)
        self.notelineEdit.setText('')
    def noteclickedevet(self):
        self.notetextEdit.show()
        self.notetextEdit.setFocus()


