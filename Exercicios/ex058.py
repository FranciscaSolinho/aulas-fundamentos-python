#Crie um programa onde o utilizador
#insira 5 números dentro de uma lista.
#Os valores devem ser registados já na
#posição correta [ordem crescente] e no
#final mostre a lista ordenada.

#Não utilizar o sort()

numeros=[]
#indice_numeros+=1

for c in range (0, 5):
    numero=int(input(f'Digite o {c+1}º número: '))
    print(numeros)

    if c==0:
        numeros.append(numero)
        print('Primeiro valor inserido.')
        continue

    if numero>numeros[-1]:
        numeros.append(numero)
        print('Maior valor inserido.')
    else:
        indice_numeros=0
        while indice_numeros<len(numeros):
            if numero <= numeros[indice_numeros]:
                numeros.insert(indice_numeros,numero)
                print(f'Valor inserido na posição {indice_numeros+1}.')
                break
            indice_numeros+=1
print(numeros)


