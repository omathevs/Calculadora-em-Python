import sys

opções = (None, 'Adição', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação', 'Sair')

class Calc:

    def __init__(self, valor1, valor2):
        self.opção = 0
        self.valor1 = valor1
        self.valor2 = valor2

    def somar(self, valor1, valor2):
        total = self.valor1 + self.valor2
        return f'{self.valor1} + {self.valor2} = {total}'

    def subtrair(self, valor1, valor2):
        diferença = self.valor1 - self.valor2
        return f'{self.valor1} - {self.valor2} = {diferença}'

    def multiplicar(self, valor1, valor2):
        produto = self.valor1 * self.valor2
        return f'{self.valor1} x {self.valor2} = {produto}'

    def dividir(self, valor1, valor2):
        quociente = self.valor1 / self.valor2
        return f'{self.valor1} ÷ {self.valor2} = {quociente}'

    def potenciar(self, valor1, valor2):
        potencia = self.valor1 ** self.valor2
        return f'{self.valor1} ^ {self.valor2} = {potencia}'

    def menu(self):
        print('''
[1] Adição
[2] Subtração
[3] Multiplicação
[4] Divisão
[5] Potenciação
[6] Sair
        ''')

    def execução(self, opção):
        self.opção = opção

        if opções[self.opção] and self.opção == 6:
            sys.exit()
        if opções[self.opção] and self.opção == 1:
            print(self.somar(self.valor1, self.valor2))
        elif opções[self.opção] and self.opção == 2:
            print(self.subtrair(self.valor1, self.valor2))
        elif opções[self.opção] and self.opção == 3:
            print(self.multiplicar(self.valor1, self.valor2))
        elif opções[self.opção] and self.opção == 4:
            print(self.dividir(self.valor1, self.valor2))
        elif opções[self.opção] and self.opção == 5:
            print(self.potenciar(self.valor1, self.valor2))
        