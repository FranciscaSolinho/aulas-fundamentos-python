#Crie um programa que gere 5 números
#aleatórios dentro de um tuple. Depois
#mostra a listagem de números gerados, o
#menor e o maior

from random import randint

numeros=(randint(0, 100),
         randint(0, 100),
         randint(0, 100),
         randint(0, 100),
         randint(0, 100))



print('-------------------------------------------------')
print(f'Números gerados aleatóriamente: {numeros}')

print('-------------------------------------------------')
print('Listagem de números gerados:')
menor=maior=0
for numero in sorted(numeros):
    print(f'\t-> {numero}', end='')
#print('-------------------------------------------------')
#print('Números do maior para o menor:')
    if numero==numeros[0]:
        menor=numero
        maior=numero
    else:
        if numero>maior:
            maior=numero
        if numero<menor:
            menor=numero
