from math import fsum
#ex1
notas=list() #também pode ser "notas=(1,2,3,4,...)" sem escrever "list" também dá para usar parêntesis retos
print(type(notas))

for c in range (0, 5):
    nota=float(input(f'Digite a {c+1}ª nota: '))

    notas.append(nota)
    print(notas)

media=fsum(notas)/len(notas)
print(f'A média das notas inseridas é: {media}.')

#ex2
nomes=['Nádia', 'Júlia', 'Francisca', 'Telmo', 'Alexandra', 'Inês', 'Victor', 'Daniel']
print(nomes)

nomes.append('João')
print(nomes)

nomes.insert(0, 'Luanna')
print(nomes)

nomes.pop()
print(nomes)

#ex3

series=list()

print(series)

while True:
    print('1 - inserir novo top 5')
    print('2 - Substituir série')
    print('3 - Mostrar top 5')
    print('4 - Sair')
    opcao=int(input('--->'))
    match opcao:
        case 1:
            print('Insere o teu top 5 de séries: ')
            for c in range(0, 5):
                serie = input(f'{c + 1}ª--> ')
                series.append(serie)
        case 2:
            nova_serie=input('Digite a nova série: ')
            serie_remover=input('Digite a série a remover: ')

            indice_serie_remover=series.index(serie_remover)
            series[indice_serie_remover]=nova_serie
            print('Série alterada com sucesso!')

        case 3:
            for indice, serie in enumerate(series):
                print(f'{indice+1}ª --> {serie}')

        case 4:
            print('A sair...')
            break

        case _:
            print('Opção Inválida')




            #if serie_remover in series:
                #series.remove(serie_remover)


