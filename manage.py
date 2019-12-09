# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from accountpage import Ui_MainWindow
from clientpage import Ui_mainWindow
import classes as sc
import uuid
import re
import sys

class Controller(object):
    listBankCustomer = []
    listFilter = []
    test = 'yes'

    def __init__(self):
        self.clientPage = QtWidgets.QMainWindow()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self.clientPage)
        self.ui.btn_add_client.clicked.connect(self.openAccountPage)
        self.ui.btn_delete.clicked.connect(self.btnDeleteClicked)
#         self.ui.btn_delete.clicked.connect(self.ui.listView.clear)
#         self.ui.btn_delete.clicked.connect(self.reloadData)
        self.ui.btn_modify.clicked.connect(self.btnModifyClicked)
        self.ui.btn_done.clicked.connect(self.btnFilterClicked)
        self.reloadData()
        self.clientPage.show()

    def openAccountPage(self):
        self.classID = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow()
        self.ui2.setupUi(self.classID)
        self.ui2.btnDone.clicked.connect(self.btnAddClicked)
        self.classID.show()

    def addAccount(self):
        self.classID.close()

    def btnAddClicked(self):
        try:
            name = self.ui2.namefield.text()
            birth = self.ui2.dateEdit.date()
            birth = str(birth.toPyDate())
            id = self.ui2.account_id_field.text()
            account = self.ui2.accnumfield1.text()
            account2 = self.ui2.accnumfield2.text()
            balance = self.ui2.balancefield.text()

            if len(name) == 0:
                raise sc.MissingDataException('NAME')
            if len(account) == 0 or len(account2) == 0:
                raise sc.MissingDataException('ACCOUNT NUMBER')
            if len(balance) == 0:
                raise sc.MissingDataException('BALANCE')

            if len(id) == 8 and re.compile('[0-9a-zA-Z]{8}').match(id):
                True
            else:
                if len(id) == 0:
                    id = uuid.uuid4().hex[:8]
                else:
                    raise sc.FormatException('ID NUMBER')

            if len(account) != 8 or not re.compile('\d{8}').match(account):
                raise sc.FormatException('ACCOUNT NUMBER')

            if len(account2) != 8 or not re.compile('\d{8}').match(account2):
                raise sc.FormatException('ACCOUNT NUMBER')

        except sc.MissingDataException as mde:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(mde.__str__())
            msg.exec()

        except sc.FormatException as fe:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(fe.__str__())
            msg.exec()

        else:
            if self.test == 'yes':
                Customer = sc.BankCustomers(name.title(), birth, id, account, account2, balance)
                if Customer not in self.listBankCustomer:
                    self.listBankCustomer.append(Customer)
                    self.listBankCustomer.sort()
                    self.saveToFile()
                    msg = QtWidgets.QMessageBox()
                else:
                    msg.setWindowTitle('Warning!')
                    msg.setIcon(QtWidgets.QMessageBox.Warning)
                    msg.setText("This customer already exist")
                    msg.exec()
            else:
                for Customer in self.listBankCustomer:
                    if Customer.getID() == self.ui2.account_id_field.text():
                        self.listBankCustomer.remove(Customer)
                        customer = sc.BankCustomers(name.title(), birth, id, account, account2, balance)
                        self.listBankCustomer.append(customer)
                        self.listBankCustomer.sort()
                        self.saveToFile()
            self.classID.close()
            self.ui.listView.clear()
            self.reloadData()

    def btnDeleteClicked(self):
        if not self.ui.listView.currentItem():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You should select any person from the list!")
            msg.exec()
        else:
            item = self.ui.listView.currentItem()
            tmp = item.text()
            tmp = tmp.split('|')
            id = tmp[2].split(": ")
            id = id[1]
            for Customer in self.listBankCustomer:
                if id.strip() == Customer.getID():
                    self.listBankCustomer.remove(Customer)
                    self.saveToFile()
                    for Customer in self.listBankCustomer:
                        self.ui.listView.addItem(Customer.__str__())
        self.ui.listView.clear()
        self.reloadData()
        
    def btnModifyClicked(self):
        if not self.ui.listView.currentItem():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Warning!")
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText("You should select any person from the list!")
            msg.exec()
        else:
            self.openAccountPage()
            item = self.ui.listView.currentItem()
            tmp = item.text()
            tmp = tmp.split('|')
            id = tmp[2].split(": ")
            id = id[1]
            for Customer in self.listBankCustomer:
                if id.strip() == Customer.getID():
                    self.ui2.namefield.setText(Customer.getName())
                    new = Customer.getBirthday().split('-')
                    # print(new)
                    self.ui2.dateEdit.setDate(QtCore.QDate(int(new[0]), int(new[1]), int(new[2])))
                    self.ui2.account_id_field.setText(Customer.getID())
                    self.ui2.accnumfield1.setText(Customer.getAccount())
                    self.ui2.accnumfield2.setText(Customer.getAccount2())
                    self.ui2.balancefield.setText(Customer.getBalance())
                    self.test = 'no'

    def btnFilterClicked(self):
        try:
            filter = self.ui.filter_field.text()
            if len(str(filter)) == 0:
                raise sc.MissingDataException('Filter By')
            else:
                filter = int(filter)
        except sc.MissingDataException as mde:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText(mde.__str__())
            msg.exec()
        else:
            self.ui.listView.clear()
            for Customer in self.listBankCustomer:
                if filter <= int(Customer.getBalance()):
                    self.ui.listView.addItem(Customer.__str__())
            self.ui.filter_field.clear()

    def saveToFile(self):
        outFile = open("database.txt", "w")
        for Customer in self.listBankCustomer:
            print('{};{};{};{};{};{}\n'.format(Customer.getName(), Customer.getBirthday(), Customer.getID(), Customer.getAccount(), Customer.getAccount2(), Customer.getBalance()),
                  file=outFile)
        outFile.close()

    def reloadData(self):
        duplicate = []
        inFile = open("database.txt", "r")
        for line in inFile:
            if line.count(";") == 5:
                tmp = line.split(';')
                example = sc.BankCustomers(tmp[0].title(), tmp[1], tmp[2], tmp[3], tmp[4], tmp[5][:-1])
                if example not in self.listBankCustomer:
                    self.listBankCustomer.append(example)
        inFile.close()
        self.listBankCustomer.sort()
        for Customer in self.listBankCustomer:
            if Customer.__str__() not in duplicate:
                duplicate.append(Customer.__str__())
                self.ui.listView.addItem(Customer.__str__())



app = QtWidgets.QApplication(sys.argv)
cntrl = Controller()
sys.exit(app.exec_())
