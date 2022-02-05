class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
        print("Novo limite definido: {}".format(self.__limite))

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor
        print("Valor depositado: {}".format(valor))
        print("Valor total: {}".format(self.__saldo))

    def __checar_sacar(self, valor):
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor <= valor_disponivel_saque

    def sacar(self, valor):
        if self.__checar_sacar(valor):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)
        print("Valor transferido: {}".format(valor))
