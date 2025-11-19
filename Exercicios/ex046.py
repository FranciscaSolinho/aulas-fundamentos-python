num=''
contador=0
soma=0

print('~*º~*º Digite "0" quando quiser parar a contagem!º*~º*~')

while num !=0:
    num = int(input('~*ºDigite um número:'))
    soma += num

print(f'~*ºTotal da soma de todos os números indicados é: {soma}')



'''correção
soma=0
contador=0
while True:
    numero=int(input('Digite um número: '))
    if numero==0:
        break    
    soma+=numero
    contador+=1
print(f'A soma entre os valores digitados é: {soma}.')
print(f'Digitou {contador} números.')'''
