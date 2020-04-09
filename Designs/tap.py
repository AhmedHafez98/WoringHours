# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Designs/tap.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 421)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 481, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(60, 140, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 120, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 100, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Tab 1"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tab 2"))
        self.pushButton_3.setText(_translate("Form", "PushButton"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Page"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
