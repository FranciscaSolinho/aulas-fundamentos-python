#num1=int(input('Digite o 1º número:'))
#num2=int(input('Digite o 2º número:'))
#num3=int(input('Digite o 3º número:'))
from time import sleep

opcao=''

while opcao!=5:
    num1 = int(input('Digite o 1º número:'))
    num2 = int(input('Digite o 2º número:'))
    num3 = int(input('Digite o 3º número:'))
    opcao=''

    while opcao != 4:
        print('---- MENU ----')
        sleep(0.5)
        print('[ 1 ] - Somar')
        sleep(0.3)
        print('[ 2 ] - Multiplicar')
        sleep(0.3)
        print('[ 3 ] - Maior')
        sleep(0.3)
        print('[ 4 ] - Novos números')
        sleep(0.3)
        print('[ 5 ] - Sair do programa')
        sleep(0.5)
        opcao=int(input('---> '))

        soma = num1 + num2 + num3
        mult = num1 * num2 * num3

        if opcao==1:
            sleep(0.5)
            print(f'{num1}+{num2}+{num3}={num1 + num2 + num3}')

        elif opcao==2:
            sleep(0.5)
            print(f'{num1}x{num2}x{num3}={num1*num2*num3}')

        elif opcao==3:
            sleep(0.5)
            if num1>num2 and num1>num3:
                print(f'O número maior é {num1}')
            elif num2>num1 and num2>num3:
                print(f'O número maior é {num2}')
            elif num3>num1 and num3>num2:
                print(f'O número maior é {num3}')
            elif num1==num2 and num1>num3 and num2>num3:
                print(f'O 1º número ({num1}) e o 2º número ({num2}) são iguais e maiores que o 3º número ({num3})')
            elif num2==num3 and num2>num1 and num3>num1:
                print(f'O 2º número ({num2}) e o 3º número ({num3}) são iguais e maiores que o 1º número ({num1})')
            elif num3==num1 and num3>num2 and num1>num2:
                print(f'O 3º número ({num3}) e o 1º número ({num1}) são iguais e maiores que o 2º número ({num2})')
            else:
                print('Os números são iguais.')

        elif opcao==4:
            print('Selecione novos números...')
            sleep(0.5)

        elif opcao==5:
            sleep(0.5)
            print('A sair...')
            break
        else:
            print('Opção inválida.')
