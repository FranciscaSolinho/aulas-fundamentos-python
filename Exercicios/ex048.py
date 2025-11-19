print('~*º~*º Tabuada v2.0 º*~º*~')
print('O programa é interrompido quando digita "0" ou um valor negativo.')

num=1
calc=0

while True:
    while num>0:
        num=int(input('Digite um número:'))

        if num<=0:
            break

    for c in range(0, 10):
        print(f'{num}x{calc + 1}={num*calc+1}')