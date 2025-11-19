from random import randint
from time import sleep
print('~*º~*º~*º Jogo da Adivinha v2.0 º*~º*~º*~')
sleep(0.5)
computador=randint(0, 10)
tentativas=0

while True:
    tentativas+=1
    user=int(input('Tente adivinhar um número entre 0 e 10: '))
    if user == computador:
        print('Acertou!')
        sleep(0.5)
        break
    elif user < computador:
        print('Tente um valor mais alto...')

    elif user > computador:
        print('Tente um valor mais baixo...')

    else:
        print('Resposta inválida')

print(f'Total de tentativas:{tentativas}')
sleep(0.5)
print('Yay!!')