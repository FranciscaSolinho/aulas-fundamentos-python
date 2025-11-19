numero1=int(input('1º Número: '))
numero2=int(input('2º Número: '))

if numero1 > numero2:
    print(f'{numero1} é maior que {numero2}.')
elif numero1 < numero2:
    print(f'{numero1} é menor que {numero2}.')
else:
    print(f'{numero1} é igual a {numero2}.')