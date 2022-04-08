class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular.title()
        self.__saldo = saldo
        self.__limite = limite
        print(f'Objeto criado: {self}')

    def extrato(self):
        print(f"Saldo atual de {self.__titular}: {self.__saldo}")

    def deposita(self, valor):
        self.__valida_valor(valor)
        if (valor > 0):
            self.__saldo += valor
            self.extrato()
        else:
            print(f'O valor {valor} é inválido para depósito.')

    def saca(self, valor):
        self.__valida_valor(valor)
        if (self.__saldo >= valor and valor > 0):
            self.__saldo -= valor
            self.extrato()
        else:
            print(f'O valor {valor} é inválido para saque.')

    def transfere(self, destinatario, valor):
        self.saca(valor)
        destinatario.deposita(valor)

    def __valida_valor(self, valor):
        try:
            val = int(valor)
        except ValueError:
            print(f'o valor {valor} é inválido')
            raise

