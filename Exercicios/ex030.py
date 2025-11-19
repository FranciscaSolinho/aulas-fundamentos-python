from random import randint

print(' ~*º~*º~*º PEDRA - PAPEL - TESOURA º*~º*~º*~ ')

print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogador=int(input('---> '))
cpu=randint(1,3)

if jogador==1:
    if cpu==1:
        print('Empate')
    elif cpu==2:
        print(f'Cpu ganha: Jogador --> {jogador} vs Cpu --> {cpu}')
    elif cpu==3:
        print(f'Jogador ganha: Jogador --> {jogador} vs Cpu --> {cpu}')
if jogador==2:
    if cpu==1:
        print(f'Jogador ganha: Jogador --> {jogador} vs Cpu --> {cpu}')
    elif cpu==2:
        print('Empate')
    elif cpu==3:
        print(f'Jogador ganha: Jogador --> {jogador} vs Cpu --> {cpu}')
if jogador==3:
    if cpu==1:
        print(f'Cpu ganha: Jogador --> {jogador} vs Cpu --> {cpu}')
    elif cpu==2:
        print(f'Jogador ganha: Jogador --> {jogador} vs Cpu --> {cpu}')
    elif cpu==3:
        print('Empate')
else:
    print('Inválido')