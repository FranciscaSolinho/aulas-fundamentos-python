#Crie um programa que leia 5 números e
#guarde-os numa lista. No final mostre o
#maior e o menor valor e a respetiva
#posição na lista.

numeros=list()
#print(type(numeros))
indice_numeros=''
menor = maior = 0

for c in range (0, 5):
    numero=int(input(f'Digite o {c+1}º número: '))

    numeros.append(numero)
    indice_numeros = c

for indice, numero in enumerate(numeros):

    if numero==numeros[0]:
        menor=numero
        maior=numero
        maior_indice=indice
        menor_indice=indice
    else:
        if numero>maior:
            maior_indice=indice
            maior=numero
        if numero<menor:
            menor_indice=indice
            menor=numero


else:
    print(f'O número menor é {menor} e está na {menor_indice+1}ª posição.')

    print(f'O número maior é {maior} e está na {maior_indice+1}ª posição.')


numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)


#correção
numeros=[]

maior=max(numeros)
menor=min(numeros)

pos_maior=numeros.index(maior)
pos_menor=numeros.index(menor)

print(f'O maior valor encontrado foi {maior} na {pos_maior+1}ª posição.')
print(f'O menor valor encontrado foi {menor} na {pos_menor+1}ª posição.')




