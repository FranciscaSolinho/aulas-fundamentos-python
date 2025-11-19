#contador que vai de 1 até 10

contador=1
while contador<=10:
    print(contador)
    contador+=1

#contador que vai de 10 até 0

contador=10

while contador<=0:
    print(contador)
    contador -=1

#criar um programa que some todos os números digitados pelo utilizador.
#Quantos? nsei, so sei que se o utilizador digitar 0, é para parar.

soma=0
num=('')
while num != 0:
    num=int(input('Digite um número:'))
    soma += num
print(soma)

#Criar um programa que peça o género de uma pessoa
#Apenas aceita como resposta M ou F.
#Se o utilizador digitar outra resposta, ele tem que pedir novamente.

genero=(' ')
while genero != 'M' and genero != 'F':
    genero=input('Digite o seu género: ').strip().upper()

#Quero criar um menu onde o utilizador pode escolher 3 opções
#Escrever 'Olá', 'Tudo bem?', sair do programa

#opcao = ''
#while opcao <=3:
while True:
    print('---- MENU ----')
    print('[ 1 ] - Olá')
    print('[ 2 ] - Tudo bem?')
    print('[ 3 ] - Sair.')
    opcao=int(input('---> '))

    if opcao==1:
        print('Olá')
    elif opcao==2:
        print('Tudo bem?')
    elif opcao==3:
        print('A sair...')
        break
    else:
        print('Opção inválida.')

#contagem de 0 até 1000

contador=-1

while True:
    print(contador)
    contador+=1

    if contador==1000:
        break

