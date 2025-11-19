# Crie um programa que leia um número de 0 a 20 introduzido pelo utilizador.
#Depois deverá mostrar por extenso o número introduzido.


n_extenso=('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
           'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
           'Dezasseis', 'Dezassete', 'Dezoito', 'Dezanove', 'Vinte')
utilizador=int(input('Digite um número entre 0 e 20--> '))

for c in range (0,len(n_extenso)):
    if c==utilizador:
        print(f'{c} --> {n_extenso[c]}')

#correção
numero=int(input('Digite um número entre 0 e 20: '))
print(n_extenso[numero])





