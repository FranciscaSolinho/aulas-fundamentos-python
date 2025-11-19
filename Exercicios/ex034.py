pares=0

for c in range(0, 10):
    num1=int(input(f'digite o {c+1}º número:'))
    if num1%2==0:
        print(f'O {num1} é par')
        pares=pares+1
    else:
        print(f'O {num1} é impar')

print(f'Total de números pares: {pares}')



