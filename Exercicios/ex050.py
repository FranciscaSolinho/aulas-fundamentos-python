maiores=0
menores=0
menores_masc=0
mulheres=0
homens=0

resposta=''
while resposta !='nao':
    idade=int(input('Digite a idade:'))
    while True:
        sexo=input('Digite o sexo[M/F]: ').strip().lower()
        if sexo!= 'm' and sexo != 'f':
            print('Por favor digite M ou F.')
        else:
            break

    if idade>25:
        maiores+=1
    if sexo == 'm' and idade <17:
        menores_masc+=1
    if sexo == 'f':
        mulheres+=1
    if idade <18:
        menores +=1

print(f'Maiores de idade: {maiores}')
print(f'Menores de idade: {menores}')
print(f'Menores de idade do sexo masculino: {menores_masc}')
print(f'Pessoas do sexo feminino registadas: {mulheres}')