from class_calc import *
import os

def main():
    while True:
        try:
            numero1 = int(input('Informe o primeiro número: '))
            numero2 = int(input('Informe o segundo número: '))
            calculadora = Calc(numero1, numero2)
            calculadora.menu()
            operação = int(input('Informe a operação: '))
            calculadora.execução(operação)
            continuar = ' '
            while continuar not in 'SsNn':
                continuar = input('\nDeseja continuar? [S/N]\n').upper()[0]
                if continuar not in 'SsNn':
                    print('Informe uma entrada válida.')
            if continuar == 'N':
                break
            else:
                os.system('cls')
        except IndexError:
            print('Informe uma operação existente.')
        except ValueError:
            print('Informe apenas valores numéricos.')

if __name__ == '__main__':
    main()
