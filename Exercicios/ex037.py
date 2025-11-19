cont=0

num1=int(input('Digite um número:'))

for c in range(0, num1):
    if num1%(c+1)==0:
        cont=cont+1
if cont == 2:
    print(f'O {num1} é primo.')
else:
    print(f'O {num1} não é primo')
