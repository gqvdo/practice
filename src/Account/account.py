class Account:

    def __init__(self, number, holder, balance, limit):
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    @staticmethod
    def bank_code():
        return "001"

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, new_limit):
        self.__limit = new_limit
        print("New limit set: {}".format(self.__limit))

    def extract(self):
        print("Balance {} / Holder {}".format(self.__balance, self.__holder))

    def deposit(self, amount):
        self.__balance += amount
        print("Deposited amount: {}".format(amount))
        print("Amount: {}".format(self.__balance))

    def __check_withdraw(self, amount):
        amount_avaiable_withdraw = self.__balance + self.__limit
        return amount <= amount_avaiable_withdraw

    def withdraw(self, amount):
        if self.__check_withdraw(amount):
            self.__balance -= amount
        else:
            print("The amount {} is above the limit".format(amount))

    def transfer(self, amount, destine):
        self.withdraw(amount)
        destine.depositar(amount)
        print("Amount transfered: {}".format(amount))
