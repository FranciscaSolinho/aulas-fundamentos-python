#Crie um programa com um tuple com os 20
#primeiros classificados do Campeonato
#Espanhol de Futebol. Depois mostre:

#a) Os primeiros 5 classificados.
#b) Os últimos 4 classificados.
#c) Uma lista com as equipas por ordem alfabética.
#d) A posição da equipa Las Palmas.

print('--- Campeonato Espanhol de Futebol: Top 20 ---')

top20=('Barcelona','Real Madrid','Atlético de Madrid',
'Athletic Club','Villarreal','Real Betis','Celta de Vigo',
'Rayo Vallecano','Osasuna','Mallorca','Real Sociedad',
'Valencia','Getafe','Espanyol','Alavés','Girona',
'Sevilla FC','Leganés','Las Palmas','Real Valladolid')

top20_pontos=('88 pontos','84 pontos','76 pontos',
'70 pontos','70 pontos','70 pontos','58 pontos',
'54 pontos','51 pontos','48 pontos','46 pontos',
'45 pontos','43 pontos','40 pontos',
'39 pontos','38 pontos','36 pontos',
'30 pontos','28 pontos','25 pontos')

print(f'a) Os primeiros 5 classificados: {top20[0]} com {top20_pontos[0]}, {top20[1]} com {top20_pontos[1]}, {top20[2]} com {top20_pontos[2]}, {top20[3]} com {top20_pontos[3]} e {top20[4]} com {top20_pontos[4]}')
print(f'b) Os últimos 4 classificados: {top20[16]} com {top20_pontos[16]}, {top20[17]} com {top20_pontos[16]}, {top20[18]} com {top20_pontos[18]} e {top20[19]} com {top20[19]}.')
print(f'c) Por ordem alfabética: {sorted(top20)}')
for indice, equipa in enumerate(top20):#parte em indices e no valor
    if equipa=='Las Palmas':
        print(f'd) Las Palmas encontra-se em {indice+1}º lugar.')

#correção
print('---------------------------------')
print('5 primeiros classificados:')
for indice, equipa in enumerate(top20):
    if indice==5:
        break
    else:
        print(f'\t{indice+1}º - {equipa}')
print('---------------------------------')
#ultimos classificados==len(top20)-1
#penultimo classificado==len(top20)-2
#etc
print('4 últimos classificados:')
for indice, equipa in enumerate(top20):
    if indice>=len(top20)-4:
        print(f'\t{indice + 1}º - {equipa}')
    else:
        continue

print('---------------------------------')
print('Equipas por ordem alfabética:')
for equipa in sorted(top20):
    print(f'\t{equipa}')

print('---------------------------------')
print('Posição da equipa Las Palmas:')

esta_la=False
indice_las_palmas=''

for indice, equipa in enumerate(top20):#parte em indice e valor
    if equipa=='Las Palmas':
        esta_la=True
        indice_las_palmas=indice
        #todo este código vai ser repetido (nsei pq é que isto ficou amarelo mas ok)
        #ele dps so mostra se las palmas estiver la caso contrario não mostra e mantém-se falso.

if esta_la:
    print(f'Las Palmas -> {indice_las_palmas+1}º lugar.')
else:
    print('Las Palmas não está classificado.')





