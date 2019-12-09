class FormatException(Exception):
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return "The " + self.__value + " format is incorrect"


class MissingDataException(Exception):
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return "The " + self.__value + " text box is empty. You should provide this mandatory data!"

class BankCustomers:

    def __init__(self, name, birthday, id, account, account2, balance):
        self.__name = name
        self.__birthday = birthday
        self.__id = id
        self.__account = account
        self.__account2 = account2
        self.__balance = balance

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setBirthday(self, birthdate):
        self.__birthday = birthdate

    def getBirthday(self):
        return self.__birthday

    def getID(self):
        return self.__id

    def setAccount(self, account):
        self.__account = account

    def getAccount(self):
        return self.__account

    def setAccount2(self, account):
        self.__account2 = account2

    def getAccount2(self):
        return self.__account2

    def setBalance(self, balance):
        self.__balance = balance

    def getBalance(self):
        return self.__balance

    def __str__(self):
        return "NAME: " + self.__name + " | DATE OF BIRTH: " + self.__birthday + " | ID: " + self.__id + " | BALANCE: " + self.__balance

    def __le__(self, other):
        if self.getName() == other.getName():
            if self.getBirthday() == other.getBirthday():
                return self.getID() < other.getID()
            else:
                return self.getBirthday() < other.getBirthday()
        else:
            return self.getName() < other.getName()

    def __gt__(self, other):
        return self.getName() > other.getName()

    def __eq__(self, other):
        return self.getID() == other.getID()
