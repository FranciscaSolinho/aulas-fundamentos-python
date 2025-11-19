valores=(int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))
qtd_sete=0
indice_cinco=''
existe_cinco=True

for c in range (0, len(valores)):
    if valores[c]==7:
        qtd_sete+=1
    if existe_cinco:
        if (valores[c]==5):
            indice_cinco=c
        else:
            existe_cinco=False

if qtd_sete>0:
    print(f'O número sete foi digitado {qtd_sete} vezes.')
else:
    print('O número sete não foi digitado.')

if indice_cinco:
    print(f'O cinco foi digitado na {indice_cinco} posição.')
else:
    print('Não foi encontrado nenhum cinco.')

