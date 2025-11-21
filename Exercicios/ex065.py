#Crie um programa que sorteie a ordem de
#jogada num jogo ao “atirar um dado ao ar”.
#Cada jogador terá um número aleatório
#associado dentro de um dicionário.
#No final ordene o ranking para ver a ordem de jogada.

from random import randint

qtd_jogadores=4
jogadores=dict()
jogador=dict()
dado=list()

for c in range(qtd_jogadores):
    while True:
        qtd_dado=randint(1,6)
        if qtd_dado in dado:
            continue
        else:
            dado.append(qtd_dado)
            break

grupo=[]

for i in range(qtd_jogadores):
    jogador['Jogador']=input(f'Digite o nome do {i + 1}º jogador: ')
    jogador['Posição do dado']=dado[i]

while True:
    indice_jogadores = qtd_jogadores

    for i in range(qtd_jogadores,indice_jogadores):
        if grupo <= jogadores[indice_jogadores]:
            grupo=(indice_jogadores,qtd_jogadores)

            indice_jogadores+=1

    break

print(grupo)

#CORREÇÃO

qtd_jogadores=int(input('Digite o número de jogadores: '))
jogadores=dict()

for c in range (qtd_jogadores):
    #jogadores[input(f'Digite o nome do {c}º jogador: ')]=randint(1,6)
    nome=input(f'Digite o nome do {c}º jogador: ')
    jogada=randint(1,6)
    jogadores[nome]=jogada
    #em cima tem tudo isso numa linha (é melhor)

auxiliar=jogadores.copy()
print(jogador)
print(' ')
grupo=(jogador.copy())
ranking=list()
auxiliar = jogadores.copy()

while auxiliar:
    maior_jogador=''
    maior_valor=0

    for jogador, dado in auxiliar.items():
        if dado > maior_valor:
            maior_jogador=jogador
            maior_valor=dado

    ranking.append((maior_jogador,maior_valor))
    del auxiliar[maior_jogador]

print(ranking)

#ex do que quero ver [(j1, valor) , (j2, valor)]

for t in ranking:
    for e in t:
        print(f'{e}', end='')
        print()


