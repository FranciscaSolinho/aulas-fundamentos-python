'''
Melhore o exercício 61
A soma de todos os valores pares
A soma dos valores da segunda coluna
O maior valor da terceira linha
'''

numeros=list()
soma_valores_pares=0
soma_seg_coluna=0
maior_terceira_linha=''

for linha in range(0, 3):
    temp = list()
    for coluna in range(0, 3):
        num=int(input('Digite um número: '))

        if num%2==0:
            soma_valores_pares+=num

        if coluna==1:
            soma_seg_coluna+=num

        if linha==2:
            if coluna==0:
                maior_terceira_linha=num
            else:
                if num>maior_terceira_linha:
                    maior_terceira_linha=num


        temp.append(num)

    numeros.append(temp[:])


for lista in numeros:
    for valor in lista:
        print(valor, end=' ')
    print()

print(f'Soma valores pares: {soma_valores_pares}')
print(f'Soma valores da segunda coluna: {soma_seg_coluna}')
print(f'Maior valor da terceira linha: {maior_terceira_linha}')