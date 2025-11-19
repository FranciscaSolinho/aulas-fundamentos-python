'''
Crie um programa que crie uma matriz 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz com a formatação adequada.
'''
numeros=list()

#exemplo: [[], [], []]
#exemplo: [[1,2,3],[4,5,6],[7,8,9]]

for linha in range(0, 3):
    temp = list()
    for coluna in range(0, 3):
        num=int(input('Digite um número: '))
        temp.append(num)

    numeros.append(temp[:])

print(numeros)  #explicação: [0] -> linha --> índice 0;
                # [2] -> coluna --> índice 2;
                # Resposta final => seria o 3º número digitado na primeira lista.
                # [ índice (linha) 0 ] [ índice (coluna) 2 ]

#for lista in numeros:
    #print(lista)#para cada lista imprime uma lista
                 # -> tipo em linhas diferentes em vez de seguidos
                 # -> tipo listas na mesma lista

for lista in numeros:
    for valor in lista:
        print(valor, end=' ')

