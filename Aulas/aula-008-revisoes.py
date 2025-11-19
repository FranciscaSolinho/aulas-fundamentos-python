numero = int(input('Digite um número: '))
if numero > 10:
    print('Número superior a 10.')
elif numero==10:
    print('O número é igual a 10.')
else:
    print('O número não é superior a 10.')

for c in range(0, numero):
    print(c+1)

contador=0
while True:
    print(contador)
    if contador==10:
        break
    contador+=1

aluno = (1,5,7,6,3, 'Ricardo') #ou [] se quiser manipular os valores

for indice, valor in enumerate(aluno):
    print(f'No índice {indice} tem o valor {valor}')

