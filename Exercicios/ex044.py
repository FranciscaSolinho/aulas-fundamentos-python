print('---Número Fatorial---')

num=int(input('Digite um número: '))
con=num
calc=num

while True:
    if con !=1:
        calc=calc*(con-1)
        con-=1
    else:
        break

print(f'O fatorial de {num} é {calc}.')

'''correção:
while num>=1:
    if num==1:
        print(num, end=' = ')
    else:
        print(num, end=' x ')
    fatorial*=num
    num-=1
print(fatorial)'''