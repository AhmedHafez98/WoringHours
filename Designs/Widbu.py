# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designs/Widbu.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(470, 365)
        Form.setMinimumSize(QtCore.QSize(470, 0))
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_summary = QtWidgets.QWidget()
        self.tab_summary.setObjectName("tab_summary")
        self.tabWidget.addTab(self.tab_summary, "")
        self.tab_todo = QtWidgets.QWidget()
        self.tab_todo.setObjectName("tab_todo")
        self.tabWidget.addTab(self.tab_todo, "")
        self.tab_notes = QtWidgets.QWidget()
        self.tab_notes.setObjectName("tab_notes")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_notes)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.noteverticalLayout_4 = QtWidgets.QVBoxLayout()
        self.noteverticalLayout_4.setObjectName("noteverticalLayout_4")
        self.notehorizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.notehorizontalLayout_2.setObjectName("notehorizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.notehorizontalLayout_2.addItem(spacerItem)
        self.notelineEdit = QtWidgets.QLineEdit(self.tab_notes)
        self.notelineEdit.setEnabled(True)
        self.notelineEdit.setMinimumSize(QtCore.QSize(150, 0))
        self.notelineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.notelineEdit.setObjectName("notelineEdit")
        self.notehorizontalLayout_2.addWidget(self.notelineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.notehorizontalLayout_2.addItem(spacerItem1)
        self.noteverticalLayout_4.addLayout(self.notehorizontalLayout_2)
        self.notehorizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.notehorizontalLayout_3.setObjectName("notehorizontalLayout_3")
        self.notetextEdit = QtWidgets.QTextEdit(self.tab_notes)
        self.notetextEdit.setMaximumSize(QtCore.QSize(16777215, 450))
        self.notetextEdit.setObjectName("notetextEdit")
        self.notehorizontalLayout_3.addWidget(self.notetextEdit)
        self.noteverticalLayout_4.addLayout(self.notehorizontalLayout_3)
        self.notescrollArea = QtWidgets.QScrollArea(self.tab_notes)
        self.notescrollArea.setWidgetResizable(True)
        self.notescrollArea.setObjectName("notescrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 424, 69))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.noteoutgridLayout = QtWidgets.QGridLayout()
        self.noteoutgridLayout.setObjectName("noteoutgridLayout")
        self.gridLayout_2.addLayout(self.noteoutgridLayout, 0, 0, 1, 1)
        self.notescrollArea.setWidget(self.scrollAreaWidgetContents)
        self.noteverticalLayout_4.addWidget(self.notescrollArea)
        self.notehorizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.notehorizontalLayout_4.setObjectName("notehorizontalLayout_4")
        self.noteverticalLayout_4.addLayout(self.notehorizontalLayout_4)
        self.verticalLayout_5.addLayout(self.noteverticalLayout_4)
        self.tabWidget.addTab(self.tab_notes, "")
        self.horizontalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        self.notelineEdit.textChanged['QString'].connect(self.notetextEdit.hide)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.notelineEdit, self.notetextEdit)
        Form.setTabOrder(self.notetextEdit, self.tabWidget)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_summary), _translate("Form", "Summary"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_todo), _translate("Form", "ToDo"))
        self.notelineEdit.setToolTip(_translate("Form", "<html><head/><body><p>Press <span style=\" font-weight:600; color:#ff0000;\">Enter</span> To Add</p></body></html>"))
        self.notelineEdit.setStatusTip(_translate("Form", "Press Enter To Add Note"))
        self.notelineEdit.setPlaceholderText(_translate("Form", "Add New Note"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_notes), _translate("Form", "Notes"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
