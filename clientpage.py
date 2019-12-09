# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clientpage.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(633, 397)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_add_client = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add_client.setGeometry(QtCore.QRect(90, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add_client.setFont(font)
        self.btn_add_client.setObjectName("btn_add_client")
        self.btn_modify = QtWidgets.QPushButton(self.centralwidget)
        self.btn_modify.setGeometry(QtCore.QRect(270, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_modify.setFont(font)
        self.btn_modify.setObjectName("btn_modify")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 10, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_done = QtWidgets.QPushButton(self.centralwidget)
        self.btn_done.setGeometry(QtCore.QRect(270, 310, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_done.setFont(font)
        self.btn_done.setObjectName("btn_done")
        self.filter_field = QtWidgets.QLineEdit(self.centralwidget)
        self.filter_field.setGeometry(QtCore.QRect(150, 310, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filter_field.setFont(font)
        self.filter_field.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.filter_field.setMaxLength(10)
        self.filter_field.setObjectName("filter_field")
        self.filter_label = QtWidgets.QLabel(self.centralwidget)
        self.filter_label.setGeometry(QtCore.QRect(80, 315, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filter_label.setFont(font)
        self.filter_label.setObjectName("filter_label")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(430, 60, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_delete.setFont(font)
        self.btn_delete.setObjectName("btn_delete")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(60, 110, 531, 181))
        self.listView.setObjectName("listView")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.btn_add_client.setText(_translate("mainWindow", "Add New Client"))
        self.btn_modify.setText(_translate("mainWindow", "Modify Client"))
        self.label.setText(_translate("mainWindow", "Client Management System"))
        self.btn_done.setText(_translate("mainWindow", "Done"))
        self.filter_field.setInputMask(_translate("mainWindow", "0000000009"))
        self.filter_field.setText(_translate("mainWindow", "0"))
        self.filter_label.setText(_translate("mainWindow", "Filter by:"))
        self.btn_delete.setText(_translate("mainWindow", "Delete Client"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
