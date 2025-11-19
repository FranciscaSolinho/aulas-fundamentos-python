#range(inicio, fim, passo)
from time import sleep

for c in range(0, 5, 2):#passo para ser de 2 em 2)Se começar no zero o numero de vezes que qero repetir pode ser indicado no numero seguinte
    print(c+1)#o +1 é para começar especificamente no 1 em vez do 0
    sleep(0.5)

print('')
print('')

soma=0
for c in range(0, 5):
    print(f'O valor da soma é:{soma}')
    nota=float(input(f'digite a {c+1}ª nota:'))
    soma += nota #para calcular a média das notas registadas. É o mesmo que soma=soma+nota
print(soma/5)

print('')
print('')

#contagem decrescente:
for c in range(5, 0, -1):
    print(c)

numero=7
for c in range(0, 10):
    print(f'{numero}x{c+1}={numero*(c+1)}')

