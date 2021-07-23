from class_calc import *
import os

def main():
    while True:
        try:
            calculadora = Calc()
            calculadora.menu()
            operação = int(input('Informe a operação: '))
            numero1 = int(input('Informe um número: '))
            numero2 = int(input('Informe um número: '))
            calculadora.execução(operação, numero1, numero2)
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
