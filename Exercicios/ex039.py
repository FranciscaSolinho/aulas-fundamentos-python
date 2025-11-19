from datetime import datetime

maiores=0
menores=0
anoatual=datetime.now().year

for c in range (0, 7):
    a_nasc = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa:'))
    idade=anoatual-a_nasc

    if idade >= 18:
        maiores+=1
    else:
        menores+=1


print(f'No ano {anoatual}:')

print(f'Número de pessoas menores de idade: {menores} ')
print(f'Número de pessoas maiores de idade: {maiores} ')
