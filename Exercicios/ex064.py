
#Crie um programa que leia o nome e a
#média de um aluno, calculando a sua
#situação, tudo dentro de um dicionário.
#No final mostre todo o conteúdo do
#dicionário.

#Situação:
#Média >= 9,5 – Aprovado
#Média < 9,5 - Reprovado

aluno= dict()
aluno['Nome'] = input(f'Digite o nome do aluno: ')
aluno['Média'] = float(input('Digite a média: '))
aluno['Situação'] = 'Aprovado' if aluno['Média'] >= 9.5 else 'Reprovado'

for chave, valor in aluno.items():
    print(f'{chave} -> {valor}')