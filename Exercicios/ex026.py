print('--- Calculadora de média ---')

nota1=float(input('Nota 1 --> '))
nota2=float(input('Nota 2 --> '))
nota3=float(input('Nota 3 --> '))
nota4=float(input('Nota 4 --> '))
nota5=float(input('Nota 5 --> '))

media=(nota1+nota2+nota3+nota4+nota5)/5
print('A sua média é:',media)
if media>=9.5:
    print(f'Parabéns, passou! A sua média é {media}.')
elif media >8:
    print(f'Em recuperação. A sua média é {media}.')
else:
    print(f'Reprovou. A sua média é {media}.')
