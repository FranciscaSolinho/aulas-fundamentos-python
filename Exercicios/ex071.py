#Crie um programa que tenha uma função que receba um texto como parâmetro
#e que mostre uma mensagem com tamanho adaptável.
#Ex:
#mostre(“Olá mundo.”)
#Saída:
#-=-=-=-=-=-=-=-=
#Olá mundo.
#-=-=-=-=-=-=-=-=

def cabecalho(txt):
    t_texto='-='*(len(txt))
    print(t_texto)
    print(f'{txt:^{len(t_texto)}}')
    print(t_texto)

def texto():
    txt=input('Digite o seu texto-->')
    cabecalho(txt)

texto()



