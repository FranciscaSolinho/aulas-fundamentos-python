jogos=('Animal Crossing: New Horizons',
       'Super Mario Party',
       'Fire Emblem Warriors',
       'Another Code: Recollection',
       'Pokemon Legends: Z-A',
       'Bayonetta')

precos=('59.99€',
        '59.99€',
        '59.99€',
        '59.99€',
        '69.99€',
        '29.99€')
#se fosse jogos e preços juntos teria dois indices um par (nomes dos jogos) e um impar (preços)

print(f'{"Lista de Jogos":-^60}')
print('_'*60)
print(f'{"Jogo": <54} Preço')
print(''*60)

for c in range (0,len(jogos)):
    if c%2==0:
        print(f'{jogos[c+1]:.<54}')
