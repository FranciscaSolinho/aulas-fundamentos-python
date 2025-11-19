print('--- Calculadora ---')

print('[ 1 ] º*~º*~º Tabuada º~*º~*º')
print('[ 2 ] º*~º*~º Calculadora º~*º~*º')
print('[ 3 ] º*~º*~º Números pares º~*º~*º')
print('[ 4 ] º*~º*~º Sair º~*º~*º')

opcao = int(input('digite a sua opção:'))
print('Escolheu a opção:',opcao)

if opcao==1:
    print('º*~º*~º  t a b u a d a  º~*º~*º')
    tabuada=int(input('Digite um número: '))
    print(f'{tabuada} x 1 = {tabuada*1}')
    print(f'{tabuada} x 2 = {tabuada*2}')
    print(f'{tabuada} x 3 = {tabuada*3}')
    print(f'{tabuada} x 4 = {tabuada*4}')
    print(f'{tabuada} x 5 = {tabuada*5}')
    print(f'{tabuada} x 6 = {tabuada*6}')
    print(f'{tabuada} x 7 = {tabuada*7}')
    print(f'{tabuada} x 8 = {tabuada*8}')
    print(f'{tabuada} x 9 = {tabuada*9}')
    print(f'{tabuada} x 10 = {tabuada*10}')

elif opcao==2:
    print('º*~º*~º  C a l c u l a d o r a  º~*º~*º')
    operacao=(input('Digite a sua operação:'))

    #exemplos da correção:

    #operacao2 = (input('[+ - x / ]')) - n deu

    #if '+' in operacao:
        #operacao = '+'

    #cal1 = operacao[:]
    #pos=operacao.find('+')
    #cal1=int(operacao[:pos])
    #cal2=int(operacao[pos+1:])
    #print(f'{cal1}+{cal2}={cal1+cal2}')

    cal1=int(input('Digite um número: '))
    cal2=int(input('Digite outro número: '))

    if operacao == '+':
        print(f'{cal1}+{cal2}={cal1+cal2}')
    elif operacao=='-':
        print(f'{cal1}-{cal2}={cal1-cal2}')
    elif operacao== '/':
        print(f'{cal1}/{cal2}={cal1/cal2}')
    elif operacao== 'x':
        print(f'{cal1}*{cal2}={cal1*cal2}')

elif opcao==3:
    print('º*~º*~º  N ú m e r o s  p a r e s  º~*º~*º')
    num1=int(input('Digite um número: '))
    #o número par é quando o ultimo digito é: 0,2,4,6 ou 8.
    #o número impar é quando o ultimo digito é: 1,3,5,7 ou 9.
    if num1%2==0:
        print(f'{num1} é par.')
    else:
        print(f'{num1} é ímpar.')

elif opcao==4:
    print('º*~º*~º  B y e  B y e  º~*º~*º')
else:
    print('Opção Inválida')
