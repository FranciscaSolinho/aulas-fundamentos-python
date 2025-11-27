#Crie um programa que tenha uma função que receba vários parâmetros como valores inteiros.
#O programa deve analisar todos os valores e dizer qual deles é o maior.



def valores():
    num_lista=list()
    num_maior=0
    contador = 0
    while True:
        contador+=1
        num=int(input(f'Digite o {contador}º número--> '))
        if num==0:
            break
        if num>num_maior:
            num_maior=num
        num_lista.append(num)

    final(num_lista,num_maior)


def final(num_lista,num_maior):
    print(f'{num_lista}')
    print(f'O maior número é: {num_maior}')


def menu():
    print('º~*º~* Análise de valores *~º*~º')
    print('Defina vários valores.')
    print('Digite 0 quando quiser terminar.')
    valores()

menu()

