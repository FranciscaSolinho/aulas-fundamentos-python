from time import sleep

print(' ~*º~*º [DESENHADOR DE FORMAS] º*~º*~ ')
sleep(0.5)
print(' ~*º~*º UMA PRODUÇÃO DE º*~º*~')
sleep(0.5)
print(' ~*º~*º FRANCISCA º*~º*~')
print(' ~*º~*º INÊS º*~º*~')
print(' ~*º~*º PEDRO º*~º*~')
sleep(0.5)
opcao = 0

while True:
    c = 0
    print('[1] Escada à esquerda')
    print('[2] Escada à direita')
    print('[3] Pirâmide')
    print('[4] Cruz')
    print('[5] Sair')
    opcao = int(input('--> '))

    if opcao == 1:
        for c in range(1, 6):
            print('*'*c)
        print()

    elif opcao == 2:
        for c in range(1, 6):
            espaco=' '* (5-c)
            print(espaco + '*' * c)
            sleep(0.3)
        print()

    elif opcao == 3:
        altura = 5 # altura da piramide
        for c in range(0, altura + 1):
            for blank in range(0, altura - c): # espaços para centrar conforme o numero de estrelas (altura - contador)
                print(' ', end='')
            for estrela in range(1, 2 * c): # estrelas (o dobro do contador)
                print('*', end='')
            sleep(0.3)
            print()

        #tmbm pode ser:
        #for c in range (1, 6):
        #   espaco=''*(5-c)
        #   estrela='*'*(c*2-1)
        #print(f'{espaço}{estrela}')

    elif opcao == 4:
        altura = 5  # altura do x
        for c in range(altura): # contador altura
            for z in range(altura): # contador largura
                if z == c or z == altura - c - 1: # se altura = largura ou altura - altura - 1 = largura
                    print('*', end='')
                else:
                    print(' ', end='')
            sleep(0.3)
        print()

    elif opcao == 5:
        print('A sair.', end='')
        sleep(0.3)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        print('Obrigado')
        break

    else:
        print('Opção inválida tente novamente')