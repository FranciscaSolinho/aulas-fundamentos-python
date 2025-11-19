
resposta=('')
print('As batatas nascem a partir da terra?')
while resposta != 'V' and resposta != 'F':
    resposta=input('[V/F]:').strip().upper()
    if resposta=='V':
        print('Acertou!')
    elif resposta=='F':
        print('Errou...')
    else:
        print('Resposta inválida.')

resposta=('')
print('O arco íris tem 30 cores?')
while resposta != 'V' and resposta != 'F':
    resposta=input('[V/F]:').strip().upper()
    if resposta=='V':
        print('Errou...')
    elif resposta=='F':
        print('Acertou!')
    else:
        print('Resposta inválida.')

print('O pai natal celebra Páscoa?')
while True:
    resposta=input('[V/F]:').strip().upper()
    if resposta=='V':
        print('Errou...')
        break
    elif resposta=='F':
        print('Acertou!')
        break
    else:
        print('Resposta inválida.')