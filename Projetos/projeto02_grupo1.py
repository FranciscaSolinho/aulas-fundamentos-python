#Grupo1 - Francisca, Telmo, Victor

print('~*º~*º~*º Bem-Vindo ao Ghost Club º*~º*~º*~')

print('Vamos criar um registo?')

user1=input('Digite um username--> ').strip()

while True:
    mail1=input('Digite o seu email--> ').strip()
    mail2=mail1.find('@')
    mail3=mail1[mail2:]

    if '@' in mail1 and '.' in mail3:
        print('O seu email está disponível.')
        break
    else:
        print('Email inválido. Tente novamente.')

pass1=input('Crie uma palavra-passe--> ').strip()

print('~*º~*º MENU º*~º*~')
print('Digite a opção pretendida, seguido de <enter>:')
#sleep(1)
print('[1] - LOGIN')
print('[2] - SAIR')

while True:
    menu = int(input(''))

    if menu == 1:
        print('Pf introduza os seus dados:')
        break
    elif menu == 2:
        print('Saída efetuada com sucesso.')
        exit()
    else:
        print('Opção inválida. Pf selecione uma das opções disponiveis.')


login_user=input('Digite o seu username:').strip()
login_password=input('Digite a sua password:').strip()

if login_user == user1 and login_password == pass1:
    print('Bem-vindo!')
else:
    print('Erro, por favor digite os seus dados novamente.')
    login_user = input('Digite o seu username:').strip()
    login_password = input('Digite a sua password:').strip()

    if login_user == user1 and login_password == pass1:
        print('Bem-vindo!')
    else:
        print('A sua conta foi bloqueada.')
