jogadores=list()

for c in range(len(nomes)):
    jogador=dict()
    jogador['Nome']=input('Digite o nome do jogador: ')
    jogador['Partidas']=int(input('Digite o número de partidas: '))
    jogador['Golos']=int(input('Digite o número de golos: '))
    jogador['Média']=jogador['Golos']/jogador['Partidas']

while True:
    print('--- Sistema de Consulta de Jogadores ---')
    print('[1] - Lista de Jogadores ')
    print('[2] - Melhor marcador')
    print('[3] - Pesquisar pelo nome')
    print('[4] - Ranking')
    print('[5] - Registar novo jogador')
    print('[6] - Sair')
