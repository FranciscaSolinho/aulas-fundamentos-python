#tuples
estante='Playstation'
print(estante)

estante='Xbox'
print(estante) #substitui o antigo

estante='Playstation', 'Xbox', 'Gameboy', 'Nintendo'
print(estante) #tuple

print(estante[0]) #estante no índice zero
#tuple é imutável
estante=input('Digite uma consola: '), input('Digite outra consola: ')

#formas de percorrer a linha de nomes:
nomes= ('Nádia', 'Júlia', 'Alexandra', 'Telmo', 'Victor',
        'Rafael', 'Daniel', 'Leticia',
        'Roman', 'Pedro', 'Francisca', 'Inês', 32, True, 3.14)

print(nomes)

for c in range (0, len(nomes)):
    print(f'No índice {c} está o nome:{nomes[c]}')

contador=0
for c in range (0, len(nomes)):
    print(f'No índice {contador} está o nome:{nomes[contador]}')
    contador+=1

for nome in nomes:
    print(nome)

#no canal do youtube tem aula sobre tuples

print(nomes[5])#Mostra o nome na posição 5 da lista atribuída.

for c in range (0, len(nomes)):
    print(f'{c}->{nomes[c]}')

for nome in nomes:
    if nome== 'Francisca':#com isto só imprime o nome que indiquei
    print(nome)

for indice, nome in enumerate(nomes):#parte em indices e no valor
    if indice%2==0:
        print(f'No índice {indice} o valor é {nome}.')

print(sorted(nomes))#Mostra por ordem alfabética.














