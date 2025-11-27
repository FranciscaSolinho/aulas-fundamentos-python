#Crie um programa que tenha uma função que receba 3 parâmetros:
#inicio, fim e passo (tipo 1 3 5 7).
#O programa deve realizar 3 contagens através da função.
    #a) De 1 até 20, de 2 em 2;
    #b) De 10 até 0, de 1 em 1;
    #c) Contagem personalizada.

from time import sleep

def num1():
    for c in range(0,20,2):
        print(c)
        sleep(0.2)
    sleep(0.5)
    menu()
def num2():
    for i in range(10,-1,-1):
        print(i)
        sleep(0.2)
    sleep(0.5)
    menu()
def num3(inicio,fim,passo):
    for x in range(inicio,fim,passo):
        print(x)
        sleep(0.2)
    sleep(0.5)
    menu()

def menu():
    while True:
        print('--- MENU ---')
        print('[ 1 ] - Contagem de 1 até 20, de 2 em 2')
        print('[ 2 ] - Contagem de 10 até 0, de 1 em 1')
        print('[ 3 ] - Contagem personalizada')
        print('[ 4 ] - Sair')
        opcao=int(input('---> '))
        if opcao==1:
            num1()
        if opcao==2:
            num2()
        if opcao==3:
            inicio=int(input('Digite o número inicial da contagem--> '))
            fim=int(input('Digite  o número final da contagem--> '))
            passo=int(input('Defina o intervalo entre os números da sua contagem--> '))

            if inicio>fim:
                passo=-passo
                fim=fim-passo

            else:
                fim=fim+passo

            num3(inicio,fim,passo)
        elif opcao==4:
            print('A sair...')
            break
        else:
            print('Por favor, digite uma opção válida.')
            sleep(0.5)

menu()



