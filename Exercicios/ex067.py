jogador=dict()

jogador['Nome']=input('Digite o nome do jogador: ')
jogador['qtd_jogos']=int(input('Digite a quantidade de jogos realizados: '))
jogador['golos']=int(input('Digite quantos golos marcou: '))
jogador['media']=jogador['golos']/jogador['qtd_jogos']

print(jogador)

for chave, valor in jogador.items():
    print(f'{chave}->{valor}')