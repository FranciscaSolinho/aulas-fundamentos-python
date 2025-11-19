#Crie um programa onde o utilizador
#possa digitar vários números e guardá-los numa lista.
#Caso o número inserido esteja na lista ele não deve ser adicionado.
#No final mostre todos os valores por ordem DECRESCENTE.

numeros=list()
indice_numeros=''
contador=0

for c in range (0, 10):
    numero=int(input(f'Digite o {contador+1}º número: '))

    if numero not in numeros:
        numeros.append(numero)
        contador += 1
    else:
        print(f'O valor {numero} já se encontra na lista.')

numeros.sort()
print(f'listagem de números inseridos: {numeros}')
numeros.sort(reverse=True)
print(f'Ordem decrescente: {numeros}')