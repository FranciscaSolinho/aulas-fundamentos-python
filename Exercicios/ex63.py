'''

Cria um programa que crie palpites para o euromilhões.
O programa deve perguntar quantas chaves serão geradas e deve sortear
aleatóriamente 5 números de 1 a 50 (sem repetir) e 2 estrelas de 1 a 12 (sem repetir).
Cada sorteio deve ser guardado numa lista composta.

'''

from random import randint

print('~*º~*º~*º Gerador de Chaves do Euromilhões º*~º*~º*~')
print(' ')

chaves=int(input('-- Digite o número de chaves que deseja gerar (máximo 5 chaves) --> '))
print(' ')
chave=list()
nums=list()
estrelas=list()

for r in range (0, chaves):
    resultado = list()

    for c in range(0, 5):
        while True:
            num = randint(1, 50)
            if num in nums:
                continue
            else:
                nums.append(num)
                break

    for c in range(0, 2):
        while True:
            num = randint(1, 12)
            if num in estrelas:
                continue
            else:
                estrelas.append(f'{num}* ')
                break

    chave.append(nums[:])
    chave.append(estrelas[:])

    print(chave)
    print('~*º~*º~*º~*º~*º~*º~*º~*º~*º~*º')
    print(' ')
    chave=list()
    nums=list()
    estrelas=list()

    for l in nums:
        for n in l:
            print(n, end=' ')



