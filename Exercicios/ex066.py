from datetime import datetime
from time import sleep

print('--- Simulador de Crédito de Habitação ---')
print('--- Simples e sem taxas! ---')

cliente=dict()
ano_atual=datetime.now().year
cliente['nome']=(input('--- Digite o seu nome: '))
cliente['data_nascimento']=int(input('--- Digite o seu ano de nascimento: '))
cliente['rendimentos_mensais']=float(input('--- Digite os seus rendimentos mensais: '))
cliente['despesas_mensais']=float(input('--- Digite as suas despesas mensais: '))
cliente['montante_credito']=float(input('--- Digite o montante de crédito: '))
cliente['prazo']=int(input('--- Digite o prazo previsto para liquidação do crédito(em anos): '))
cliente['idade']=ano_atual-cliente['data_nascimento']
cliente['remanescente']=cliente['rendimentos_mensais']-cliente['despesas_mensais']
cliente['mensalidade']=cliente['montante_credito']/(cliente['prazo']*12)

cliente['situação']='Aprovado' if cliente['remanescente'] > cliente['mensalidade'] else 'Reprovado'

print(f'A analisar a situação do cliente {cliente['nome']}', end='')
for c in range(3):
    print('.', end='')
sleep(0.5)
print()

for chave, valor in cliente.items():
    print(f'{cliente['situação']}', end='')



