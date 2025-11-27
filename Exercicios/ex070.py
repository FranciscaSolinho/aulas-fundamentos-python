#Crie um programa que tenha uma função chamada area()
#que receba as dimensões de um terreno e mostre a área do terreno.

def area(comprimento:float, largura:float):
    print(f'-- A área do terreno é --> {comprimento*largura}')

def menu():
    print('--- Calcule a área do terreno ---')
    n1 = int(input('-- Digite o comprimento --> '))
    n2 = int(input('-- Digite a largura --> '))
    area(n1,n2)

menu()